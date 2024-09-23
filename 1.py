'''
Author: zhang 2672961671@qq.com
Date: 2024-09-23 23:26:58
LastEditors: zhang 2672961671@qq.com
LastEditTime: 2024-09-24 00:52:10
FilePath: /undefined/Users/zhanghongping/Library/Containers/com.tencent.WeWorkMac/Data/Documents/Profiles/4E0C1A2B34695EF5CBEED9C978379A9C/Caches/Files/2024-09/4d8dcd153440326ce6259dd10c520cf6/1.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os  
import shutil  

# inPath = "F:\\work\\BrainHole2\\assets\\Game\\Levels"
# outPath = "F:\\work\\outFiles"

# 生成文件夹
# 循环
# for i in range(1041, 1088):  
#     folder_path = outPath + "\\LevelBrain" + str(i)
#     # 尝试删除目录及其所有内容  
#     try:  
#         shutil.rmtree(outPath)  
#         # 如果需要，可以在这里重新创建空目录  
#         # 注意：如果父目录不存在，os.mkdir() 会失败，所以你可能需要使用 os.makedirs(directory_path, exist_ok=True)  
#         os.makedirs(outPath, exist_ok=True)  
#         # print(f"目录 {outPath} 的内容已被删除，并且目录已重新创建（如果它之前不存在的话）。")  
#     except OSError as e:  
#         print(f"删除目录 {outPath} 时出错。原因：{e}")
#     try:  
#         os.makedirs(folder_path)  
#         print(f"文件夹 {folder_path} 创建成功。")  
#     except FileExistsError:  
#         print(f"文件夹 {folder_path} 已存在。")  
#     except Exception as e:  
#         print(f"创建文件夹时发生错误：{e}")

# 判断文件夹是否为空
# def is_dir_empty(path):  
#     """  
#     检查指定路径的文件夹是否为空  
#     :param path: 文件夹的路径  
#     :return: 如果文件夹为空则返回True，否则返回False  
#     """  
#     # os.listdir(path) 列出指定目录下的所有文件和子目录名  
#     # 如果列表为空，则文件夹为空  
#     return not os.listdir(path)  



# def ensure_folder(folder_path):
#     if os.path.exists(folder_path):
#         # 清空文件夹
#         shutil.rmtree(folder_path)
#         os.makedirs(folder_path)  # 重新创建文件夹
#     else:
#         os.makedirs(folder_path)  # 创建文件夹

# folder_path = '你的文件夹路径'
# ensure_folder(folder_path)

# 当前路径
# current_file_path = os.path.abspath(__file__)
# print(current_file_path)

# aaa结尾的路径
def find_files_and_dirs(path):
    matches = []
    for root, dirs, files in os.walk(path):
        for name in files + dirs:
            print(name)
            if name.endswith('aaa'):
                matches.append(os.path.join(root, name))
    return matches

folder_path = '/Users/zhanghongping/SourceTreeFiles'
results = find_files_and_dirs(folder_path)
print(results)

# 遍历文件夹，找出以 "aaa" 结尾的文件和文件夹，并将它们复制到指定目录：
# def copy_files_and_dirs(src_path, dest_path):
#     if not os.path.exists(dest_path):
#         os.makedirs(dest_path)

#     for root, dirs, files in os.walk(src_path):
#         for name in files + dirs:
#             if name.endswith('aaa'):
#                 full_path = os.path.join(root, name)
#                 shutil.copy(full_path, dest_path)

# src_folder = '源文件夹路径'
# dest_folder = '目标文件夹路径'
# copy_files_and_dirs(src_folder, dest_folder)

