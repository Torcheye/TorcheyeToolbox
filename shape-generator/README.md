# Vector Shape Generator

A simple, lightweight web application for creating and customizing primitive vector shapes with real-time preview and PNG export capabilities.

## Features

- **Create Shapes**: Choose between circles and rectangles
- **Customize Properties**: Adjust dimensions, fill colors, outline colors, thickness, and opacity
- **Real-time Preview**: See changes instantly on the canvas
- **PNG Export**: Export your shapes with custom dimensions and DPI settings
- **Persistent Preferences**: Your last settings are automatically saved

## Quick Start

### Option 1: Open Directly
Simply open `index.html` in your web browser by double-clicking the file.

### Option 2: Local Server (Recommended)
For the best experience, run a local web server:

**Using Python:**
```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

**Using Node.js:**
```bash
npx http-server -p 8000
```

Then navigate to: `http://localhost:8000/index.html`

## How to Use

### Creating a Shape

1. **Select Shape Type**: Choose Circle or Rectangle from the dropdown
2. **Adjust Properties**:
   - **Circle**: Set radius, colors, outline thickness, and opacity
   - **Rectangle**: Set width, height, colors, outline thickness, and opacity
3. **Preview**: Watch your shape update in real-time on the canvas

### Customizing Colors

- Click the color picker to select fill or stroke colors
- The hex code is displayed next to each color picker
- Adjust opacity using the slider (0-100%)

### Exporting as PNG

1. Click the **"Export to PNG"** button
2. Set your desired export dimensions (1-5000px)
3. Choose a DPI setting:
   - **72 DPI**: Web graphics (default)
   - **150 DPI**: Print quality
   - **300 DPI**: High-resolution print
4. Enter a filename (letters, numbers, hyphens, underscores only)
5. Click **"Export"** to download your PNG file

## Browser Compatibility

This application works in all modern browsers:

- **Chrome** 90+
- **Firefox** 88+
- **Safari** 14+
- **Edge** 90+

**Note**: The application requires HTML5 Canvas support and will display an error message if your browser is not supported.

## Shape Properties

### Circle
- **Radius**: 1 - 1000 pixels
- **Fill Color**: Any hex color
- **Stroke Color**: Any hex color
- **Stroke Width**: 0.5 - 50 pixels
- **Opacity**: 0 - 100%

### Rectangle
- **Width**: 1 - 1000 pixels
- **Height**: 1 - 1000 pixels
- **Fill Color**: Any hex color
- **Stroke Color**: Any hex color
- **Stroke Width**: 0.5 - 50 pixels
- **Opacity**: 0 - 100%

## Export Settings

- **Dimensions**: 1 - 5000 pixels (width and height)
- **DPI**: 1 - 600 (common: 72, 150, 300)
- **Format**: PNG only
- **Background**: White

## Tips and Tricks

- **Synchronized Inputs**: Sliders and number inputs are synchronized - change either one
- **Quick DPI Selection**: Click the preset buttons (72, 150, 300 DPI) for common settings
- **Keyboard Input**: You can type exact values in the number input fields
- **Preferences**: Your last shape type and export settings are automatically saved
- **Zero Stroke**: Set stroke width to 0 for shapes without outlines

## Technical Details

- **Zero Dependencies**: Pure vanilla HTML, CSS, and JavaScript
- **Single File**: Everything in one HTML file for easy portability
- **Client-Side Only**: No server required, all processing happens in your browser
- **Offline Capable**: Works without internet after initial load
- **Performance**: Uses requestAnimationFrame for smooth 60fps rendering

## File Structure

```
shape-generator/
├── index.html          # Complete application (HTML, CSS, JavaScript)
├── README.md           # This file
└── assets/             # Optional assets folder
    └── (empty)
```

## Troubleshooting

### Canvas not displaying
- Ensure JavaScript is enabled in your browser
- Check browser console for errors
- Try refreshing the page

### Export not working
- Verify your export dimensions are within limits (1-5000px)
- Try smaller dimensions if export fails
- Check that your filename contains only valid characters

### Colors not updating
- Make sure you're clicking the color picker itself
- Refresh the page if controls become unresponsive
- Check that opacity is not set to 0%

### Slow performance
- Try smaller shape dimensions (reduce radius/width/height)
- Close other browser tabs to free up memory
- Use a modern browser with hardware acceleration

## Keyboard Shortcuts

- **Tab**: Navigate between controls
- **Arrow Keys**: Adjust slider values when focused
- **Enter**: Confirm export modal (when focused on confirm button)
- **Escape**: Close export modal (when modal is open)

## Known Limitations

- **PNG Only**: Currently only exports PNG format (SVG and JPG not supported)
- **Single Shape**: Can only work with one shape at a time
- **No Undo**: Changes cannot be undone (refresh to reset)
- **Desktop-First**: Mobile experience is functional but not optimized
- **No Shape Library**: Cannot save multiple shapes or create templates

## Future Enhancements

These features are not currently implemented but may be added in future versions:

- Additional shape types (triangle, polygon, ellipse)
- SVG export support
- Multiple shapes on one canvas
- Shape library and templates
- Undo/redo functionality
- Custom gradient fills
- Shape transformations (rotation, skew)
- Mobile-optimized interface

## License

This tool is part of the TorchEye Games Studio Toolbox.

## Support

For bugs or feature requests, please report issues to the TorchEye Games development team.

## Version

**Current Version**: 1.0.0
**Release Date**: 2025-11-04

---

**Made with** by TorchEye Games Studio
