import os
import sys
#python export_folder.py ./my_project output.txt
def export_folder_structure(folder_path, output_file):
    """
    导出文件夹结构和文件内容到文本文件
    
    参数:
        folder_path (str): 要遍历的文件夹路径
        output_file (str): 输出文本文件路径
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f_out:
            # 写入头部标记
            f_out.write("# FOLDER STRUCTURE EXPORT FILE #\n")
            f_out.write(f"# SOURCE: {os.path.abspath(folder_path)}\n\n")
            
            for root, dirs, files in os.walk(folder_path):
                # 计算相对路径
                rel_path = os.path.relpath(root, folder_path)
                if rel_path == '.':
                    rel_path = ''
                
                # 写入目录标记
                f_out.write(f"[DIR] {rel_path.replace(os.sep, '/')}\n")
                
                # 写入文件内容
                for file in files:
                    file_path = os.path.join(root, file)
                    rel_file_path = os.path.join(rel_path, file).replace(os.sep, '/')
                    
                    f_out.write(f"[FILE] {rel_file_path}\n")
                    
                    # 尝试读取文件内容
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f_in:
                            content = f_in.read()
                            f_out.write(content)
                    except UnicodeDecodeError:
                        f_out.write("[BINARY FILE CONTENT NOT EXPORTED]\n")
                    except Exception as e:
                        f_out.write(f"[ERROR READING FILE: {str(e)}]\n")
                    
                    f_out.write("\n[END FILE]\n\n")
            
            f_out.write("# END OF EXPORT #\n")
        print(f"成功导出文件夹结构和内容到: {output_file}")
    except Exception as e:
        print(f"导出过程中出错: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使用方法: python export_folder.py <文件夹路径> <输出文件路径>")
        print("示例: python export_folder.py ./my_project output.txt")
    else:
        folder_path = sys.argv[1]
        output_file = sys.argv[2]
        
        if not os.path.isdir(folder_path):
            print(f"错误: '{folder_path}' 不是有效的文件夹路径")
        else:
            export_folder_structure(folder_path, output_file)