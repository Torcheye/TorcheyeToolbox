# Research: Vector Shape Generator

**Phase**: 0 - Outline & Research
**Date**: 2025-11-04
**Status**: Complete

## Overview

This document captures research findings and technical decisions for implementing the Vector Shape Generator web application. All unknowns from the Technical Context have been researched and resolved with concrete decisions.

## Technology Decisions

### 1. Rendering Engine: HTML5 Canvas vs SVG

**Decision**: HTML5 Canvas API (CanvasRenderingContext2D)

**Rationale**:
- **PNG Export Requirement**: Canvas provides native `toDataURL('image/png')` and `toBlob()` methods for pixel-perfect PNG generation
- **Performance**: Canvas raster rendering is faster for real-time updates (<16ms requirement) compared to SVG DOM manipulation
- **DPI Control**: Canvas allows precise pixel-level control for high-DPI exports (300 DPI for print)
- **Simplicity**: Direct drawing API without DOM overhead

**Alternatives Considered**:
- **SVG**: Better for scalability and future vector export, but:
  - PNG export requires additional rasterization step (using foreignObject or external libraries)
  - DOM manipulation overhead impacts real-time preview performance
  - More complex for pixel-perfect rendering at specific resolutions
- **Hybrid Approach**: Maintain both Canvas and SVG representations
  - Rejected due to increased complexity and code duplication
  - Violates constitution principle I (Simplicity First)

### 2. Color Picker Implementation

**Decision**: Native HTML5 `<input type="color">` with custom hex/RGB inputs

**Rationale**:
- **Zero Dependencies**: Native browser support across all target browsers (Chrome 90+, Firefox 88+, Safari 14+)
- **Accessibility**: Built-in keyboard navigation and screen reader support
- **Alpha Channel**: Supplement with separate opacity slider (0-100%) for RGBA support
- **User Familiarity**: Native color picker UX matches OS conventions

**Alternatives Considered**:
- **Third-party libraries** (e.g., Pickr, Spectrum, vanilla-picker):
  - More features (alpha in single picker, HSL sliders, swatches)
  - Rejected to maintain zero-dependency principle
  - Can be added later if native input proves insufficient
- **Custom CSS-only color picker**:
  - Full control over UX
  - Rejected due to implementation complexity (100+ LOC) and accessibility concerns

### 3. Range Slider Controls

**Decision**: Native HTML5 `<input type="range">` with custom CSS styling

**Rationale**:
- **Native Performance**: Hardware-accelerated, smooth dragging
- **Accessibility**: Built-in ARIA attributes and keyboard support (arrow keys)
- **Customizable**: CSS custom properties allow clean, modern styling
- **Mobile Support**: Touch-friendly with large hit areas

**Best Practices**:
- Always pair with `<input type="number">` for precise value entry
- Use `step` attribute for appropriate granularity (e.g., `step="0.5"` for outline thickness)
- Display current value in real-time next to slider
- CSS custom properties for consistent theming:
  ```css
  input[type="range"] {
    --track-color: #e0e0e0;
    --thumb-color: #007bff;
    --thumb-size: 20px;
  }
  ```

### 4. PNG Export with DPI Support

**Decision**: Canvas scaling approach with pixel ratio calculation

**Rationale**:
- **DPI Conversion**: Scale canvas dimensions by (targetDPI / 72) to achieve desired print resolution
  - Example: 100px at 72 DPI → 417px at 300 DPI (100 × 300/72)
- **Preserve Aspect Ratio**: Maintain visual proportions when scaling
- **Memory Efficiency**: Create temporary canvas for export, destroy after blob generation

**Implementation Pattern**:
```javascript
function exportToPNG(width, height, dpi) {
  const scale = dpi / 72;
  const exportCanvas = document.createElement('canvas');
  exportCanvas.width = width * scale;
  exportCanvas.height = height * scale;

  const ctx = exportCanvas.getContext('2d');
  ctx.scale(scale, scale);

  // Redraw shape at scaled resolution
  drawShape(ctx, shapeData);

  // Export as blob
  exportCanvas.toBlob(blob => {
    // Trigger download
  }, 'image/png');
}
```

**Alternatives Considered**:
- **Server-side rendering**: Node.js with node-canvas
  - Rejected per constitution (client-side only)
- **External libraries**: html2canvas, dom-to-image
  - Rejected due to dependency footprint and unnecessary features

### 5. State Management

**Decision**: Plain JavaScript object with event-driven updates

**Rationale**:
- **Simplicity**: No framework overhead, easy to understand
- **Performance**: Direct object mutation with targeted redraws
- **Reactive Updates**: Custom event system for UI synchronization

**State Structure**:
```javascript
const state = {
  shapeType: 'circle', // 'circle' | 'rectangle'
  circle: {
    radius: 100,
    fillColor: '#ffffff',
    strokeColor: '#000000',
    strokeWidth: 2,
    opacity: 100
  },
  rectangle: {
    width: 200,
    height: 150,
    fillColor: '#ffffff',
    strokeColor: '#000000',
    strokeWidth: 2,
    opacity: 100
  },
  export: {
    width: 800,
    height: 600,
    dpi: 72
  }
};

function updateState(path, value) {
  // Deep set value
  // Trigger canvas redraw
  // Update UI inputs
}
```

**Alternatives Considered**:
- **React/Vue/Svelte**: Overkill for single-page app, violates zero-dependency principle
- **Web Components**: Future consideration, but adds complexity to MVP
- **Proxy-based reactivity**: Elegant but harder to debug, deferred to future iterations

### 6. Layout and Styling

**Decision**: CSS Grid for main layout, Flexbox for control panels

**Rationale**:
- **Grid**: Two-column layout (canvas preview | control panel)
  - Responsive breakpoints for smaller screens
  - Easy to center canvas with `place-items: center`
- **Flexbox**: Vertical stacking of control groups
  - Natural flow for form controls
  - Simple alignment with `gap` property

**Design System**:
- **Typography**: System font stack (`-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto`)
- **Spacing**: 8px base unit (0.5rem, 1rem, 1.5rem, 2rem)
- **Colors**: Neutral grays with accent blue (#007bff)
- **Border Radius**: 8px for cards, 4px for inputs
- **Shadow**: Subtle elevation (`box-shadow: 0 2px 8px rgba(0,0,0,0.1)`)

### 7. Browser Feature Detection

**Decision**: Graceful degradation with Canvas support check

**Implementation**:
```javascript
function checkCanvasSupport() {
  const canvas = document.createElement('canvas');
  const supported = !!(canvas.getContext && canvas.getContext('2d'));

  if (!supported) {
    document.body.innerHTML = `
      <div class="error">
        <h1>Browser Not Supported</h1>
        <p>This application requires HTML5 Canvas support.</p>
        <p>Please upgrade to a modern browser.</p>
      </div>
    `;
  }

  return supported;
}
```

### 8. Validation Strategy

**Decision**: Client-side validation with visual feedback

**Validation Rules**:
- **Dimensions**: Positive numbers, max 5000px (FR-016)
- **Outline thickness**: 0.5-50px range
- **DPI**: Common values (72, 150, 300) with manual entry support
- **Colors**: Valid hex codes (#RRGGBB) or use native picker

**Error Display**:
- Inline error messages below invalid inputs
- Red border on invalid fields
- Disable export button until all validations pass

## Performance Optimization

### Real-time Preview (<16ms target)

**Strategies**:
1. **Debouncing**: Delay rapid slider updates to 16ms intervals
2. **RequestAnimationFrame**: Queue redraws to sync with browser refresh
3. **Partial Redraws**: Only clear and redraw affected regions (future optimization)
4. **Canvas Caching**: Pre-render static elements (future optimization)

### Memory Management

**Strategies**:
1. **Temporary Canvas Disposal**: Clear references after PNG export
2. **Event Listener Cleanup**: Remove listeners on state updates
3. **Avoid Memory Leaks**: No global event listeners without cleanup

## Testing Strategy

### Manual Testing Checklist

**Browser Compatibility**:
- [ ] Chrome 90+ (Windows, macOS)
- [ ] Firefox 88+ (Windows, macOS)
- [ ] Safari 14+ (macOS, iOS)
- [ ] Edge 90+ (Windows)

**Functional Testing**:
- [ ] Circle creation and customization
- [ ] Rectangle creation and customization
- [ ] Color picker functionality (fill, stroke)
- [ ] Opacity slider (0-100%)
- [ ] Real-time preview updates
- [ ] Shape type switching
- [ ] PNG export at 72 DPI
- [ ] PNG export at 300 DPI
- [ ] Export validation (invalid dimensions)
- [ ] File download with correct filename

**Performance Testing**:
- [ ] Slider drag performance (60fps)
- [ ] Export speed (<2s for 1000x1000px)
- [ ] Initial page load (<1s)

**Edge Cases**:
- [ ] Minimum values (radius: 1px, thickness: 0.5px)
- [ ] Maximum values (radius: 1000px, export: 5000x5000px)
- [ ] Identical fill/stroke colors
- [ ] Fully transparent shapes (opacity: 0%)
- [ ] Invalid export dimensions (0, negative, >5000)

### Optional Automated Testing

**Unit Tests** (Jest, if complexity grows):
- Color conversion utilities (hex ↔ RGBA)
- DPI scaling calculations
- Validation functions
- State update logic

**Not Required for MVP**: Integration or E2E tests (manual testing sufficient)

## Open Questions Resolved

### Q1: Should we support additional color formats (HSL, named colors)?

**Answer**: No for MVP. Native `<input type="color">` returns hex values. Add hex input field for manual entry. HSL can be added in future iterations if user feedback requests it.

### Q2: How to handle high-DPI displays (Retina, 4K)?

**Answer**: Canvas automatically scales to devicePixelRatio for preview. Export uses explicit DPI parameter, independent of display DPI. No additional handling needed.

### Q3: Should shapes be anti-aliased?

**Answer**: Yes. Canvas 2D context has anti-aliasing enabled by default (`imageSmoothingEnabled: true`). Provides smoother edges for circles and diagonal lines.

### Q4: How to handle extremely large export dimensions (memory limits)?

**Answer**: Enforce maximum 5000x5000px limit (FR-016). At 300 DPI, this supports ~17x17 inch prints (adequate for most use cases). Larger exports would risk browser crashes on low-memory devices.

### Q5: Should we persist user preferences across sessions?

**Answer**: Optional enhancement. Use `localStorage` to save last-used values (colors, dimensions). Load on page init. Improves UX for repeat users. Low complexity, high value.

## Dependencies and Libraries

**Final Dependency List**: None (Zero-dependency architecture)

**Rationale**: All requirements achievable with native browser APIs:
- HTML5 Canvas API (rendering, export)
- Native form inputs (color picker, range sliders, number inputs)
- CSS Grid/Flexbox (layout)
- LocalStorage API (optional persistence)

**Future Considerations** (if scope expands):
- Color manipulation library (e.g., chroma.js) for advanced color features
- FileSaver.js for better cross-browser download support (if native download fails)
- Jest for automated testing (if codebase exceeds 1000 LOC)

## Conclusion

All technical unknowns have been resolved. The implementation plan uses proven web standards (HTML5 Canvas, native form inputs, CSS Grid) with zero external dependencies. This aligns with the constitution's Simplicity First principle while meeting all functional requirements and success criteria from the feature spec.

**Ready to proceed to Phase 1**: Data model and API contracts design.
