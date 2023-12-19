import os



FunK = input('請輸入調用範例 : ')

if FunK == 'pointcloud':
    fld = input('請命名輸出資料夾名稱 : ')
    os.system(f'python mapping_visu.py --outputFolder {fld}')