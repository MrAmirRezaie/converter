# File Converter Utility

## Overview
This script (`converter.py`) provides a command-line interface for converting various file formats. It supports conversions between text, image, audio, video, spreadsheet, and document formats.

## Features
- Convert CSV to JSON and vice versa
- Convert PNG to JPEG and vice versa
- Convert Markdown (MD) to HTML and PDF
- Convert audio formats (MP3 to WAV, WAV to MP3, MP3 to OGG, etc.)
- Convert video formats (MP4 to AVI, AVI to MP4)
- Convert PDFs to text and images
- Convert DOCX and PPTX to PDF
- Resize images
- Convert YAML, JSON, and XML
- Convert Excel to CSV and vice versa
- Convert HTML to PDF and image
- Text-to-speech conversion

## Dependencies
Ensure you have the following Python packages installed:

```bash
pip install pillow markdown2 pydub pdfkit pypdf2 docx2pdf pandas gtts moviepy imgkit comtypes
```

Additional requirements:
- `wkhtmltopdf` (for HTML to PDF conversion)
- `ffmpeg` (for video processing)

## Usage
Run the script and follow the prompts to select a conversion type:

```bash
python converter.py
```

You will be asked to enter the input file path and the output file path. Some conversions require additional parameters such as width and height (for resizing images) or language (for text-to-speech conversion).

## Examples for Each Option

### 1. Convert CSV to JSON
```bash
python converter.py
# Choose option 1
# Enter input file path: data.csv
# Enter output file path: data.json
```

### 2. Convert JSON to CSV
```bash
python converter.py
# Choose option 2
# Enter input file path: data.json
# Enter output file path: data.csv
```

### 3. Convert PNG to JPEG
```bash
python converter.py
# Choose option 3
# Enter input file path: image.png
# Enter output file path: image.jpg
```

### 4. Convert JPEG to PNG
```bash
python converter.py
# Choose option 4
# Enter input file path: image.jpg
# Enter output file path: image.png
```

### 5. Convert Text (TXT) to Markdown (MD)
```bash
python converter.py
# Choose option 5
# Enter input file path: document.txt
# Enter output file path: document.md
```

### 6. Convert Markdown (MD) to HTML
```bash
python converter.py
# Choose option 6
# Enter input file path: document.md
# Enter output file path: document.html
```

### 7. Convert Raw Audio to WAV
```bash
python converter.py
# Choose option 7
# Enter input file path: audio.raw
# Enter output file path: audio.wav
```

### 8. Convert MP3 to WAV
```bash
python converter.py
# Choose option 8
# Enter input file path: audio.mp3
# Enter output file path: audio.wav
```

### 9. Convert PDF to Text
```bash
python converter.py
# Choose option 9
# Enter input file path: document.pdf
# Enter output file path: document.txt
```

### 10. Convert DOCX to PDF
```bash
python converter.py
# Choose option 10
# Enter input file path: document.docx
# Enter output file path: document.pdf
```

### 11. Resize an Image
```bash
python converter.py
# Choose option 11
# Enter input file path: image.png
# Enter output file path: resized_image.png
# Enter width: 200
# Enter height: 150
```

### 12. Convert HTML to PDF
```bash
python converter.py
# Choose option 12
# Enter input file path: page.html
# Enter output file path: page.pdf
```

### 13. Convert XML to JSON
```bash
python converter.py
# Choose option 13
# Enter input file path: data.xml
# Enter output file path: data.json
```

### 14. Convert YAML to JSON
```bash
python converter.py
# Choose option 14
# Enter input file path: data.yaml
# Enter output file path: data.json
```

### 15. Convert PPTX to PDF
```bash
python converter.py
# Choose option 15
# Enter input file path: presentation.pptx
# Enter output file path: presentation.pdf
```

### 16. Convert TXT to PDF
```bash
python converter.py
# Choose option 16
# Enter input file path: document.txt
# Enter output file path: document.pdf
```

### 17. Convert MD to PDF
```bash
python converter.py
# Choose option 17
# Enter input file path: document.md
# Enter output file path: document.pdf
```

### 18. Convert Image to PDF
```bash
python converter.py
# Choose option 18
# Enter input file path: image.png
# Enter output file path: document.pdf
```

### 19. Convert PDF to Image
```bash
python converter.py
# Choose option 19
# Enter input file path: document.pdf
# Enter output file path: image.png
```

### 20. Convert WAV to MP3
```bash
python converter.py
# Choose option 20
# Enter input file path: audio.wav
# Enter output file path: audio.mp3
```

### 21. Convert MP3 to OGG
```bash
python converter.py
# Choose option 21
# Enter input file path: audio.mp3
# Enter output file path: audio.ogg
```

### 22. Convert MP4 to AVI
```bash
python converter.py
# Choose option 22
# Enter input file path: video.mp4
# Enter output file path: video.avi
```

### 23. Convert AVI to MP4
```bash
python converter.py
# Choose option 23
# Enter input file path: video.avi
# Enter output file path: video.mp4
```

### 24. Convert Excel to CSV
```bash
python converter.py
# Choose option 24
# Enter input file path: data.xlsx
# Enter output file path: data.csv
```

### 25. Convert CSV to Excel
```bash
python converter.py
# Choose option 25
# Enter input file path: data.csv
# Enter output file path: data.xlsx
```

### 26. Convert JSON to XML
```bash
python converter.py
# Choose option 26
# Enter input file path: data.json
# Enter output file path: data.xml
```

### 27. Convert YAML to XML
```bash
python converter.py
# Choose option 27
# Enter input file path: data.yaml
# Enter output file path: data.xml
```

### 28. Convert HTML to Image
```bash
python converter.py
# Choose option 28
# Enter input file path: page.html
# Enter output file path: page.png
```

### 29. Convert Text to Speech
```bash
python converter.py
# Choose option 29
# Enter input file path: text.txt
# Enter output file path: speech.mp3
# Enter language code (e.g., 'en' for English)
```

## Logging
All conversion operations are logged in `file_converter.log`.

---

## Contributing

- If you would like to contribute to the development of this project, please submit a Pull Request or report new Issues.
---

## License

- This project is licensed under the MIT License. For more information, see the [LICENSE](https://github.com/MrAmirRezaie/networkTool/blob/main/LICENSE) file.
---
## Contact
For questions, feedback, or bug reports, contact the maintainer:
- **Email**: MrAmirRezaie70@gmail.com
- **Telegram**: [@MrAmirRezaie](https://t.me/MrAmirRezaie)
- **GitHub**: [MrAmirRezaie](https://github.com/MrAmirRezaie/)