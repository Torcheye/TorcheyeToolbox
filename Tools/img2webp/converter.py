"""
PNG to WebP Converter
A lightweight desktop GUI application for batch converting image files (PNG/JPG/GIF) to WebP format.
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.scrolledtext import ScrolledText
from pathlib import Path
from datetime import datetime
import time

try:
    from PIL import Image
except ImportError:
    print("Error: Pillow library not found!")
    print("Please install it using: pip install -r requirements.txt")
    exit(1)

try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
    DND_AVAILABLE = True
except ImportError:
    DND_AVAILABLE = False
    print("Note: tkinterdnd2 not found. Drag and drop will be disabled.")
    print("To enable drag and drop, install: pip install tkinterdnd2")


class WebPConverter:
    """Main application class for image to WebP conversion"""

    def __init__(self, root):
        """Initialize the GUI and all components"""
        self.root = root
        self.root.title("Image to WebP Converter")
        self.root.geometry("650x550")
        self.root.resizable(False, False)

        # Instance variables
        self.selected_files = []
        self.output_folder = ""
        self.quality_value = tk.IntVar(value=80)
        self.same_as_source = tk.BooleanVar(value=True)
        self.preserve_animation = tk.BooleanVar(value=True)

        # Dark theme colors
        self.colors = {
            'bg': '#1e1e1e',
            'fg': '#e0e0e0',
            'input_bg': '#2d2d2d',
            'input_fg': '#ffffff',
            'button_bg': '#0d7377',
            'button_hover': '#14a3a8',
            'accent': '#32e0c4',
            'secondary': '#323232',
            'border': '#3d3d3d',
            'success': '#4CAF50',
            'error': '#f44336',
            'warning': '#ff9800'
        }

        # Create GUI
        self._create_gui()

        # Setup drag and drop if available
        if DND_AVAILABLE:
            self._setup_drag_and_drop()

    def _create_gui(self):
        """Create all GUI components"""
        # Apply dark theme to root
        self.root.configure(bg=self.colors['bg'])

        # Configure ttk styles
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TProgressbar',
                       background=self.colors['accent'],
                       troughcolor=self.colors['secondary'],
                       bordercolor=self.colors['border'],
                       lightcolor=self.colors['accent'],
                       darkcolor=self.colors['accent'])

        # Main container with padding
        main_frame = tk.Frame(self.root, padx=10, pady=10, bg=self.colors['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 1. File Selection Section
        file_section = tk.LabelFrame(main_frame, text="File Selection", padx=10, pady=5,
                                     bg=self.colors['bg'], fg=self.colors['accent'],
                                     font=('Segoe UI', 10, 'bold'))
        file_section.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        label_text = "Selected Image Files (PNG/JPG/GIF):"
        if DND_AVAILABLE:
            label_text += " - Drag & Drop Supported!"
        tk.Label(file_section, text=label_text, font=('Segoe UI', 9),
                bg=self.colors['bg'], fg=self.colors['fg']).pack(anchor=tk.W)

        # Listbox with scrollbar
        listbox_frame = tk.Frame(file_section, relief=tk.SUNKEN, borderwidth=1,
                                bg=self.colors['border'])
        listbox_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        scrollbar = tk.Scrollbar(listbox_frame, bg=self.colors['secondary'])
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.file_listbox = tk.Listbox(listbox_frame, height=6, yscrollcommand=scrollbar.set,
                                       bg=self.colors['input_bg'], fg=self.colors['input_fg'],
                                       selectbackground=self.colors['button_bg'],
                                       selectforeground=self.colors['input_fg'],
                                       font=('Consolas', 9), borderwidth=0,
                                       highlightthickness=0)
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.file_listbox.yview)

        # Buttons frame
        button_frame = tk.Frame(file_section, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, pady=5)

        browse_btn = tk.Button(button_frame, text="Browse Image Files...", command=self.browse_files,
                              font=('Segoe UI', 9), bg=self.colors['button_bg'], fg=self.colors['input_fg'],
                              activebackground=self.colors['button_hover'], activeforeground=self.colors['input_fg'],
                              borderwidth=0, padx=15, pady=5, cursor='hand2')
        browse_btn.pack(side=tk.LEFT, padx=(0, 5))

        clear_btn = tk.Button(button_frame, text="Clear Selection", command=self.clear_selection,
                             font=('Segoe UI', 9), bg=self.colors['secondary'], fg=self.colors['fg'],
                             activebackground=self.colors['border'], activeforeground=self.colors['input_fg'],
                             borderwidth=0, padx=15, pady=5, cursor='hand2')
        clear_btn.pack(side=tk.LEFT)

        # 2. Output Settings Section
        output_section = tk.LabelFrame(main_frame, text="Output Settings", padx=10, pady=5,
                                      bg=self.colors['bg'], fg=self.colors['accent'],
                                      font=('Segoe UI', 10, 'bold'))
        output_section.pack(fill=tk.X, pady=(0, 10))

        tk.Checkbutton(output_section, text="Save in same folder as source files",
                      variable=self.same_as_source, command=self._toggle_output_folder,
                      bg=self.colors['bg'], fg=self.colors['fg'],
                      selectcolor=self.colors['input_bg'], activebackground=self.colors['bg'],
                      activeforeground=self.colors['accent'], font=('Segoe UI', 9)).pack(anchor=tk.W)

        tk.Checkbutton(output_section, text="Preserve GIF animation (create animated WebP)",
                      variable=self.preserve_animation,
                      bg=self.colors['bg'], fg=self.colors['fg'],
                      selectcolor=self.colors['input_bg'], activebackground=self.colors['bg'],
                      activeforeground=self.colors['accent'], font=('Segoe UI', 9)).pack(anchor=tk.W, pady=(5, 0))

        output_frame = tk.Frame(output_section, bg=self.colors['bg'])
        output_frame.pack(fill=tk.X, pady=5)

        tk.Label(output_frame, text="Output Folder:", bg=self.colors['bg'],
                fg=self.colors['fg'], font=('Segoe UI', 9)).pack(anchor=tk.W)

        output_path_frame = tk.Frame(output_frame, bg=self.colors['bg'])
        output_path_frame.pack(fill=tk.X)

        self.output_entry = tk.Entry(output_path_frame, state='readonly',
                                     bg=self.colors['input_bg'], fg=self.colors['input_fg'],
                                     readonlybackground=self.colors['input_bg'],
                                     font=('Consolas', 9), borderwidth=1,
                                     relief=tk.SOLID, insertbackground=self.colors['accent'])
        self.output_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        self.output_button = tk.Button(output_path_frame, text="Choose Output Folder...",
                                       command=self.choose_output_folder, state='disabled',
                                       font=('Segoe UI', 9), bg=self.colors['button_bg'],
                                       fg=self.colors['input_fg'], activebackground=self.colors['button_hover'],
                                       activeforeground=self.colors['input_fg'],
                                       disabledforeground='#666666',
                                       borderwidth=0, padx=15, pady=5, cursor='hand2')
        self.output_button.pack(side=tk.LEFT)

        # 3. Quality Settings Section
        quality_section = tk.LabelFrame(main_frame, text="Quality Settings", padx=10, pady=5,
                                       bg=self.colors['bg'], fg=self.colors['accent'],
                                       font=('Segoe UI', 10, 'bold'))
        quality_section.pack(fill=tk.X, pady=(0, 10))

        self.quality_label = tk.Label(quality_section, text="WebP Quality: 80",
                                      bg=self.colors['bg'], fg=self.colors['fg'],
                                      font=('Segoe UI', 9))
        self.quality_label.pack(anchor=tk.W)

        self.quality_slider = tk.Scale(quality_section, from_=1, to=100, orient=tk.HORIZONTAL,
                                      variable=self.quality_value, command=self.update_quality_label,
                                      bg=self.colors['bg'], fg=self.colors['fg'],
                                      troughcolor=self.colors['secondary'],
                                      activebackground=self.colors['accent'],
                                      highlightthickness=0, borderwidth=0,
                                      font=('Segoe UI', 8))
        self.quality_slider.pack(fill=tk.X, pady=5)

        tk.Label(quality_section, text="(Higher = better quality, larger file size)",
                font=('Segoe UI', 8), fg='#999',
                bg=self.colors['bg']).pack(anchor=tk.W)

        # 4. Action Section
        action_section = tk.Frame(main_frame, bg=self.colors['bg'])
        action_section.pack(fill=tk.X, pady=(0, 10))

        self.convert_button = tk.Button(action_section, text="⚡ Convert to WebP",
                                        command=self.convert_files, bg=self.colors['success'],
                                        fg='white', font=('Segoe UI', 14, 'bold'), height=2, pady=10,
                                        borderwidth=0, activebackground='#45a049',
                                        activeforeground='white', cursor='hand2')
        self.convert_button.pack(fill=tk.X, pady=(0, 10), ipady=5)

        # Progress section
        progress_frame = tk.Frame(action_section, bg=self.colors['bg'])
        progress_frame.pack(fill=tk.X, pady=(0, 5))

        tk.Label(progress_frame, text="Progress:", font=('Segoe UI', 9),
                bg=self.colors['bg'], fg=self.colors['fg']).pack(anchor=tk.W)
        self.progress_bar = ttk.Progressbar(progress_frame, mode='determinate', length=300)
        self.progress_bar.pack(fill=tk.X, pady=(2, 0))

        self.status_label = tk.Label(action_section, text="Ready", anchor=tk.W,
                                     font=('Segoe UI', 9), fg='#999',
                                     bg=self.colors['bg'])
        self.status_label.pack(fill=tk.X)

        # 5. Log/Results Section
        log_section = tk.LabelFrame(main_frame, text="Conversion Log", padx=5, pady=5,
                                   bg=self.colors['bg'], fg=self.colors['accent'],
                                   font=('Segoe UI', 10, 'bold'))
        log_section.pack(fill=tk.BOTH, expand=True)

        self.log_text = ScrolledText(log_section, height=8, state='disabled', wrap=tk.WORD,
                                     bg=self.colors['input_bg'], fg=self.colors['input_fg'],
                                     font=('Consolas', 9), borderwidth=0,
                                     insertbackground=self.colors['accent'])
        self.log_text.pack(fill=tk.BOTH, expand=True)

    def _toggle_output_folder(self):
        """Enable/disable output folder selection based on checkbox"""
        if self.same_as_source.get():
            self.output_button.config(state='disabled')
            self.output_entry.config(state='normal')
            self.output_entry.delete(0, tk.END)
            self.output_entry.config(state='readonly')
            self.output_folder = ""
        else:
            self.output_button.config(state='normal')

    def _setup_drag_and_drop(self):
        """Setup drag and drop functionality"""
        self.file_listbox.drop_target_register(DND_FILES)
        self.file_listbox.dnd_bind('<<Drop>>', self._on_drop)

    def _on_drop(self, event):
        """Handle dropped files"""
        # Parse dropped file paths
        files = self.root.tk.splitlist(event.data)

        # Filter for supported image formats
        supported_formats = ('.png', '.jpg', '.jpeg', '.gif')
        valid_files = [f for f in files if Path(f).suffix.lower() in supported_formats]

        if valid_files:
            # Add to existing selection
            for file in valid_files:
                if file not in self.selected_files:
                    self.selected_files.append(file)

            # Update listbox
            self.file_listbox.delete(0, tk.END)
            for file in self.selected_files:
                self.file_listbox.insert(tk.END, Path(file).name)

            self.log_message(f"Added {len(valid_files)} file(s) via drag & drop")
        else:
            self.log_message("No supported image files found in drop")

    def browse_files(self):
        """Open file dialog to select image files"""
        files = filedialog.askopenfilenames(
            title="Select Image Files",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.gif"),
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg *.jpeg"),
                ("GIF files", "*.gif"),
                ("All files", "*.*")
            ]
        )

        if files:
            self.selected_files = list(files)
            self.file_listbox.delete(0, tk.END)
            for file in self.selected_files:
                self.file_listbox.insert(tk.END, Path(file).name)
            self.log_message(f"Selected {len(self.selected_files)} file(s)")

    def clear_selection(self):
        """Clear file selection and reset UI"""
        self.selected_files = []
        self.file_listbox.delete(0, tk.END)
        self.progress_bar['value'] = 0
        self.status_label.config(text="Ready")
        self.log_text.config(state='normal')
        self.log_text.delete(1.0, tk.END)
        self.log_text.config(state='disabled')

    def choose_output_folder(self):
        """Open directory dialog to select output folder"""
        folder = filedialog.askdirectory(title="Select Output Folder")
        if folder:
            self.output_folder = folder
            self.output_entry.config(state='normal')
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, folder)
            self.output_entry.config(state='readonly')
            self.log_message(f"Output folder set to: {folder}")

    def update_quality_label(self, value):
        """Update quality label when slider moves"""
        self.quality_label.config(text=f"WebP Quality: {int(float(value))}")

    def convert_files(self):
        """Main conversion method - processes all selected files"""
        if not self.selected_files:
            messagebox.showwarning("No Files Selected",
                                  "Please select PNG files to convert.")
            return

        # Validate output folder if not using same as source
        if not self.same_as_source.get() and not self.output_folder:
            messagebox.showwarning("No Output Folder",
                                  "Please select an output folder or check 'Save in same folder as source files'.")
            return

        # Disable convert button during processing
        self.convert_button.config(state='disabled')
        self.status_label.config(text="Converting...")

        # Reset progress
        self.progress_bar['value'] = 0
        self.progress_bar['maximum'] = len(self.selected_files)

        # Conversion tracking
        total_files = len(self.selected_files)
        successful = 0
        failed = 0
        start_time = time.time()

        quality = self.quality_value.get()

        self.log_message("=" * 50)
        self.log_message(f"Starting batch conversion of {total_files} file(s)")
        self.log_message(f"Quality setting: {quality}")
        self.log_message("=" * 50)

        # Get preserve animation setting
        preserve_animation = self.preserve_animation.get()

        # Process each file
        for i, input_path in enumerate(self.selected_files, 1):
            input_path_obj = Path(input_path)

            # Determine output path
            if self.same_as_source.get():
                output_path = input_path_obj.parent / f"{input_path_obj.stem}.webp"
            else:
                output_path = Path(self.output_folder) / f"{input_path_obj.stem}.webp"

            self.status_label.config(text=f"Converting {i}/{total_files}: {input_path_obj.name}")
            self.root.update_idletasks()

            # Convert the file
            success, message = self.convert_single_file(str(input_path), str(output_path), quality, preserve_animation)

            if success:
                successful += 1
            else:
                failed += 1
                self.log_message(f"ERROR: {message}")

            # Update progress
            self.progress_bar['value'] = i
            self.root.update_idletasks()

        # Calculate elapsed time
        elapsed_time = time.time() - start_time

        # Show summary
        self.log_message("=" * 50)
        self.log_message(f"Conversion completed in {elapsed_time:.2f} seconds")
        self.log_message(f"Successful: {successful}/{total_files}")
        if failed > 0:
            self.log_message(f"Failed: {failed}/{total_files}")
        self.log_message("=" * 50)

        self.status_label.config(text=f"Done! {successful} of {total_files} files converted")
        self.convert_button.config(state='normal')

        # Show completion message
        messagebox.showinfo("Conversion Complete",
                           f"Successfully converted {successful} of {total_files} files in {elapsed_time:.2f} seconds.")

    def convert_single_file(self, input_path, output_path, quality, preserve_animation=False):
        """Convert a single image file (PNG/JPG/GIF) to WebP

        Args:
            input_path: Path to input image file
            output_path: Path to output WebP file
            quality: WebP quality (1-100)
            preserve_animation: Whether to preserve GIF animation (default: False)

        Returns:
            Tuple of (success: bool, message: str)
        """
        try:
            input_path_obj = Path(input_path)
            output_path_obj = Path(output_path)

            # Get original file size
            original_size = input_path_obj.stat().st_size

            # Open and convert the image
            with Image.open(input_path) as img:
                # Check if this is an animated GIF
                is_animated = hasattr(img, 'is_animated') and img.is_animated

                if is_animated and preserve_animation:
                    # Save animated WebP
                    self.log_message(f"  Note: Converting animated GIF with {getattr(img, 'n_frames', 1)} frames")

                    # Extract all frames
                    frames = []
                    durations = []

                    for frame_idx in range(getattr(img, 'n_frames', 1)):
                        img.seek(frame_idx)

                        # Convert frame to RGBA then RGB
                        frame = img.copy()
                        if frame.mode == 'P':
                            frame = frame.convert('RGBA')

                        if frame.mode in ('RGBA', 'LA'):
                            # Create white background for transparency
                            background = Image.new('RGB', frame.size, (255, 255, 255))
                            background.paste(frame, mask=frame.split()[-1])
                            frame = background
                        elif frame.mode != 'RGB':
                            frame = frame.convert('RGB')

                        frames.append(frame)
                        durations.append(img.info.get('duration', 100))

                    # Save as animated WebP
                    frames[0].save(
                        output_path,
                        'WEBP',
                        save_all=True,
                        append_images=frames[1:],
                        duration=durations,
                        loop=0,
                        quality=quality
                    )

                elif is_animated and not preserve_animation:
                    # Save only first frame
                    img.seek(0)
                    self.log_message(f"  Note: Animated GIF detected, using first frame only")

                    # Convert to RGB mode if necessary
                    if img.mode in ('RGBA', 'LA', 'P'):
                        background = Image.new('RGB', img.size, (255, 255, 255))
                        if img.mode == 'P':
                            img = img.convert('RGBA')
                        if img.mode in ('RGBA', 'LA'):
                            background.paste(img, mask=img.split()[-1])
                        else:
                            background.paste(img)
                        img = background
                    elif img.mode != 'RGB':
                        img = img.convert('RGB')

                    # Save as WebP
                    img.save(output_path, 'WEBP', quality=quality)

                else:
                    # Static image (PNG/JPG or non-animated GIF)
                    # Convert to RGB mode if necessary
                    if img.mode in ('RGBA', 'LA', 'P'):
                        # Create white background for transparency
                        background = Image.new('RGB', img.size, (255, 255, 255))
                        if img.mode == 'P':
                            img = img.convert('RGBA')
                        # Paste with alpha mask
                        if img.mode in ('RGBA', 'LA'):
                            background.paste(img, mask=img.split()[-1])
                        else:
                            background.paste(img)
                        img = background
                    elif img.mode != 'RGB':
                        img = img.convert('RGB')

                    # Save as WebP
                    img.save(output_path, 'WEBP', quality=quality)

            # Get new file size
            new_size = output_path_obj.stat().st_size

            # Calculate size reduction
            size_reduction = ((original_size - new_size) / original_size) * 100 if original_size > 0 else 0

            # Format sizes for display
            original_size_kb = original_size / 1024
            new_size_kb = new_size / 1024

            # Use MB if file is large enough, otherwise KB
            if original_size_kb >= 1024:
                original_size_mb = original_size_kb / 1024
                new_size_mb = new_size_kb / 1024
                self.log_message(f"✓ {input_path_obj.name} -> {output_path_obj.name}")
                self.log_message(f"  Size: {original_size_mb:.2f}MB -> {new_size_mb:.2f}MB ({size_reduction:.1f}% reduction)")
            else:
                self.log_message(f"✓ {input_path_obj.name} -> {output_path_obj.name}")
                self.log_message(f"  Size: {original_size_kb:.2f}KB -> {new_size_kb:.2f}KB ({size_reduction:.1f}% reduction)")

            return True, "Success"

        except FileNotFoundError:
            return False, f"File not found: {input_path}"
        except PermissionError:
            return False, f"Permission denied: {output_path}"
        except Exception as e:
            return False, f"Error converting {Path(input_path).name}: {str(e)}"

    def log_message(self, message):
        """Add a message to the log with timestamp"""
        self.log_text.config(state='normal')
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_text.see(tk.END)
        self.log_text.config(state='disabled')


def main():
    """Main entry point"""
    if DND_AVAILABLE:
        root = TkinterDnD.Tk()
    else:
        root = tk.Tk()
    app = WebPConverter(root)
    root.mainloop()


if __name__ == "__main__":
    main()
