def process_localization_text(file_path):
    def get_text_length(text):
        """计算文本长度，中文字符计2，其他字符计1"""
        length = 0
        for char in text:
            if '\u4e00' <= char <= '\u9fff':
                length += 2
            else:
                length += 1
        return length

    def split_text_by_length(text, max_length=44):
        """将文本按指定长度分割，保持单词和标点完整"""
        if not text:
            return []

        result = []
        current_line = ''
        current_length = 0
        
        # 按空格和标点符号分割文本
        chars = list(text)
        i = 0
        
        while i < len(chars):
            char = chars[i]
            char_length = 2 if '\u4e00' <= char <= '\u9fff' else 1
            
            # 如果添加当前字符会超出长度限制
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
        # 处理连续换行的情况
        parts = value.split('\\n\\n')
        processed_parts = []
        
        for part in parts:
            # 处理每个由单个\n分隔的部分
            subparts = part.split('\\n')
            processed_subparts = []
            
            for subpart in subparts:
                if subpart.strip():  # 如果不是空字符串
                    lines = split_text_by_length(subpart)
                    processed_subparts.extend(lines)
            
            processed_parts.append('\\n'.join(processed_subparts))
        
        # 重新组合所有部分，保持双换行
        return '\\n\\n'.join(processed_parts)

    # 读取文件
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

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
        
        # 分离键和值
        key, value = line.split('=', 1)
        
        # 处理值部分
        new_value = process_value(value)
        
        # 组合新行
        new_lines.append(f'{key}={new_value}')

    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(new_lines))

if __name__ == "__main__":
    localization_files = [
        # 'localization/briefings.txt',
        'localization/game.txt'
    ]

    for file_path in localization_files:
        try:
            print(f'处理文件: {file_path}')
            process_localization_text(file_path)
            print(f'成功处理: {file_path}')
        except Exception as e:
            print(f'处理 {file_path} 时出错: {str(e)}')