def process_localization_text(src_file_path, dest_file_path, max_length=40):
    def get_text_length(text):
        length = 0
        for char in text:
            if '\u4e00' <= char <= '\u9fff':
                length += 2
            else:
                length += 1
        return length

    def split_text_by_length(text, max_length=40):
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

    def process_value(value, max_length):
        parts = value.split('\\n\\n')
        processed_parts = []
        
        for part in parts:
            subparts = part.split('\\n')
            processed_subparts = []
            
            for subpart in subparts:
                if subpart.strip():
                    lines = split_text_by_length(subpart, max_length)
                    processed_subparts.extend(lines)
            
            processed_parts.append('\\n'.join(processed_subparts))
        
        return '\\n\\n'.join(processed_parts)

    try:
        with open(src_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f'源文件不存在: {src_file_path}')
        return
    except Exception as e:
        print(f'读取源文件时出错: {str(e)}')
        return

    new_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            new_lines.append('')
            continue
            
        if '=' not in line:
            new_lines.append(line)
            continue
        
        key, value = line.split('=', 1)
        new_value = process_value(value, max_length)
        new_lines.append(f'{key}={new_value}')

    try:
        with open(dest_file_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(new_lines))
        print(f'成功导入文件: {dest_file_path}')
    except Exception as e:
        print(f'写入目标文件时出错: {str(e)}')

if __name__ == "__main__":
    import os

    files = {
        'game.txt': 40,
        'briefings.txt': 30
    }

    for filename, max_length in files.items():
        src_path = os.path.join('src\localization', filename)
        dest_path = os.path.join('localization', filename)
        
        try:
            if os.path.exists(src_path):
                print(f'处理文件: {filename}')
                process_localization_text(src_path, dest_path, max_length)
            else:
                print(f'跳过不存在的源文件: {src_path}')
        except Exception as e:
            print(f'处理 {filename} 时出错: {str(e)}')