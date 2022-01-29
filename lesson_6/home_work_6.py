import os
import sys
import shutil



def create_dirs_from_list(path, ext_dict):
    for dir in ext_dict:
        if not os.path.exists(f'{path}\\{dir}'):
            os.mkdir(f'{path}\\{dir}')



def get_dirs_list(folder_path):
    get_folder_list = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    return get_folder_list



def get_files_list(folder_path):
    file_list = [f.path for f in os.scandir(folder_path) if f.is_file()]

    return file_list



def get_immediate_subdirectories(path):
    return [name for name in os.listdir(path)
            if os.path.isdir(os.path.join(path, name))]



def normalize(name, ext): # заменяет кирилицу 
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

    TRANS = {
             ord('.') : '_', ord('!') : '_', ord('@') : '_', ord('#') : '_', ord('$') : '_', ord('%') : '_', ord('^') : '_',
             ord('&') : '_', ord('(') : '_', ord(')') : '_', ord('-') : '_', ord('=') : '_', ord('+') : '_', ord(',') : '_'
             }
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()    

    name = name.split('\\')[-1]
        
    return f'{name.translate(TRANS)}{ext}'



def sort_files_in_dir(path, main_path):
    main_path = main_path
    files_list = get_files_list(path)
    print(files_list)
    dirs_lists = get_dirs_list(path)
    print(dirs_lists)

    if path == main_path: # исключаем папки из ext_dict из списка папок для сортировки
        dirs_names = get_immediate_subdirectories(path)
        for dir_name in dirs_names:
            print(dir_name)
            if dir_name in ext_dict:
                dir = os.path.join(path, dir_name)
                dirs_lists.remove(dir)
                print(dir)

        create_dirs_from_list(path, ext_dict)
        print(dirs_lists, 'after sort')

    for file_name in files_list: # начало сортировки файлов по папкам
        name, ext = os.path.splitext(file_name)
        norm_file_name = normalize(name, ext)
        
        if ext in ext_dict.get('archive'):
            new_path = f'{main_path}\\archive\\{norm_file_name}'
            unpack(file_name, ext, new_path)
            os.remove(file_name)
            continue

        for new_dir, val in ext_dict.items():
            if ext in val:
                new_path = f'{main_path}\\{new_dir}'
                os.replace(f'{file_name}', f'{new_path}\\{norm_file_name}')  # перемещаем фаил в папку из ext_dict
                break
            
    files_list = get_files_list(path)
    for file_name in files_list: # перемещаем фаил в папку не из ext_dict
        name, ext = os.path.splitext(file_name)
        norm_file_name = normalize(name, ext)
        new_path = f'{main_path}\\other'
        os.replace(f'{file_name}', f'{new_path}\\{norm_file_name}')
        if ext not in ext_dict.get('other'):
            ext_dict['other'] += [ext]

    print('Сортировка файлов в папке ' + path + ' завершена.')

    if dirs_lists != []:
        for dir in dirs_lists:
           new_path = os.path.join(path, dir)
           sort_files_in_dir(new_path, main_path)
           print('Удаляю папку '+ new_path + ' после сортировки.' )
           os.rmdir(new_path)
           
        else:
            print('Сортировка в папке '+ path + ' завершена.')



def unpack(file_name, archive_format, new_path):

    shutil.unpack_archive(file_name, new_path, archive_format)
    print("Archive file unpacked successfully.")



if __name__ == '__main__':

    # key names will be folder names!
    ext_dict = {
                'audio' : ['.mp3', '.ogg', '.wav', '.amr'], 
                'archive': ['.zip', '.gz', '.tar'], 
                'documents' : ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'], 
                'image' : ['.jpeg', '.png', '.jpg', '.svg', '.bmp', '.tif', '.tiff'], 
                'other': ['!', ], 
                'video' : ['.avi', '.mp4', '.mov', '.mkv', '.mpeg'], 
    }

    main_path = sys.argv[1]

    sort_files_in_dir(main_path, main_path)






