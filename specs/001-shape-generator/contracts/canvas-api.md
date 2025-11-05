# Canvas Rendering API Contract

**Phase**: 1 - Design & Contracts
**Date**: 2025-11-04
**Type**: Internal JavaScript Module Interface

## Overview

This document defines the contract for the Canvas Rendering module, which is responsible for drawing shapes on the HTML5 canvas and exporting them as PNG files. Since this is a client-side only application, this is an internal JavaScript module interface (not a REST/GraphQL API).

---

## CanvasRenderer Module

### Initialization

```javascript
/**
 * Initialize the canvas renderer with a canvas element
 * @param {HTMLCanvasElement} canvas - The canvas DOM element
 * @throws {Error} If canvas is null or not a valid canvas element
 */
function initializeCanvas(canvas) {
  if (!canvas || !(canvas instanceof HTMLCanvasElement)) {
    throw new Error('Invalid canvas element');
  }

  const ctx = canvas.getContext('2d');
  if (!ctx) {
    throw new Error('Canvas 2D context not supported');
  }

  return {
    canvas,
    ctx,
    width: canvas.width,
    height: canvas.height
  };
}
```

**Preconditions**:
- Canvas element must exist in DOM
- Browser must support Canvas 2D context

**Postconditions**:
- Returns canvas context object
- Canvas is ready for drawing operations

---

### Clear Canvas

```javascript
/**
 * Clear the entire canvas to transparent or specified background color
 * @param {CanvasRenderingContext2D} ctx - Canvas 2D context
 * @param {string} [backgroundColor] - Optional background color (hex or rgba)
 */
function clearCanvas(ctx, backgroundColor = null) {
  const canvas = ctx.canvas;

  // Clear to transparent
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Optional background fill
  if (backgroundColor) {
    ctx.fillStyle = backgroundColor;
    ctx.fillRect(0, 0, canvas.width, canvas.height);
  }
}
```

**Preconditions**:
- `ctx` must be valid CanvasRenderingContext2D
- `backgroundColor` (if provided) must be valid CSS color string

**Postconditions**:
- Canvas is cleared to transparent or background color
- Ready for new drawing operations

---

### Draw Circle

```javascript
/**
 * Draw a circle on the canvas
 * @param {CanvasRenderingContext2D} ctx - Canvas 2D context
 * @param {CircleShape} shape - Circle configuration object
 * @param {Object} [options] - Optional rendering options
 * @param {number} [options.centerX] - X coordinate of circle center (default: canvas.width / 2)
 * @param {number} [options.centerY] - Y coordinate of circle center (default: canvas.height / 2)
 */
function drawCircle(ctx, shape, options = {}) {
  const {
    centerX = ctx.canvas.width / 2,
    centerY = ctx.canvas.height / 2
  } = options;

  const { radius, fillColor, strokeColor, strokeWidth, opacity } = shape;

  // Validate shape data
  if (radius <= 0) {
    throw new Error('Circle radius must be positive');
  }

  // Save context state
  ctx.save();

  // Apply opacity
  ctx.globalAlpha = opacity / 100;

  // Draw filled circle
  ctx.fillStyle = fillColor;
  ctx.beginPath();
  ctx.arc(centerX, centerY, radius, 0, Math.PI * 2);
  ctx.fill();

  // Draw stroke (if strokeWidth > 0)
  if (strokeWidth > 0) {
    ctx.strokeStyle = strokeColor;
    ctx.lineWidth = strokeWidth;
    ctx.stroke();
  }

  // Restore context state
  ctx.restore();
}
```

**Preconditions**:
- `ctx` must be valid CanvasRenderingContext2D
- `shape` must conform to CircleShape interface
- `radius` must be positive number
- Colors must be valid CSS color strings

**Postconditions**:
- Circle is drawn at specified position with given properties
- Canvas context state is restored (no side effects)

**Example Usage**:
```javascript
const circle = {
  radius: 100,
  fillColor: '#3498db',
  strokeColor: '#2c3e50',
  strokeWidth: 3,
  opacity: 80
};

drawCircle(ctx, circle, { centerX: 200, centerY: 200 });
```

---

### Draw Rectangle

```javascript
/**
 * Draw a rectangle on the canvas
 * @param {CanvasRenderingContext2D} ctx - Canvas 2D context
 * @param {RectangleShape} shape - Rectangle configuration object
 * @param {Object} [options] - Optional rendering options
 * @param {number} [options.centerX] - X coordinate of rectangle center (default: canvas.width / 2)
 * @param {number} [options.centerY] - Y coordinate of rectangle center (default: canvas.height / 2)
 */
function drawRectangle(ctx, shape, options = {}) {
  const {
    centerX = ctx.canvas.width / 2,
    centerY = ctx.canvas.height / 2
  } = options;

  const { width, height, fillColor, strokeColor, strokeWidth, opacity } = shape;

  // Validate shape data
  if (width <= 0 || height <= 0) {
    throw new Error('Rectangle dimensions must be positive');
  }

  // Calculate top-left corner (centered)
  const x = centerX - (width / 2);
  const y = centerY - (height / 2);

  // Save context state
  ctx.save();

  // Apply opacity
  ctx.globalAlpha = opacity / 100;

  // Draw filled rectangle
  ctx.fillStyle = fillColor;
  ctx.fillRect(x, y, width, height);

  // Draw stroke (if strokeWidth > 0)
  if (strokeWidth > 0) {
    ctx.strokeStyle = strokeColor;
    ctx.lineWidth = strokeWidth;
    ctx.strokeRect(x, y, width, height);
  }

  // Restore context state
  ctx.restore();
}
```

**Preconditions**:
- `ctx` must be valid CanvasRenderingContext2D
- `shape` must conform to RectangleShape interface
- `width` and `height` must be positive numbers
- Colors must be valid CSS color strings

**Postconditions**:
- Rectangle is drawn at specified position with given properties
- Canvas context state is restored (no side effects)

**Example Usage**:
```javascript
const rectangle = {
  width: 200,
  height: 150,
  fillColor: '#e74c3c',
  strokeColor: '#c0392b',
  strokeWidth: 2,
  opacity: 100
};

drawRectangle(ctx, rectangle, { centerX: 300, centerY: 200 });
```

---

### Render Current Shape

```javascript
/**
 * Render the currently selected shape from application state
 * @param {CanvasRenderingContext2D} ctx - Canvas 2D context
 * @param {AppState} state - Application state object
 */
function renderCurrentShape(ctx, state) {
  // Clear canvas
  clearCanvas(ctx, '#ffffff'); // White background

  // Get current shape
  const shapeType = state.currentShape;
  const shape = state.shapes[shapeType];

  // Render based on type
  if (shapeType === 'circle') {
    drawCircle(ctx, shape);
  } else if (shapeType === 'rectangle') {
    drawRectangle(ctx, shape);
  } else {
    throw new Error(`Unknown shape type: ${shapeType}`);
  }
}
```

**Preconditions**:
- `ctx` must be valid CanvasRenderingContext2D
- `state` must contain valid AppState structure
- `state.currentShape` must be a valid shape type
- `state.shapes[currentShape]` must exist

**Postconditions**:
- Canvas is cleared and redrawn with current shape
- Preview reflects current application state

---

## ExportManager Module

### Export to PNG

```javascript
/**
 * Export the current shape as a PNG file
 * @param {AppState} state - Application state
 * @param {ExportSettings} exportSettings - Export configuration
 * @returns {Promise<Blob>} PNG blob
 */
async function exportToPNG(state, exportSettings) {
  const { width, height, dpi } = exportSettings;

  // Validate export settings
  if (width <= 0 || height <= 0 || width > 5000 || height > 5000) {
    throw new Error('Invalid export dimensions (must be 1-5000px)');
  }

  // Calculate DPI scaling
  const scale = dpi / 72;

  // Create temporary canvas
  const exportCanvas = document.createElement('canvas');
  exportCanvas.width = width * scale;
  exportCanvas.height = height * scale;

  const ctx = exportCanvas.getContext('2d');

  // Scale context for DPI
  ctx.scale(scale, scale);

  // Set virtual dimensions
  const virtualWidth = width;
  const virtualHeight = height;

  // Render shape to export canvas
  clearCanvas(ctx, '#ffffff'); // White background for export

  const shapeType = state.currentShape;
  const shape = state.shapes[shapeType];

  if (shapeType === 'circle') {
    drawCircle(ctx, shape, {
      centerX: virtualWidth / 2,
      centerY: virtualHeight / 2
    });
  } else if (shapeType === 'rectangle') {
    drawRectangle(ctx, shape, {
      centerX: virtualWidth / 2,
      centerY: virtualHeight / 2
    });
  }

  // Convert to blob
  return new Promise((resolve, reject) => {
    exportCanvas.toBlob(blob => {
      if (blob) {
        resolve(blob);
      } else {
        reject(new Error('Failed to generate PNG blob'));
      }
    }, 'image/png');
  });
}
```

**Preconditions**:
- `state` must contain valid shape data
- `exportSettings` must have valid width, height, and dpi
- Browser must support `canvas.toBlob()`

**Postconditions**:
- Returns a Promise that resolves to PNG Blob
- Original canvas is not modified
- Temporary canvas is eligible for garbage collection

**Example Usage**:
```javascript
const exportSettings = {
  width: 1920,
  height: 1080,
  dpi: 300,
  filename: 'my-shape'
};

const blob = await exportToPNG(state, exportSettings);
downloadBlob(blob, `${exportSettings.filename}.png`);
```

---

### Download Blob

```javascript
/**
 * Trigger browser download of a blob
 * @param {Blob} blob - File blob to download
 * @param {string} filename - Download filename (with extension)
 */
function downloadBlob(blob, filename) {
  // Create object URL
  const url = URL.createObjectURL(blob);

  // Create temporary download link
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  a.style.display = 'none';

  // Trigger download
  document.body.appendChild(a);
  a.click();

  // Cleanup
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}
```

**Preconditions**:
- `blob` must be valid Blob object
- `filename` must be non-empty string

**Postconditions**:
- Browser download is triggered
- Object URL is revoked (no memory leak)
- Temporary DOM elements are removed

---

## Performance Contracts

### Real-time Rendering

**Target**: <16ms per frame (60fps)

**Optimizations**:
1. **RequestAnimationFrame**: Queue updates to sync with browser refresh
2. **Debouncing**: Batch rapid updates (e.g., slider drag) to 16ms intervals
3. **Minimize State Changes**: Only redraw when state actually changes

```javascript
let rafId = null;

function scheduleRender(ctx, state) {
  // Cancel pending render
  if (rafId) {
    cancelAnimationFrame(rafId);
  }

  // Schedule new render
  rafId = requestAnimationFrame(() => {
    renderCurrentShape(ctx, state);
    rafId = null;
  });
}
```

### Export Performance

**Target**: <2s for 1000x1000px export

**Constraints**:
- Maximum canvas size: 5000x5000px (per FR-016)
- Memory limit: ~100MB per temporary canvas
- Typical export time: 200-500ms for web sizes, 1-2s for print sizes

---

## Error Handling

### Error Types

```javascript
// Invalid input errors
class ValidationError extends Error {
  constructor(field, value, constraint) {
    super(`Invalid ${field}: ${value} (${constraint})`);
    this.name = 'ValidationError';
    this.field = field;
    this.value = value;
  }
}

// Canvas operation errors
class CanvasError extends Error {
  constructor(operation, reason) {
    super(`Canvas operation failed: ${operation} (${reason})`);
    this.name = 'CanvasError';
    this.operation = operation;
  }
}

// Export errors
class ExportError extends Error {
  constructor(reason) {
    super(`Export failed: ${reason}`);
    this.name = 'ExportError';
  }
}
```

### Error Handling Strategy

```javascript
function safeRender(ctx, state) {
  try {
    renderCurrentShape(ctx, state);
  } catch (error) {
    console.error('Render error:', error);
    showUserError('Failed to render shape. Please check your settings.');

    // Fallback: Clear canvas
    clearCanvas(ctx);
  }
}

async function safeExport(state, exportSettings) {
  try {
    const blob = await exportToPNG(state, exportSettings);
    return blob;
  } catch (error) {
    console.error('Export error:', error);

    if (error instanceof ValidationError) {
      showUserError(`Invalid export setting: ${error.field}`);
    } else {
      showUserError('Export failed. Please try different dimensions.');
    }

    throw error; // Re-throw for caller to handle
  }
}
```

---

## Testing Contracts

### Unit Test Coverage

**Render Functions**:
- ✅ `drawCircle()` renders at correct position
- ✅ `drawCircle()` applies correct colors and opacity
- ✅ `drawRectangle()` renders at correct position
- ✅ `drawRectangle()` applies correct dimensions
- ✅ `clearCanvas()` fully clears canvas
- ✅ `renderCurrentShape()` delegates to correct draw function

**Export Functions**:
- ✅ `exportToPNG()` generates blob with correct dimensions
- ✅ `exportToPNG()` applies DPI scaling correctly
- ✅ `exportToPNG()` handles maximum dimension limits
- ✅ `downloadBlob()` triggers browser download
- ✅ `downloadBlob()` cleans up object URLs

**Error Handling**:
- ✅ Invalid shape data throws ValidationError
- ✅ Unsupported canvas throws CanvasError
- ✅ Export failures throw ExportError

---

## Browser Compatibility

### Required APIs

| API | Chrome | Firefox | Safari | Edge |
|-----|--------|---------|--------|------|
| Canvas 2D Context | ✅ All | ✅ All | ✅ All | ✅ All |
| `canvas.toBlob()` | ✅ 50+ | ✅ 19+ | ✅ 11+ | ✅ 79+ |
| `URL.createObjectURL()` | ✅ All | ✅ All | ✅ All | ✅ All |
| `requestAnimationFrame()` | ✅ All | ✅ All | ✅ All | ✅ All |

**Fallback Strategy**:
- If `toBlob()` not supported: Use `canvas.toDataURL()` and convert to blob manually
- If Canvas not supported: Show error message (no graceful degradation possible)

---

## Summary

The Canvas Rendering API provides a clean, functional interface for drawing shapes and exporting PNG files. All functions follow consistent patterns:
- **Validation first**: Check inputs before operations
- **State preservation**: Save/restore canvas context
- **Error handling**: Throw descriptive errors for invalid inputs
- **Performance**: Use RAF for smooth rendering, optimize export

This contract ensures consistent behavior across the application and provides a solid foundation for testing and future enhancements.
