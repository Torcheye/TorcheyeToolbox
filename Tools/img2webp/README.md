# Image to WebP Converter

A lightweight desktop GUI application for batch converting image files (PNG/JPG/GIF) to WebP format. Perfect for game developers and web designers looking to optimize their image assets.

## Features

- **Multiple Format Support**: Convert PNG, JPG, JPEG, and GIF files to WebP
- **Animated WebP Support**: Preserve GIF animations as animated WebP files
- **Drag & Drop**: Simply drag and drop files into the application window
- **Modern Dark Theme**: Beautiful, eye-friendly dark interface with modern styling
- **Batch Conversion**: Convert multiple image files at once
- **Quality Control**: Adjustable WebP quality slider (1-100)
- **Flexible Output**: Save converted files in the same directory or choose a custom output folder
- **Enhanced Progress Bar**: Clear visual progress indicator with status updates
- **File Size Tracking**: See before/after file sizes and percentage reduction
- **Error Handling**: Gracefully handles invalid files and conversion errors
- **Transparency Support**: Automatically handles images with alpha channels
- **Intuitive Interface**: Clean, modern single-window design with improved button visibility

## System Requirements

- **Python**: 3.8 or higher
- **Operating System**: Windows, macOS, or Linux
- **Dependencies**:
  - Pillow (PIL Fork) 10.0.0 or higher
  - tkinterdnd2 0.3.0 or higher (for drag & drop support)

## Installation

1. **Clone or download** this repository to your local machine

2. **Navigate** to the project directory:
   ```bash
   cd "png2webp Converter"
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or install packages individually:
   ```bash
   pip install Pillow>=10.0.0 tkinterdnd2>=0.3.0
   ```

   **Note**: The application will work without tkinterdnd2, but drag & drop functionality will be disabled.

## Usage

### Running the Application

Launch the converter by running:
```bash
python converter.py
```

### Converting Files

1. **Select Image Files**:
   - **Option 1**: Click "Browse Image Files..." button and select PNG, JPG, JPEG, or GIF files
   - **Option 2**: Drag and drop image files directly into the file list area
   - Selected files will appear in the list box

2. **Choose Output Location** (Optional):
   - By default, "Save in same folder as source files" is checked
   - Uncheck this option to specify a custom output folder
   - Click "Choose Output Folder..." to select where converted files will be saved

3. **Animation Settings** (Optional):
   - Check "Preserve GIF animation" to convert animated GIFs to animated WebP files
   - If unchecked, only the first frame of animated GIFs will be converted
   - This setting only affects animated GIF files

4. **Adjust Quality**:
   - Use the quality slider to set WebP quality (1-100)
   - Default is 80, which provides a good balance between quality and file size
   - Higher values = better quality but larger file sizes
   - Lower values = smaller file sizes but reduced quality

5. **Convert**:
   - Click the "⚡ Convert to WebP" button
   - Watch the progress bar and log for real-time updates
   - A summary dialog will appear when conversion is complete

### Clearing Selection

Click "Clear Selection" to:
- Remove all selected files
- Reset the progress bar
- Clear the conversion log

## Understanding WebP Quality Settings

| Quality Range | Best For | File Size | Quality |
|--------------|----------|-----------|---------|
| 1-30 | Thumbnails, backgrounds | Smallest | Low |
| 40-60 | Web graphics, icons | Small | Medium |
| 70-85 | General purpose images | Moderate | Good |
| 86-100 | High-quality assets, photos | Large | Excellent |

**Recommended**: Start with quality 80 and adjust based on your needs.

## Interface

The application features a modern dark theme designed for comfortable extended use:
- **Dark Background**: Easy on the eyes during long conversion sessions
- **Accent Colors**: Teal/cyan highlights for better visual hierarchy
- **Modern Fonts**: Segoe UI for interface elements, Consolas for file listings
- **Clear Contrast**: High-contrast text for excellent readability
- **Intuitive Layout**: Well-organized sections with clear visual separation

## How It Works

### Format Support

- **PNG**: Full support including transparency handling
- **JPG/JPEG**: Direct conversion to WebP format
- **GIF**: Full support including animated GIF to animated WebP conversion
  - With "Preserve GIF animation" enabled: Creates animated WebP files
  - With "Preserve GIF animation" disabled: Extracts first frame only

### Transparency Handling

Images with transparency (RGBA mode) are automatically converted:
- Alpha channel is removed
- Transparent areas are replaced with a white background
- Image is saved in RGB mode for WebP compatibility

For lossless transparency preservation, you may need to modify the code to use WebP's lossless mode.

### File Naming

Converted files maintain the original filename with the `.webp` extension:
- `logo.png` → `logo.webp`
- `photo.jpg` → `photo.webp`
- `animation.gif` → `animation.webp`
- `background-image.png` → `background-image.webp`

### Error Recovery

If a file fails to convert:
- The error is logged in the conversion log
- Processing continues with remaining files
- Final summary shows number of successful and failed conversions

## Troubleshooting

### "Error: Pillow library not found!"
**Solution**: Install Pillow using `pip install Pillow>=10.0.0`

### "Permission denied" errors
**Solution**: Ensure you have write permissions for the output directory

### Files not appearing in file dialog
**Solution**: Make sure you're selecting files with `.png`, `.jpg`, `.jpeg`, or `.gif` extensions, or select "All files" in the dialog

### Drag and drop not working
**Solution**: Install tkinterdnd2 using `pip install tkinterdnd2>=0.3.0`. The application will still work without it, but you'll need to use the Browse button instead.

### Application window is too small/large
**Solution**: The window is fixed at 650x550 pixels. To change this, modify the `self.root.geometry("650x550")` line in `converter.py`

## Technical Details

- **Language**: Python 3.8+
- **GUI Framework**: Tkinter (included with Python)
- **Drag & Drop**: tkinterdnd2 (optional but recommended)
- **Image Processing**: Pillow (PIL Fork)
- **Supported Formats**: PNG, JPG, JPEG, GIF → WebP
- **Cross-platform**: Works on Windows, macOS, and Linux

### Project Structure

```
png2webp Converter/
├── converter.py          # Main application file
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── IMPLEMENTATION_PLAN.md # Development specifications
```

## Use Cases

Perfect for:
- **Game Development**: Optimize game assets and UI sprites
- **Web Development**: Reduce website image sizes for faster loading
- **Mobile Apps**: Compress images to save bandwidth and storage
- **Digital Art**: Create web-friendly versions of artwork
- **Photography**: Generate compressed versions for online galleries

## Performance Tips

- **Batch Processing**: Convert multiple files at once for efficiency
- **Quality Presets**: Use quality 80 for general purpose, 90+ for important assets, 60-70 for less critical images
- **Test First**: Try different quality settings on a sample file to find your ideal balance
- **Large Files**: The application handles large PNG files, but conversion may take longer

## Future Enhancements

Potential features for future versions:
- Support for additional formats (BMP, TIFF, etc.)
- Lossless WebP conversion option
- Before/after preview comparison
- Preset quality buttons (Low/Medium/High)
- Recursive folder processing
- Batch rename patterns
- Configuration file for default settings
- Light/Dark theme toggle
- Custom color themes

## License

MIT License

Copyright (c) 2025 TorchEye Games Studio

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Support

For issues, questions, or contributions, please visit the [TorchEye Games Toolbox](https://github.com/TorcheyeGames/TorcheyeUtility) repository.

## Credits

Part of the **TorchEye Games Studio Toolbox** - A comprehensive collection of tools and utilities for game development.

Built with:
- [Python](https://www.python.org/)
- [Pillow](https://python-pillow.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
