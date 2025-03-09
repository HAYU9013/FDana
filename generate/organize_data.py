import os
import shutil

def organize_hspace(base_dir, folder_name):

    # 定義路徑
    base_dir = base_dir + r'\lab\hspace'
    photo_dir = os.path.join(base_dir, folder_name)
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

def organize_latents(base_dir, folder_name):
    # 定義路徑
    base_dir = base_dir + r'\latents'
    photo_dir = os.path.join(base_dir,  folder_name)
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

def move_to_analyze(base_dir, folder_name, category, target_dir):
    latent_dir = os.path.join(base_dir, 'latents', folder_name)
    hspace_dir = os.path.join(base_dir,'lab', 'hspace', folder_name)
    latent_analyze_dir = os.path.join(target_dir, 'latent', category)
    hspace_analyze_dir = os.path.join(target_dir, 'hspace', category)

    os.makedirs(latent_analyze_dir, exist_ok=True)
    os.makedirs(hspace_analyze_dir, exist_ok=True)

    shutil.move(latent_dir, latent_analyze_dir)
    shutil.move(hspace_dir, hspace_analyze_dir)

    # input_dir = os.path.join(base_dir, '..', 'input')
    # target_input_dir = os.path.join(latent_analyze_dir, '..', '..', 'input')

    # print(input_dir)
    # print(target_input_dir)
    
    # os.makedirs(target_input_dir, exist_ok=True)
    
    # for file_name in os.listdir(input_dir):
    #     if folder_name+".png" == file_name:
    #         shutil.copy(os.path.join(input_dir, file_name), os.path.join(target_input_dir, file_name))
    


def organize_data(folder_name = "photo", category = "car"):
    base_dir = r'C:\coding\Professer Proj\Comfy\newMyComfy\myComfyUI\output'
    target_dir = r'C:\coding\Professer Proj\Comfy\newMyComfy\FDanalyze\analyze'
    organize_hspace(base_dir=base_dir, folder_name=folder_name)
    organize_latents(base_dir=base_dir, folder_name=folder_name)
    move_to_analyze(base_dir=base_dir, folder_name=folder_name, category=category, target_dir=target_dir)

if __name__ == '__main__':
    organize_data(folder_name="redcar", category="car")