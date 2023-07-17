text = """
...
"""
trimmed_lines = [line.strip() for line in text.split('\n') if line.strip()]
trimmed_text = '.'.join(trimmed_lines)

print(trimmed_text)
