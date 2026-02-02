import argparse
import markdown


def get_argument_parser():
    parser = argparse.ArgumentParser(description="File Converter")
    parser.add_argument(
        "--inputpath", type=str, required=True, help="入力ファイルのパスを指定します。"
    )
    parser.add_argument(
        "--outputpath", type=str, required=True, help="出力ファイルのパスを指定します。"
    )
    parser.add_argument(
        "--command",
        choices=["markdown"],
        type=str,
        required=True,
        help="変換後のファイル形式を指定します。",
    )
    return parser

def convert_markdown(input_path, output_path):
    with open(input_path, "r") as infile:
        content = infile.read()
    
    html_content = markdown.markdown(content)
    with open(output_path, "w") as outfile:
        outfile.write(html_content)


def main():
    parser = get_argument_parser()
    args = parser.parse_args()
    if args.command == "markdown":
        convert_markdown(args.inputpath, args.outputpath)
    


if __name__ == "__main__":
    main()
