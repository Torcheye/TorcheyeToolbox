# Shape Generator Constitution

## Core Principles

### I. Simplicity First
- Single HTML file with embedded CSS and JavaScript (when possible)
- No build tools or complex dependencies required
- Client-side only - no backend server needed
- Works offline after initial load

### II. Canvas-Based Rendering
- All image generation uses HTML5 Canvas API
- Support both 2D context and basic WebGL for performance
- Efficient rendering with requestAnimationFrame for animations
- Clear canvas manipulation with undo/redo support

### III. User Experience
- Intuitive controls with real-time preview
- Immediate visual feedback for all parameter changes
- Export images in common formats (PNG, JPG, SVG)
- Mobile-responsive design (works on touch devices)

### IV. Minimal but Complete
- Focus on core shape generation (circles, squares, polygons, lines)
- Basic customization: colors, sizes, positions, rotations
- Simple UI with sliders, color pickers, and number inputs
- Download functionality with filename customization

### V. Browser Compatibility
- Support modern browsers (Chrome, Firefox, Safari, Edge)
- Graceful degradation for older browsers
- No experimental/bleeding-edge APIs without fallbacks
- Test on desktop and mobile viewports

## Technical Requirements

**Technology Stack:**
- Pure HTML5, CSS3, and vanilla JavaScript
- HTML5 Canvas API for rendering
- No frameworks required (optional: use simple libraries if needed)
- Local storage for saving user preferences

**Performance Standards:**
- Initial page load under 1 second
- Real-time preview updates (< 16ms per frame for 60fps)
- Image export under 2 seconds for typical sizes
- Memory efficient (no canvas memory leaks)

## Development Workflow

**Development Process:**
- Start with working prototype, iterate on features
- Test in multiple browsers before finalizing
- Keep code readable and well-commented
- Validate HTML/CSS/JS with standard linters

**Quality Gates:**
- Manual testing in Chrome, Firefox, and Safari
- Mobile device testing (or responsive mode)
- Verify all export formats work correctly
- Check accessibility basics (keyboard navigation, labels)

## Governance

This constitution defines the bare minimum requirements for the Shape Generator web app. Any feature additions must maintain the simplicity and client-side nature of the application. Complexity must be justified by clear user value.

**Version**: 1.0.0 | **Ratified**: 2025-11-04 | **Last Amended**: 2025-11-04
