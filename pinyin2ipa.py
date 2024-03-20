import re

def main():
    # ファイルからテキストを読み込む
    with open('wuu_in.txt', 'r') as file:
        original_text = file.read()

    # 各置換操作をリストに格納
    replacements = [
        (r'(.*)(ng)', r'\1ŋ'),
        (r'sh', 'ʂ'),
        (r'zh', 'tʂ'),
        (r'ch', 'ʈʂʰ'),
        (r'yu', 'ɥ'),
        (r'yang', 'yɑng'),
        (r'(.*)(iang)', r'\1yɑng'),
        (r'yan', 'yɛn'),
        (r'(.*)(ian)', r'\1iɛn'),
        (r'yuan', 'yuɛn'),
        (r'(.*)(üan)', r'\1üɛn'),
        (r'ye', 'ye̞'),
        (r'(.*)(ie)', r'\1ie̞'),
        (r'yue', 'yue̞'),
        (r'(.*)(üe)', r'\1üe̞'),
        (r'en', 'ən'),
        (r'eng', 'əng'),
        (r'er', 'ɚ'),
        (r'yi', 'i'),
        (r'(.*)(i)', r'\1i'),
        (r'wo', 'wo̞'),
        (r'zhi', 'zhɻ̩'),
        (r'chi', 'chɻ̩'),
        (r'shi', 'shɻ̩'),
        (r'ri', 'rɻ̩'),
        (r'zi', 'zɹ̩'),
        (r'ci', 'cɹ̩'),
        (r'si', 'sɹ̩'),
        (r'wu', 'u'),
        (r'(.*)(u)', r'\1u'),
        (r'(.*)(ong)', r'\1ʊng'),
        (r'k', 'kʰ'),
        (r'p', 'pʰ'),
        (r't', 'tʰ'),
        (r'j', 'tɕ'),
        (r'q', 'tɕʰ'),
        (r'z', 'ts'),
        (r'c', 'tsʰ'),
        (r'yu', 'y'),
        (r'(.*)(ü)', r'\1y')
    ]

    # 各置換操作を適用
    for pattern, replacement in replacements:
        original_text = re.sub(pattern, replacement, original_text)

    # 文字ごとの置換を実行
    translation_table = str.maketrans('xfyglmnbrsdwhae', 
                                      'ɕfjklmnprstwxäɤ')
    translated_text = original_text.translate(translation_table)

    # 変換結果をファイルに書き込む
    with open('Wuu_in_IPA.txt', 'w') as file:
        file.write(translated_text)

if __name__ == "__main__":
    main()
