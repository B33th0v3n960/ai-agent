import os


class InvalidPath(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"


def get_files_info(working_directory: str, directory: str = ".") -> str:
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

        return f'Success: "{directory}" is within the working directory'
    except InvalidPath as error:
        return f"Error: {error}"
    except Exception as error:
        return f"Error: {error}"
