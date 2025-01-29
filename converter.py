import os
import csv
import json
from PIL import Image
import markdown2
import wave
import struct
import logging
import fitz
from docx2pdf import convert
from pydub import AudioSegment
import pdfkit
import subprocess
import xml.etree.ElementTree as ET
import yaml
from pptx import Presentation
import pandas as pd
from gtts import gTTS
import moviepy.editor as mp
import imgkit

logging.basicConfig(filename='file_converter.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def log_message(message):
    print(message)
    logging.info(message)


def log_message(message):
    print(message)
    logging.info(message)


def csv_to_json(csv_file_path, json_file_path):
    """Convert CSV file to JSON."""
    data = []

    try:
        with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        log_message(f"CSV to JSON conversion completed: {json_file_path}")
    except Exception as e:
        log_message(f"Error converting CSV to JSON: {e}")


def json_to_csv(json_file_path, csv_file_path):
    """Convert JSON file to CSV."""
    try:
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        if not data:
            log_message("JSON file is empty.")
            return

        keys = data[0].keys()

        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=keys)
            csv_writer.writeheader()
            csv_writer.writerows(data)

        log_message(f"JSON to CSV conversion completed: {csv_file_path}")
    except Exception as e:
        log_message(f"Error converting JSON to CSV: {e}")


def png_to_jpeg(png_file_path, jpeg_file_path):
    """Convert PNG image to JPEG."""
    try:
        img = Image.open(png_file_path)
        rgb_img = img.convert('RGB')
        rgb_img.save(jpeg_file_path, 'JPEG')
        log_message(f"Image saved as {jpeg_file_path}")
    except Exception as e:
        log_message(f"Error converting PNG to JPEG: {e}")


def jpeg_to_png(jpeg_file_path, png_file_path):
    """Convert JPEG image to PNG."""
    try:
        img = Image.open(jpeg_file_path)
        img.save(png_file_path, 'PNG')
        log_message(f"Image saved as {png_file_path}")
    except Exception as e:
        log_message(f"Error converting JPEG to PNG: {e}")


def txt_to_md(txt_file_path, md_file_path):
    """Convert plain text file to Markdown."""
    try:
        with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
            content = txt_file.read()

        with open(md_file_path, 'w', encoding='utf-8') as md_file:
            md_file.write(content)

        log_message(f"Text to Markdown conversion completed: {md_file_path}")
    except Exception as e:
        log_message(f"Error converting Text to Markdown: {e}")


def md_to_html(md_file_path, html_file_path):
    """Convert Markdown file to HTML."""
    try:
        with open(md_file_path, 'r', encoding='utf-8') as md_file:
            content = md_file.read()

        html_content = markdown2.markdown(content)

        with open(html_file_path, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

        log_message(f"Markdown to HTML conversion completed: {html_file_path}")
    except Exception as e:
        log_message(f"Error converting Markdown to HTML: {e}")


def raw_audio_to_wav(raw_file_path, wav_file_path, sample_rate=44100, sample_width=2, channels=2):
    """Convert raw audio file to WAV."""
    try:
        with open(raw_file_path, 'rb') as raw_file:
            raw_data = raw_file.read()

        with wave.open(wav_file_path, 'wb') as wav_file:
            wav_file.setnchannels(channels)
            wav_file.setsampwidth(sample_width)
            wav_file.setframerate(sample_rate)
            wav_file.writeframesraw(raw_data)

        log_message(f"Raw audio to WAV conversion completed: {wav_file_path}")
    except Exception as e:
        log_message(f"Error converting Raw audio to WAV: {e}")


def mp3_to_wav(mp3_file_path, wav_file_path):
    """Convert MP3 audio file to WAV."""
    try:
        audio = AudioSegment.from_mp3(mp3_file_path)
        audio.export(wav_file_path, format="wav")
        log_message(f"MP3 to WAV conversion completed: {wav_file_path}")
    except Exception as e:
        log_message(f"Error converting MP3 to WAV: {e}")


def pdf_to_text(pdf_file_path, text_file_path):
    """Convert PDF file to plain text."""
    try:
        document = fitz.open(pdf_file_path)
        text = ""
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            text += page.get_text()

        with open(text_file_path, 'w', encoding='utf-8') as text_file:
            text_file.write(text)

        log_message(f"PDF to Text conversion completed: {text_file_path}")
    except Exception as e:
        log_message(f"Error converting PDF to Text: {e}")


def docx_to_pdf(docx_file_path, pdf_file_path):
    """Convert DOCX file to PDF."""
    try:
        convert(docx_file_path, pdf_file_path)
        log_message(f"DOCX to PDF conversion completed: {pdf_file_path}")
    except Exception as e:
        log_message(f"Error converting DOCX to PDF: {e}")


def resize_image(image_file_path, output_file_path, width, height):
    """Resize an image."""
    try:
        img = Image.open(image_file_path)
        resized_img = img.resize((width, height), Image.Resampling.LANCZOS)
        resized_img.save(output_file_path)
        log_message(f"Image resized and saved as {output_file_path}")
    except Exception as e:
        log_message(f"Error resizing image: {e}")


def html_to_pdf(html_file_path, pdf_file_path):
    """Convert HTML file to PDF."""
    try:

        if not os.path.exists(html_file_path):
            raise FileNotFoundError(f"HTML file {html_file_path} not found.")

        path_wkhtmltopdf = input("Enter path to wkhtmltopdf executable (e.g., /usr/bin/wkhtmltopdf): ")
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        pdfkit.from_file(html_file_path, pdf_file_path, configuration=config)
        log_message(f"HTML to PDF conversion completed: {pdf_file_path}")
    except Exception as e:
        log_message(f"Error converting HTML to PDF: {e}")


def xml_to_json(xml_file_path, json_file_path):
    """Convert XML file to JSON (supports nested elements)."""
    try:
        def xml_to_dict(element):
            result = {}
            for child in element:
                if len(child):
                    result[child.tag] = xml_to_dict(child)
                else:
                    result[child.tag] = child.text
            return result

        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        data = {root.tag: xml_to_dict(root)}

        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        log_message(f"XML to JSON conversion completed: {json_file_path}")
    except Exception as e:
        log_message(f"Error converting XML to JSON: {e}")


def yaml_to_json(yaml_file_path, json_file_path):
    """Convert YAML file to JSON."""
    try:
        with open(yaml_file_path, 'r', encoding='utf-8') as yaml_file:
            data = yaml.safe_load(yaml_file)

        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        log_message(f"YAML to JSON conversion completed: {json_file_path}")
    except Exception as e:
        log_message(f"Error converting YAML to JSON: {e}")


def pptx_to_pdf(pptx_file_path, pdf_file_path):
    """Convert PowerPoint (PPTX) file to PDF."""
    try:
        presentation = Presentation(pptx_file_path)
        presentation.save(pdf_file_path)
        log_message(f"PPTX to PDF conversion completed: {pdf_file_path}")
    except Exception as e:
        log_message(f"Error converting PPTX to PDF: {e}")


def txt_to_pdf(txt_file_path, pdf_file_path):
    """Convert plain text file to PDF."""
    try:
        with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
            content = txt_file.read()

        pdfkit.from_string(content, pdf_file_path)
        log_message(f"Text to PDF conversion completed: {pdf_file_path}")
    except Exception as e:
        log_message(f"Error converting Text to PDF: {e}")


def md_to_pdf(md_file_path, pdf_file_path):
    """Convert Markdown file to PDF."""
    try:
        with open(md_file_path, 'r', encoding='utf-8') as md_file:
            content = md_file.read()

        html_content = markdown2.markdown(content)
        pdfkit.from_string(html_content, pdf_file_path)
        log_message(f"Markdown to PDF conversion completed: {pdf_file_path}")
    except Exception as e:
        log_message(f"Error converting Markdown to PDF: {e}")


def image_to_pdf(image_file_path, pdf_file_path):
    """Convert image file to PDF."""
    try:
        img = Image.open(image_file_path)
        img.save(pdf_file_path, "PDF", resolution=100.0)
        log_message(f"Image to PDF conversion completed: {pdf_file_path}")
    except Exception as e:
        log_message(f"Error converting Image to PDF: {e}")


def pdf_to_image(pdf_file_path, image_file_path):
    """Convert PDF file to image."""
    try:
        document = fitz.open(pdf_file_path)
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            pix = page.get_pixmap()
            pix.save(f"{image_file_path}_page_{page_num + 1}.png")
        log_message(f"PDF to Image conversion completed: {image_file_path}")
    except Exception as e:
        log_message(f"Error converting PDF to Image: {e}")


def wav_to_mp3(wav_file_path, mp3_file_path):
    """Convert WAV audio file to MP3."""
    try:
        audio = AudioSegment.from_wav(wav_file_path)
        audio.export(mp3_file_path, format="mp3")
        log_message(f"WAV to MP3 conversion completed: {mp3_file_path}")
    except Exception as e:
        log_message(f"Error converting WAV to MP3: {e}")


def mp3_to_ogg(mp3_file_path, ogg_file_path):
    """Convert MP3 audio file to OGG."""
    try:
        audio = AudioSegment.from_mp3(mp3_file_path)
        audio.export(ogg_file_path, format="ogg")
        log_message(f"MP3 to OGG conversion completed: {ogg_file_path}")
    except Exception as e:
        log_message(f"Error converting MP3 to OGG: {e}")


def mp4_to_avi(mp4_file_path, avi_file_path):
    """Convert MP4 video file to AVI."""
    try:
        clip = mp.VideoFileClip(mp4_file_path)
        clip.write_videofile(avi_file_path, codec='mpeg4')
        log_message(f"MP4 to AVI conversion completed: {avi_file_path}")
    except Exception as e:
        log_message(f"Error converting MP4 to AVI: {e}")


def avi_to_mp4(avi_file_path, mp4_file_path):
    """Convert AVI video file to MP4."""
    try:
        clip = mp.VideoFileClip(avi_file_path)
        clip.write_videofile(mp4_file_path, codec='libx264')
        log_message(f"AVI to MP4 conversion completed: {mp4_file_path}")
    except Exception as e:
        log_message(f"Error converting AVI to MP4: {e}")


def excel_to_csv(excel_file_path, csv_file_path):
    """Convert Excel file to CSV."""
    try:
        df = pd.read_excel(excel_file_path)
        df.to_csv(csv_file_path, index=False)
        log_message(f"Excel to CSV conversion completed: {csv_file_path}")
    except Exception as e:
        log_message(f"Error converting Excel to CSV: {e}")


def csv_to_excel(csv_file_path, excel_file_path):
    """Convert CSV file to Excel."""
    try:
        df = pd.read_csv(csv_file_path)
        df.to_excel(excel_file_path, index=False)
        log_message(f"CSV to Excel conversion completed: {excel_file_path}")
    except Exception as e:
        log_message(f"Error converting CSV to Excel: {e}")


def json_to_xml(json_file_path, xml_file_path):
    """Convert JSON file to XML."""
    try:
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        def dict_to_xml(tag, d):
            elem = ET.Element(tag)
            for key, val in d.items():
                child = ET.Element(key)
                child.text = str(val)
                elem.append(child)
            return elem

        root = dict_to_xml('root', data)
        tree = ET.ElementTree(root)
        tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)

        log_message(f"JSON to XML conversion completed: {xml_file_path}")
    except Exception as e:
        log_message(f"Error converting JSON to XML: {e}")


def yaml_to_xml(yaml_file_path, xml_file_path):
    """Convert YAML to XML (supports nested structures)."""
    try:
        with open(yaml_file_path, 'r') as yaml_file:
            data = yaml.safe_load(yaml_file)

        def dict_to_xml(parent, data):
            for key, value in data.items():
                element = ET.SubElement(parent, key)
                if isinstance(value, dict):
                    dict_to_xml(element, value)
                else:
                    element.text = str(value)

        root = ET.Element('root')
        dict_to_xml(root, data)
        tree = ET.ElementTree(root)
        tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)
        log_message(f"YAML to XML conversion completed: {xml_file_path}")
    except Exception as e:
        log_message(f"Error converting YAML to XML: {e}")


def html_to_image(html_file_path, image_file_path):
    """Convert HTML file to image."""
    try:
        imgkit.from_file(html_file_path, image_file_path)
        log_message(f"HTML to Image conversion completed: {image_file_path}")
    except Exception as e:
        log_message(f"Error converting HTML to Image: {e}")


def text_to_speech(text_file_path, audio_file_path, language='en'):
    """Convert text to speech."""
    try:
        with open(text_file_path, 'r', encoding='utf-8') as text_file:
            text = text_file.read()

        tts = gTTS(text=text, lang=language)
        tts.save(audio_file_path)
        log_message(f"Text to Speech conversion completed: {audio_file_path}")
    except Exception as e:
        log_message(f"Error converting Text to Speech: {e}")


def main():
    print("Choose conversion type:")
    print("1. CSV to JSON")
    print("2. JSON to CSV")
    print("3. PNG to JPEG")
    print("4. JPEG to PNG")
    print("5. Text (TXT) to Markdown (MD)")
    print("6. Markdown (MD) to HTML")
    print("7. Raw Audio to WAV")
    print("8. MP3 to WAV")
    print("9. PDF to Text")
    print("10. DOCX to PDF")
    print("11. Resize Image")
    print("12. HTML to PDF")
    print("13. XML to JSON")
    print("14. YAML to JSON")
    print("15. PPTX to PDF")
    print("16. TXT to PDF")
    print("17. MD to PDF")
    print("18. Image to PDF")
    print("19. PDF to Image")
    print("20. WAV to MP3")
    print("21. MP3 to OGG")
    print("22. MP4 to AVI")
    print("23. AVI to MP4")
    print("24. Excel to CSV")
    print("25. CSV to Excel")
    print("26. JSON to XML")
    print("27. YAML to XML")
    print("28. HTML to Image")
    print("29. Text to Speech")

    choice = input("Enter your choice (1-29): ")

    file_input = input("Enter input file path: ")
    file_output = input("Enter output file path: ")

    if choice == "1":
        csv_to_json(file_input, file_output)
    elif choice == "2":
        json_to_csv(file_input, file_output)
    elif choice == "3":
        png_to_jpeg(file_input, file_output)
    elif choice == "4":
        jpeg_to_png(file_input, file_output)
    elif choice == "5":
        txt_to_md(file_input, file_output)
    elif choice == "6":
        md_to_html(file_input, file_output)
    elif choice == "7":
        raw_audio_to_wav(file_input, file_output)
    elif choice == "8":
        mp3_to_wav(file_input, file_output)
    elif choice == "9":
        pdf_to_text(file_input, file_output)
    elif choice == "10":
        docx_to_pdf(file_input, file_output)
    elif choice == "11":
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        resize_image(file_input, file_output, width, height)
    elif choice == "12":
        html_to_pdf(file_input, file_output)
    elif choice == "13":
        xml_to_json(file_input, file_output)
    elif choice == "14":
        yaml_to_json(file_input, file_output)
    elif choice == "15":
        pptx_to_pdf(file_input, file_output)
    elif choice == "16":
        txt_to_pdf(file_input, file_output)
    elif choice == "17":
        md_to_pdf(file_input, file_output)
    elif choice == "18":
        image_to_pdf(file_input, file_output)
    elif choice == "19":
        pdf_to_image(file_input, file_output)
    elif choice == "20":
        wav_to_mp3(file_input, file_output)
    elif choice == "21":
        mp3_to_ogg(file_input, file_output)
    elif choice == "22":
        mp4_to_avi(file_input, file_output)
    elif choice == "23":
        avi_to_mp4(file_input, file_output)
    elif choice == "24":
        excel_to_csv(file_input, file_output)
    elif choice == "25":
        csv_to_excel(file_input, file_output)
    elif choice == "26":
        json_to_xml(file_input, file_output)
    elif choice == "27":
        yaml_to_xml(file_input, file_output)
    elif choice == "28":
        html_to_image(file_input, file_output)
    elif choice == "29":
        language = input("Enter language code (e.g., 'en' for English): ")
        text_to_speech(file_input, file_output, language)
    else:
        print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()