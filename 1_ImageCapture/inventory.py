import os, time, datetime, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s","--source", type=str)
parser.add_argument("-d","--destination", type=str)
args = parser.parse_args()

target_dir = args.source
output_dir = args.destination
timestr = time.strftime("%Y%m%d-%H%M%S")

def file_stats(file_path):
    stat_info = os.stat(file_path)
    file_name = os.path.basename(file_path)
    file_size = stat_info.st_size
    date_created = time.ctime(stat_info.st_ctime)
    date_modified = time.ctime(stat_info.st_mtime)
    return f"{file_name};{file_path};{file_size};{date_created};{date_created};{date_modified}"

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