import os

from functions.errors import InvalidPath


def get_files_info(working_directory: str, directory: str = ".") -> str:
    output = ""
    if directory != ".":
        output += f"Result for '{directory}' directory:\n"
    else:
        output += f"Result for current directory:\n"

    try:
        working_dir_abs = os.path.abspath(working_directory)

        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        )

        if not valid_target_dir:
            raise InvalidPath(
                f'Cannot list "{directory}" as it is outside the permitted working directory'
            )

        if not os.path.isdir(target_dir):
            raise InvalidPath(f'"{directory}" is not a directory')

        for file in os.listdir(target_dir):
            file_path = os.path.join(target_dir, file)
            output += f"  - {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}\n"

    except InvalidPath as error:
        output += f"  Error: {error}"
    except Exception as error:
        output += f"  Error: {error}"

    return output
