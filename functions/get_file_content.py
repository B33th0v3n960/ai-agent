import os

from functions.errors import InvalidPath

MAX_CHARS = 10_000


def get_file_content(working_directory: str, file_path: str) -> str:
    output = ""
    try:
        working_dir_abs = os.path.abspath(working_directory)

        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = (
            os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
        )

        if not valid_target_dir:
            raise InvalidPath(
                f'Cannot read "{file_path}" as it is outside the permitted working directory'
            )

        if not os.path.isfile(target_path):
            raise InvalidPath(
                f'File not found or is not a regular file: "{file_path}"'
            )
        
        with open(target_path, "r") as file:
            output += file.read(MAX_CHARS)
            if file.read(1):
                output += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

    except InvalidPath as error:
        output += f"Error: {error}"
    except Exception as error:
        output += f"Error: {error}"

    return output
