def process_localization_text(src_file_path, dest_file_path):
    def get_text_length(text):
        """计算文本长度，中文字符计2，其他字符计1"""
        length = 0
        for char in text:
            if '\u4e00' <= char <= '\u9fff':
                length += 2
            else:
                length += 1
        return length

    def split_text_by_length(text, max_length=40):
        """将文本按指定长度分割，保持单词和标点完整"""
        if not text:
            return []

        result = []
        current_line = ''
        current_length = 0
        
        chars = list(text)
        i = 0
        
        while i < len(chars):
            char = chars[i]
            char_length = 2 if '\u4e00' <= char <= '\u9fff' else 1
            
            if current_length + char_length > max_length and current_line:
                result.append(current_line)
                current_line = ''
                current_length = 0
                continue
            
            current_line += char
            current_length += char_length
            i += 1
        
        if current_line:
            result.append(current_line)
            
        return result

    def process_value(value):
        """处理单个本地化值"""
        parts = value.split('\\n\\n')
        processed_parts = []
        
        for part in parts:
            subparts = part.split('\\n')
            processed_subparts = []
            
            for subpart in subparts:
                if subpart.strip():
                    lines = split_text_by_length(subpart)
                    processed_subparts.extend(lines)
            
            processed_parts.append('\\n'.join(processed_subparts))
        
        return '\\n\\n'.join(processed_parts)

    # 读取源文件
    try:
        with open(src_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f'源文件不存在: {src_file_path}')
        return
    except Exception as e:
        print(f'读取源文件时出错: {str(e)}')
        return

    # 处理每一行
    new_lines = []
    for line in lines:
        line = line.strip()
        if not line:  # 保留空行
            new_lines.append('')
            continue
            
        if '=' not in line:  # 不是本地化键值对
            new_lines.append(line)
            continue
        
        key, value = line.split('=', 1)
        new_value = process_value(value)
        new_lines.append(f'{key}={new_value}')

    # 写入目标文件
    try:
        with open(dest_file_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(new_lines))
        print(f'成功导入文件: {dest_file_path}')
    except Exception as e:
        print(f'写入目标文件时出错: {str(e)}')

if __name__ == "__main__":
    import os

    # 定义要处理的文件列表
    files = [
        'game.txt',
        'menu.txt',
        'squad_name_pool.txt',
        'rmg_opname_pool.txt',
        'tips.txt',
        'campaigns.txt',
        'key_binding.txt'
    ]

    for filename in files:
        src_path = os.path.join('src\localization', filename)
        dest_path = os.path.join('localization', filename)
        
        try:
            if os.path.exists(src_path):
                print(f'处理文件: {filename}')
                process_localization_text(src_path, dest_path)
            else:
                print(f'跳过不存在的源文件: {src_path}')
        except Exception as e:
            print(f'处理 {filename} 时出错: {str(e)}')