import re
import glob, os

def sanitize_mathematica(file):
    with open(file, "r") as f:

        # Get comment sections of text
        parsed = ''
        text = f.read()
        L = len(text)
        for ch in range(L-1):
            if (text[ch] == '(') & (text[ch+1] == '*'):
                comment_index = ch+1
                while( (text[comment_index] != '*') or (text[comment_index+1] != ')') ):
                    parsed += text[comment_index+1]
                    comment_index += 1
                ch = comment_index

        # Remove excess characters and words
        sanitized_text = parsed.replace('RowBox[', '').replace('\"\[IndentingNewLine]\"', '').replace('\"','')
        sanitized_text = re.sub(r'[\{\}\[\],\*]+', ' ', sanitized_text)  # Remove braces, brackets, commas, and asterisks
        sanitized_text = re.sub(r'\s+', ' ', sanitized_text)   # Replace multiple spaces with a single space
        sanitized_text = sanitized_text.strip()                # Remove leading and trailing spaces

        # Add newlines
        readable_text = re.sub("(.{64})", "\\1\n", sanitized_text, 0, re.DOTALL)

    with open(os.path.splitext(file)[0]+"_comments.txt", 'w') as f:
        f.write(readable_text)


if __name__=='__main__':
    files = glob.glob("*.nb")
    for file in files:
        sanitize_mathematica(file)

