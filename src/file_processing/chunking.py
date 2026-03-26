import os


def simple_checking(line: str):
	if "Вопрос" in line and "Ответ" in line:
		if line.find("Вопрос") < line.find("Ответ"):
			return True
	return False


def qa_chunk_processing(file_path: str, chunk_size: int = 300):
	with open(file_path, 'r', encoding='utf-8') as f:
		lines = f.read()
	lines = lines.split('\n\n')

	for line in lines:
		if not simple_checking(line):
			raise ValueError(f"Строка не соответствует формату Вопрос-Ответ:\n{line}")

	ind = 1
	while ind < len(lines):
		if len(lines[ind - 1]) + len(lines[ind]) <= chunk_size:
			lines[ind - 1] += '\n' + lines[ind]
			lines.remove(lines[ind])
		else:
			ind += 1

	return lines


def chunk_directory(dir: str, chunk_size: int = 300):
	result = []
	for root, ders, files in os.walk(dir):
		for file in files:
			file_path = os.path.join(root, file)
			result.append(qa_chunk_processing(file_path, chunk_size))

	return result

if __name__ == '__main__':
	qa_chunk_processing("C:/Users/PC/Desktop/dataset/Настолки.txt")
