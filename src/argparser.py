import argparse


class ArgsParser:
    def __init__(self):
        pass

    @staticmethod
    def args_parser():
        parser = argparse.ArgumentParser()
        parser.add_argument("--excel_schedules", help="excel_schedules", default="../test_datas")
        parser.add_argument("--google_api_credentials_path", help="google_api_credentials_path", default="../resources/credentials.json")
        parser.add_argument("--google_api_token_path", help="google_api_token_path", default="../resources/token.json")
        args = parser.parse_args()
        return args
