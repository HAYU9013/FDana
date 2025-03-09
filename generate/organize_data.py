import os
import shutil

def organize_hspace(base_dir):

    # 定義路徑
    base_dir = base_dir + r'\hspace'
    photo_dir = os.path.join(base_dir, 'photo')
    original_dir = os.path.join(photo_dir, 'original')
    addnoise_dir = os.path.join(photo_dir, 'addnoise')
    # 建立資料夾
    os.makedirs(original_dir, exist_ok=True)
    os.makedirs(addnoise_dir, exist_ok=True)
    # 處理檔案
    for i in range(1, 55):
        file_name = f'{i}.pkl'
        file_path = os.path.join(base_dir, file_name)
        
        if i % 3 == 0:
            # 刪除檔案
            if os.path.exists(file_path):
                os.remove(file_path)
        elif i % 3 == 1:
            # 移動到 original 資料夾
            shutil.move(file_path, os.path.join(original_dir, file_name))
        elif i % 3 == 2:
            # 移動到 addnoise 資料夾
            shutil.move(file_path, os.path.join(addnoise_dir, file_name))

def organize_latents(base_dir):
    # 定義路徑
    base_dir = base_dir + r'\latents'
    photo_dir = os.path.join(base_dir, 'photo')
    original_dir = os.path.join(photo_dir, 'original')
    addnoise_dir = os.path.join(photo_dir, 'addnoise')

    # 建立資料夾
    os.makedirs(original_dir, exist_ok=True)
    os.makedirs(addnoise_dir, exist_ok=True)

    # 處理檔案
    for file_name in os.listdir(base_dir):
        file_path = os.path.join(base_dir, file_name)
        
        if 'original' in file_name:
            shutil.move(file_path, os.path.join(original_dir, file_name))
        elif 'addnoise' in file_name:
            shutil.move(file_path, os.path.join(addnoise_dir, file_name))

def move_to_analyze(target_dir):

def organize_data():
    base_dir = r'C:\coding\Professer Proj\Comfy\newMyComfy\myComfyUI\output'
    organize_hspace(base_dir)
    organize_latents(base_dir)