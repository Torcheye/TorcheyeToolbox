# Vector Shapes Generator

A modern, interactive web application for creating and customizing simple vector shapes. Built with vanilla HTML, CSS, and JavaScript.

## Features

### Shape Types
- **Circle**: Adjustable radius
- **Rectangle**: Customizable width, height, and corner radius

### Customization Options
- **Fill**: Color picker and opacity control
- **Stroke**: Color, width, and opacity controls
- **Canvas Size**: Adjustable width and height (100-2000px)

### Export
- Download as PNG with high-quality resolution
- Multiple export scales: 1x, 2x, 3x, 4x
- Automatic filename with timestamp

### User Interface
- Clean, modern dark theme design
- Real-time preview
- Intuitive sliders and color pickers
- Responsive layout
- Smooth animations and interactions

## How to Use

1. **Open the Application**
   - Simply open `index.html` in any modern web browser
   - No build process or dependencies required

2. **Choose a Shape**
   - Click on "Circle" or "Rectangle" button to select shape type

3. **Customize Properties**
   - Use sliders to adjust dimensions (radius, width, height, corner radius)
   - Pick fill and stroke colors using color pickers
   - Adjust opacity for both fill and stroke
   - Modify stroke width

4. **Adjust Canvas Size**
   - Set custom canvas dimensions using the number inputs
   - Canvas updates in real-time

5. **Export**
   - Select desired export resolution scale (1x-4x)
   - Click "Download PNG" to save your shape
   - File will be saved with automatic naming: `{shape}-{scale}x-{timestamp}.png`

## Technical Details

- **No Dependencies**: Pure vanilla JavaScript, HTML5, and CSS3
- **Canvas API**: Uses HTML5 Canvas for shape rendering
- **Modern CSS**: CSS Grid, Flexbox, and CSS Variables for theming
- **Responsive**: Works on desktop and tablet devices
- **Browser Support**: All modern browsers (Chrome, Firefox, Safari, Edge)

## File Structure

```
vector-shapes-generator/
├── index.html          # Complete application (HTML, CSS, JS)
└── README.md          # Documentation
```

## Customization

The application uses CSS variables for theming. You can easily customize colors by modifying the `:root` variables in the `<style>` section:

```css
:root {
    --primary: #6366f1;
    --secondary: #8b5cf6;
    --background: #0f172a;
    /* ... more variables */
}
```

## Future Enhancements

Potential features for future versions:
- Additional shapes (triangle, ellipse, polygon, star)
- Multiple shapes on one canvas
- SVG export option
- Shape layering and z-index control
- Gradient fills
- Shadow effects
- Pattern fills
- Copy/paste shapes
- Undo/redo functionality
- Preset templates

## License

Part of TorchEye Games Toolbox
