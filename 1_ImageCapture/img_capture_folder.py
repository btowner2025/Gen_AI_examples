import os, time, datetime, argparse
from pillow_heif import register_heif_opener
from PIL import Image, UnidentifiedImageError
from transformers import AutoProcessor, BlipForConditionalGeneration

parser = argparse.ArgumentParser()
parser.add_argument("-s","--source", type=str)
parser.add_argument("-d","--destination", type=str)
args = parser.parse_args()

target_dir = args.source
output_dir = args.destination
timestr = time.strftime("%Y%m%d-%H%M%S")


def img_label(file_path):
    # Load the pretrained processor and model
    processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    # Load your image or pass variable
    img_path = file_path

   # Check if the file exists
    if not os.path.isfile(file_path):
        print("The file does not exist.")
    else:
        register_heif_opener()  # enables PIL to open HEIC/HEIF

        # Try to identify whether it's an image
        try:
            # convert it into an RGB format 
            image = Image.open(img_path).convert('RGB')
            inputs = processor(images=image, return_tensors="pt")
            # Generate a caption for the image
            outputs = model.generate(**inputs, max_length=50)
            # Decode the generated tokens to text
            caption = processor.decode(outputs[0], skip_special_tokens=True)
        except UnidentifiedImageError:
            caption = "The file is NOT an image file."
        except Exception as e:
            caption = "Unexpected error: {e}"
    return (caption)

def file_stats(file_path):
    stat_info = os.stat(file_path)
    file_name = os.path.basename(file_path)
    file_size = stat_info.st_size
    date_created = time.ctime(stat_info.st_ctime)
    date_modified = time.ctime(stat_info.st_mtime)
    file_caption = img_label(file_path)
    # file_caption = ""
    return f"{file_name};{file_path};{file_size};{date_created};{date_modified};{file_caption}"

def list_files(directory_path, output_file):
    with open(output_file,"w", encoding="utf-8") as f:
        f.write("File Name; File Path; File Size; Date Created; Date Modified; Image Caption\n")
        for dirpath, _, filenames in os.walk(directory_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                file_info = file_stats(file_path)
                f.write(file_info + "\n")

if __name__ == "__main__":
    source_directory = args.source # replace with the desired source directory path
    output_file = (args.destination + 'Inventory-' + timestr + '.txt') # replace with the desired output file name
    list_files(source_directory,output_file)





 