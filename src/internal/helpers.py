def log(s: any) -> None:
    print("\033[92m" + "INFO: GENERAL: " + str(s) + "\033[0m")


def get_main_py_directory():
    import os

    return os.path.dirname(os.path.realpath(__file__)).replace("internal", "")
