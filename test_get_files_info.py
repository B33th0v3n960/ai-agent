from functions.get_files_info import get_files_info

output: str|None = None

output = get_files_info("calculator", ".")
print(output)
output = get_files_info("calculator", "pkg")
print(output)
output = get_files_info("calculator", "/bin")
print(output)
output = get_files_info("calculator", "../")
print(output)
