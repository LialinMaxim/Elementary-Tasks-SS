def file_parcer(file_path, source_text, replace_text=None):
    '''file parser
    counts the number of occurrences or replaces the string with a given

    :param file_path: str
    :param source_text: str
    :param replace_text: str
    :return: int, None if file wasn't open
    '''
    if not isinstance(file_path, (str)):
        print("TypeError,", 'file path:', file_path)
        return None
    if not isinstance(source_text, (str)):
        print("TypeError,", 'source_text:', file_path)
        return None
    if not isinstance(replace_text, (str)) and replace_text:
        print("TypeError,", 'replace_text:', file_path)
        return None

    str_count = 0
    try:
        with open(file_path) as f:
            for line in f:
                str_count += line[:].count(source_text)
    except FileNotFoundError:
        print("FileNotFoundError,", 'file path:', file_path)
        return None

    if replace_text:
        with open(file_path) as f:
            text = f.read()
        with open(file_path, 'w') as f:
            f.write(text.replace(source_text, replace_text))
    return str_count


if __name__ == "__main__":
    f = 'static_files/lipsum.txt'
    print((file_parcer(f, 'F')))
    print((file_parcer(f, 'f', 'F')))
    print((file_parcer(f, 'f')))


