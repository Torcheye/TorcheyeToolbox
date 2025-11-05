# Quickstart Guide: Vector Shape Generator

**Feature**: Vector Shape Generator
**Branch**: `001-shape-generator`
**Target Audience**: Developers implementing this feature

---

## Overview

The Vector Shape Generator is a single-file web application that allows users to create and customize primitive vector shapes (circles and rectangles) with real-time preview and PNG export. This guide will help you get started with development.

---

## Prerequisites

### Required Knowledge
- HTML5, CSS3, JavaScript ES6+
- Canvas API basics
- DOM manipulation
- Event handling

### Required Tools
- **Code Editor**: VS Code, Sublime Text, or any text editor
- **Web Browser**: Chrome 90+, Firefox 88+, or Safari 14+ (for testing)
- **Local Server** (optional): Python's `http.server`, Node's `http-server`, or VS Code's Live Server extension

### No Build Tools Required
This project uses vanilla JavaScript with no build step, bundlers, or transpilation.

---

## Quick Start (5 Minutes)

### Option 1: Direct File Opening

1. **Create project directory**:
   ```bash
   mkdir shape-generator
   cd shape-generator
   ```

2. **Create `index.html`**:
   ```bash
   touch index.html
   ```

3. **Open in browser**:
   ```bash
   # macOS
   open index.html

   # Windows
   start index.html

   # Linux
   xdg-open index.html
   ```

### Option 2: Local Server (Recommended)

1. **Start a local server**:

   **Using Python**:
   ```bash
   # Python 3
   python -m http.server 8000

   # Python 2
   python -m SimpleHTTPServer 8000
   ```

   **Using Node.js (npx)**:
   ```bash
   npx http-server -p 8000
   ```

   **Using VS Code Live Server**:
   - Install "Live Server" extension
   - Right-click `index.html` → "Open with Live Server"

2. **Open in browser**:
   ```
   http://localhost:8000/index.html
   ```

---

## Project Structure

```
shape-generator/
├── index.html           # Single-file application (ALL code here)
├── README.md            # User documentation
└── assets/              # (Optional) Icons, favicons
    └── favicon.ico
```

**Note**: All HTML, CSS, and JavaScript code lives in `index.html`. This single-file architecture maximizes portability and eliminates build complexity.

---

## Architecture Overview

### High-Level Components

```
┌─────────────────────────────────────────────┐
│              index.html                     │
├─────────────────────────────────────────────┤
│  HTML Structure                             │
│  ├── Canvas (preview)                       │
│  ├── Controls Panel (shape selector, props) │
│  └── Export Dialog (dimensions, DPI)        │
├─────────────────────────────────────────────┤
│  CSS Styles (embedded <style>)              │
│  ├── Grid layout (canvas | controls)        │
│  ├── Form controls styling                  │
│  └── Modal dialog styling                   │
├─────────────────────────────────────────────┤
│  JavaScript Modules (embedded <script>)     │
│  ├── State Management                       │
│  ├── Canvas Renderer                        │
│  ├── Event Handlers                         │
│  ├── Validation                             │
│  └── Export Manager                         │
└─────────────────────────────────────────────┘
```

### Data Flow

```
User Interaction → Event Handler → Validation → State Update → Canvas Render
                                                      ↓
                                              LocalStorage Persist
```

---

## Development Workflow

### Phase 1: HTML Structure (30 min)

**Goal**: Create semantic HTML layout

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vector Shape Generator</title>
</head>
<body>
  <!-- Main container -->
  <div class="app-container">
    <!-- Canvas preview area -->
    <div class="canvas-area">
      <canvas id="preview-canvas" width="600" height="600"></canvas>
    </div>

    <!-- Controls panel -->
    <div class="controls-panel">
      <!-- Shape selector -->
      <section class="shape-selector">
        <label>Shape Type:</label>
        <select id="shape-type">
          <option value="circle">Circle</option>
          <option value="rectangle">Rectangle</option>
        </select>
      </section>

      <!-- Circle controls -->
      <section id="circle-controls" class="shape-controls">
        <div class="control-group">
          <label for="circle-radius">Radius:</label>
          <input type="range" id="circle-radius" min="1" max="1000" value="100">
          <input type="number" id="circle-radius-num" min="1" max="1000" value="100">
        </div>
        <!-- Add fill color, stroke color, stroke width, opacity -->
      </section>

      <!-- Rectangle controls -->
      <section id="rectangle-controls" class="shape-controls" style="display:none;">
        <!-- Similar structure for width, height, colors, etc. -->
      </section>

      <!-- Export button -->
      <button id="export-btn">Export to PNG</button>
    </div>
  </div>

  <!-- Export modal (hidden by default) -->
  <div id="export-modal" class="modal">
    <!-- Export settings form -->
  </div>

  <style>
    /* CSS goes here */
  </style>

  <script>
    /* JavaScript goes here */
  </script>
</body>
</html>
```

**Checklist**:
- [ ] Canvas element with appropriate dimensions
- [ ] Shape type selector (circle/rectangle)
- [ ] Input controls for all shape properties
- [ ] Export button and modal dialog
- [ ] Semantic HTML (sections, labels, forms)

---

### Phase 2: CSS Styling (1 hour)

**Goal**: Clean, modern design with responsive layout

**Key Patterns**:

```css
/* CSS Grid for main layout */
.app-container {
  display: grid;
  grid-template-columns: 2fr 1fr; /* Canvas 2/3, Controls 1/3 */
  gap: 2rem;
  height: 100vh;
  padding: 2rem;
}

/* Center canvas */
.canvas-area {
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f5f5f5;
  border-radius: 8px;
}

/* Control panel styling */
.controls-panel {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  padding: 1.5rem;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* Range slider styling */
input[type="range"] {
  width: 100%;
  accent-color: #007bff;
}

/* Color picker styling */
input[type="color"] {
  width: 60px;
  height: 40px;
  border: 1px solid #ddd;
  border-radius: 4px;
  cursor: pointer;
}
```

**Design Tokens**:
- **Colors**: Primary (#007bff), Neutral (#f5f5f5, #e0e0e0, #333)
- **Spacing**: 0.5rem, 1rem, 1.5rem, 2rem (8px base unit)
- **Typography**: System font stack, 16px base, 1.5 line-height
- **Shadows**: `0 2px 8px rgba(0,0,0,0.1)` for elevation

**Checklist**:
- [ ] Responsive grid layout
- [ ] Clean form control styling
- [ ] Modal overlay and dialog
- [ ] Focus states for accessibility
- [ ] Consistent spacing and typography

---

### Phase 3: State Management (1 hour)

**Goal**: Centralized state with update functions

```javascript
// Initialize state
const state = {
  currentShape: 'circle',
  shapes: {
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
    }
  },
  exportSettings: {
    width: 800,
    height: 600,
    dpi: 72,
    filename: 'shape-export'
  }
};

// Update function
function updateShape(property, value) {
  const shapeType = state.currentShape;
  state.shapes[shapeType][property] = value;

  // Trigger side effects
  renderCanvas();
  savePreferences();
}

// Switch shape type
function switchShape(newType) {
  state.currentShape = newType;

  // Update UI visibility
  document.getElementById('circle-controls').style.display =
    newType === 'circle' ? 'block' : 'none';
  document.getElementById('rectangle-controls').style.display =
    newType === 'rectangle' ? 'block' : 'none';

  renderCanvas();
}
```

**Checklist**:
- [ ] State object with all required fields
- [ ] Update functions for shape properties
- [ ] Shape switching logic
- [ ] LocalStorage persistence (optional)

---

### Phase 4: Canvas Rendering (2 hours)

**Goal**: Real-time shape rendering with Canvas API

```javascript
// Get canvas context
const canvas = document.getElementById('preview-canvas');
const ctx = canvas.getContext('2d');

// Clear canvas
function clearCanvas() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = '#ffffff';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
}

// Draw circle
function drawCircle(shape) {
  const centerX = canvas.width / 2;
  const centerY = canvas.height / 2;

  ctx.save();
  ctx.globalAlpha = shape.opacity / 100;

  // Fill
  ctx.fillStyle = shape.fillColor;
  ctx.beginPath();
  ctx.arc(centerX, centerY, shape.radius, 0, Math.PI * 2);
  ctx.fill();

  // Stroke
  if (shape.strokeWidth > 0) {
    ctx.strokeStyle = shape.strokeColor;
    ctx.lineWidth = shape.strokeWidth;
    ctx.stroke();
  }

  ctx.restore();
}

// Draw rectangle
function drawRectangle(shape) {
  const centerX = canvas.width / 2;
  const centerY = canvas.height / 2;
  const x = centerX - (shape.width / 2);
  const y = centerY - (shape.height / 2);

  ctx.save();
  ctx.globalAlpha = shape.opacity / 100;

  // Fill
  ctx.fillStyle = shape.fillColor;
  ctx.fillRect(x, y, shape.width, shape.height);

  // Stroke
  if (shape.strokeWidth > 0) {
    ctx.strokeStyle = shape.strokeColor;
    ctx.lineWidth = shape.strokeWidth;
    ctx.strokeRect(x, y, shape.width, shape.height);
  }

  ctx.restore();
}

// Main render function
function renderCanvas() {
  clearCanvas();

  const shapeType = state.currentShape;
  const shape = state.shapes[shapeType];

  if (shapeType === 'circle') {
    drawCircle(shape);
  } else if (shapeType === 'rectangle') {
    drawRectangle(shape);
  }
}
```

**Checklist**:
- [ ] Canvas context initialization
- [ ] Clear canvas function
- [ ] Draw circle with fill and stroke
- [ ] Draw rectangle with fill and stroke
- [ ] Opacity support
- [ ] Centered positioning

---

### Phase 5: Event Handlers (1 hour)

**Goal**: Connect UI inputs to state updates

```javascript
// Shape type selector
document.getElementById('shape-type').addEventListener('change', (e) => {
  switchShape(e.target.value);
});

// Circle radius slider
document.getElementById('circle-radius').addEventListener('input', (e) => {
  const value = parseInt(e.target.value);
  document.getElementById('circle-radius-num').value = value;
  updateShape('radius', value);
});

// Circle radius number input
document.getElementById('circle-radius-num').addEventListener('input', (e) => {
  const value = parseInt(e.target.value);
  document.getElementById('circle-radius').value = value;
  updateShape('radius', value);
});

// Color pickers
document.getElementById('circle-fill-color').addEventListener('input', (e) => {
  updateShape('fillColor', e.target.value);
});

// Export button
document.getElementById('export-btn').addEventListener('click', () => {
  openExportModal();
});
```

**Best Practices**:
- Sync slider and number input values
- Debounce rapid updates (for performance)
- Validate inputs before state updates
- Use `input` event for real-time updates

**Checklist**:
- [ ] All input controls wired to state
- [ ] Slider/number input synchronization
- [ ] Color picker updates
- [ ] Export button handler

---

### Phase 6: PNG Export (2 hours)

**Goal**: Export shapes as PNG with custom resolution

```javascript
async function exportToPNG() {
  const { width, height, dpi, filename } = state.exportSettings;

  // Validate settings
  if (width <= 0 || height <= 0 || width > 5000 || height > 5000) {
    alert('Invalid dimensions (1-5000px)');
    return;
  }

  // Create temporary canvas
  const scale = dpi / 72;
  const exportCanvas = document.createElement('canvas');
  exportCanvas.width = width * scale;
  exportCanvas.height = height * scale;

  const ctx = exportCanvas.getContext('2d');
  ctx.scale(scale, scale);

  // Render shape
  ctx.fillStyle = '#ffffff';
  ctx.fillRect(0, 0, width, height);

  const shapeType = state.currentShape;
  const shape = state.shapes[shapeType];

  if (shapeType === 'circle') {
    drawCircleOnContext(ctx, shape, width / 2, height / 2);
  } else {
    drawRectangleOnContext(ctx, shape, width / 2, height / 2);
  }

  // Convert to blob
  const blob = await new Promise(resolve => {
    exportCanvas.toBlob(resolve, 'image/png');
  });

  // Download
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `${filename}.png`;
  a.click();
  URL.revokeObjectURL(url);

  closeExportModal();
}
```

**Checklist**:
- [ ] Export modal with dimension inputs
- [ ] DPI scaling calculation
- [ ] Temporary canvas creation
- [ ] Blob generation
- [ ] File download trigger
- [ ] Memory cleanup (revokeObjectURL)

---

## Testing Checklist

### Manual Testing

**Functionality**:
- [ ] Create circle with default properties
- [ ] Adjust circle radius (slider and number input)
- [ ] Change circle fill color
- [ ] Change circle stroke color and width
- [ ] Adjust circle opacity
- [ ] Switch to rectangle
- [ ] Adjust rectangle dimensions
- [ ] Change rectangle colors
- [ ] Export PNG at 72 DPI
- [ ] Export PNG at 300 DPI
- [ ] Verify exported PNG matches preview

**Edge Cases**:
- [ ] Minimum values (radius: 1, thickness: 0.5)
- [ ] Maximum values (radius: 1000, export: 5000px)
- [ ] Zero opacity (invisible shape)
- [ ] Invalid export dimensions (shows error)

**Performance**:
- [ ] Smooth slider dragging (60fps)
- [ ] Fast export (<2s for 1000x1000px)

**Browser Compatibility**:
- [ ] Chrome 90+
- [ ] Firefox 88+
- [ ] Safari 14+
- [ ] Edge 90+

---

## Common Patterns

### Debouncing Rapid Updates

```javascript
let debounceTimer;

function debouncedUpdate(property, value, delay = 16) {
  clearTimeout(debounceTimer);
  debounceTimer = setTimeout(() => {
    updateShape(property, value);
  }, delay);
}
```

### RequestAnimationFrame Rendering

```javascript
let rafId = null;

function scheduleRender() {
  if (rafId) cancelAnimationFrame(rafId);

  rafId = requestAnimationFrame(() => {
    renderCanvas();
    rafId = null;
  });
}
```

### LocalStorage Persistence

```javascript
function savePreferences() {
  const prefs = {
    lastShapeType: state.currentShape,
    lastExportSettings: state.exportSettings
  };

  localStorage.setItem('shapeGeneratorPrefs', JSON.stringify(prefs));
}

function loadPreferences() {
  const saved = localStorage.getItem('shapeGeneratorPrefs');
  if (saved) {
    const prefs = JSON.parse(saved);
    state.currentShape = prefs.lastShapeType || 'circle';
    state.exportSettings = { ...state.exportSettings, ...prefs.lastExportSettings };
  }
}
```

---

## Troubleshooting

### Canvas not rendering

**Issue**: Blank canvas after updates

**Solutions**:
- Check console for JavaScript errors
- Verify `ctx.getContext('2d')` returns valid context
- Ensure canvas dimensions are set (width/height attributes)
- Check if `renderCanvas()` is being called

### Export not working

**Issue**: PNG download fails or shows blank image

**Solutions**:
- Check if `canvas.toBlob()` is supported (Chrome 50+, Firefox 19+)
- Verify export dimensions are within limits (1-5000px)
- Check console for quota errors (browser memory limits)
- Test with smaller dimensions first

### Colors not updating

**Issue**: Color picker changes don't reflect in canvas

**Solutions**:
- Verify event listener is attached to correct input
- Check if `updateShape()` is being called
- Ensure `renderCanvas()` is triggered after state update
- Inspect state object in console to confirm update

### Performance issues

**Issue**: Laggy slider updates or slow rendering

**Solutions**:
- Add debouncing to rapid input events
- Use `requestAnimationFrame` for render scheduling
- Reduce canvas dimensions for preview (use 600x600 instead of 1920x1080)
- Profile with browser DevTools Performance tab

---

## Next Steps

1. **Implement basic structure** (Phase 1-2): Get HTML and CSS working
2. **Add canvas rendering** (Phase 3-4): Implement state and drawing functions
3. **Wire up interactions** (Phase 5): Connect UI to state updates
4. **Add export** (Phase 6): Implement PNG generation and download
5. **Test thoroughly**: Follow testing checklist
6. **Polish UX**: Add animations, error messages, loading states

---

## Resources

### Documentation
- [Canvas API (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API)
- [Canvas Tutorial (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial)
- [HTML5 Input Types](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)

### Design References
- See `data-model.md` for state structure
- See `canvas-api.md` for rendering contracts
- See `research.md` for technology decisions

### Performance
- [RequestAnimationFrame Guide](https://developer.mozilla.org/en-US/docs/Web/API/window/requestAnimationFrame)
- [Canvas Performance Tips](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial/Optimizing_canvas)

---

## Support

For questions or issues during implementation:
1. Review `spec.md` for requirements
2. Check `research.md` for technical decisions
3. Refer to `data-model.md` for state structure
4. Consult `canvas-api.md` for rendering contracts

**Estimated Implementation Time**: 8-10 hours for MVP

Good luck with implementation!
