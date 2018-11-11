__author__ = 'mandar'

from mutagen import mp3
import glob, re, os, sys

TEST_FILE = r'path-to-test-file'
TEST_FOLDER = r'path-to-test-folder'

def load_files(path):
    '''
    Load files from a given folder
    :return: list of MP3 files
    '''
    mp3_files = []
    files = glob.glob(pathname=path + '/**/*.*', recursive=True)
    for file in files:
        try:
            if os.path.isdir(file):
                raise mp3.HeaderNotFoundError()
            mp3_files.append(mp3.MP3(file))
        except mp3.HeaderNotFoundError:
            print('Error: Invalid MP3, skipping - ' + file)
    print(str(len(mp3_files)) + ' MP3 files found.')
    return mp3_files

def clean_files(folder_path, regex_list):
    mp3_files = load_files(path=folder_path)
    for file in mp3_files:
        for regex in regex_list:
            clean_tags(file, regex=regex)

def print_values(tag, original_text, new_text):
    print(tag + ' > ' + original_text + ' > ' + new_text)

def clean_tags(id3_instance, regex):
    try:
        tags_list = list(id3_instance.keys())
        for tag in tags_list:
            original_tag = id3_instance.tags.get(tag)
            if tag.startswith('APIC:'):
                continue
            if tag.startswith('PRIV:') or tag.startswith('UFID:'):
                continue

            if hasattr(original_tag, 'text'):
                if isinstance(original_tag.text, list):
                    original_text = original_tag.text[0]
                    if isinstance(original_text, str):
                        new_text = re.sub(regex, '', original_text)
                        original_tag.text[0] = new_text
                        print_values(tag=tag, original_text=original_text, new_text=new_text)
                elif isinstance(original_tag.text, str):
                    original_text = original_tag.text
                    new_text = re.sub(regex, '', original_text)
                    original_tag.text = new_text
                    print_values(tag=tag, original_text=original_text, new_text=new_text)
            elif hasattr(original_tag, 'url'):
                original_text = original_tag.url
                if isinstance(original_text, str):
                    new_text = re.sub(regex, '', original_text)
                    original_tag.url = new_text
                    print_values(tag=tag, original_text=original_text, new_text=new_text)
            elif hasattr(original_tag, 'email'):
                original_text = original_tag.email
                if isinstance(original_text, str):
                    new_text = re.sub(regex, '', original_text)
                    original_tag.url = new_text
                    print_values(tag=tag, original_text=original_text, new_text=new_text)
            else:
                print('Unrecognized attribute found for tag ' + tag)
    except:
        print('Error occurred. ' + str(sys.exc_info()[0]))
    id3_instance.save()

if __name__ == '__main__':
    clean_files(folder_path=TEST_FOLDER, regex_list=[])
