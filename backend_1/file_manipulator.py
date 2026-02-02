import argparse
from abc import ABC, abstractmethod


class FileManipulator(ABC):
    @staticmethod
    @abstractmethod
    def validate_args(args):
        pass

    @staticmethod
    @abstractmethod
    def execute(args):
        pass


class ReverseFile(FileManipulator):
    @staticmethod
    def validate_args(args):
        if args.outputpath is None:
            raise ValueError("outputpathは必須です。")

    @staticmethod
    def execute(args):
        with open(args.inputpath, "r") as infile:
            content = infile.read()
        reversed_content = content[::-1]
        with open(args.outputpath, "w") as outfile:
            outfile.write(reversed_content)


class CopyFile(FileManipulator):
    @staticmethod
    def validate_args(args):
        if args.outputpath is None:
            raise ValueError("outputpathは必須です。")

    @staticmethod
    def execute(args):
        with open(args.inputpath, "r") as infile:
            content = infile.read()
        with open(args.outputpath, "w") as outfile:
            outfile.write(content)


class DuplicateContentsFile(FileManipulator):
    @staticmethod
    def validate_args(args):
        if args.duplicate_count is None or args.duplicate_count <= 0:
            raise ValueError("duplicate-countは1以上の整数で指定してください。")

    @staticmethod
    def execute(args):
        with open(args.inputpath, "r") as infile:
            content = infile.read()
        duplicated_content = content * args.duplicate_count
        with open(args.inputpath, "w") as outfile:
            outfile.write(duplicated_content)


class ReplaceStringFile(FileManipulator):
    @staticmethod
    def validate_args(args):
        if args.search_string is None or args.replace_string is None:
            raise ValueError("search-stringとreplace-stringは必須です。")

    @staticmethod
    def execute(args):
        with open(args.inputpath, "r") as infile:
            content = infile.read()
        replaced_content = content.replace(args.search_string, args.replace_string)
        with open(args.inputpath, "w") as outfile:
            outfile.write(replaced_content)


def setting_argument_parser():
    parser = argparse.ArgumentParser(description="File Manipulator")
    parser.add_argument(
        "--operation",
        choices=["reverse", "copy", "duplicate-contents", "replace-string"],
        type=str,
        required=True,
        help="操作の種類を指定します。",
    )

    parser.add_argument(
        "--inputpath", type=str, required=True, help="入力ファイルのパスを指定します。"
    )
    parser.add_argument(
        "--outputpath",
        type=str,
        required=False,
        help="出力ファイルのパスを指定します。",
    )
    parser.add_argument(
        "--duplicate-count",
        type=int,
        required=False,
        help="内容を複製する回数を指定します。",
    )
    parser.add_argument(
        "--search-string",
        type=str,
        required=False,
        help="置換対象の文字列を指定します。",
    )
    parser.add_argument(
        "--replace-string",
        type=str,
        required=False,
        help="置換後の文字列を指定します。",
    )
    return parser


def main():
    parser = setting_argument_parser()
    args = parser.parse_args()
    file_manipulators = {
        "reverse": ReverseFile,
        "copy": CopyFile,
        "duplicate-contents": DuplicateContentsFile,
        "replace-string": ReplaceStringFile,
    }
    manipulator_class = file_manipulators.get(args.operation)
    manipulator_class.validate_args(args)
    manipulator_class.execute(args)
    print(f"{args.operation}操作が完了しました。")


if __name__ == "__main__":
    main()
