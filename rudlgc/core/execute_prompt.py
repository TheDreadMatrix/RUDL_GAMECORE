import argparse
import webbrowser
import yaml

class _RUDLParser(argparse.ArgumentParser):
    def error(self, message):
        print(f"\033[31m{message}\033[0m")
        exit(1)






def _rudlgc_admin():
    parser = _RUDLParser(prog="rudl", description="RUDL Engine ++", formatter_class=argparse.RawTextHelpFormatter)
    sub_parser = parser.add_subparsers(dest="command")

    start_project = sub_parser.add_parser("newproject", help="Creates game project")
    start_project.add_argument("project_name")

    start_scene = sub_parser.add_parser("newscene", help="Creates new game scene")
    start_scene.add_argument("filename")
    start_scene.add_argument("classname")

    clear_cache = sub_parser.add_parser("clearcache", help="After deleting your project, you must clear cache in config to recreate other game")

    telegram_channel = sub_parser.add_parser("tg", help="Open TG channel")
    youtube_channel = sub_parser.add_parser("youtube", help="Open YT channel")
    discord_server = sub_parser.add_parser("discord", help="Open discord server")
    documentation_url = sub_parser.add_parser("docs", help="Open github s documentation repo")



    args = parser.parse_args()
    if args.command == "newproject":
        pass

    elif args.command == "newscene":
        pass

    elif args.command == "clearcache":
        pass

    elif args.command == "tg":
        webbrowser.open_new_tab("https://www.youtube.com/@DaemonDuck16")

    elif args.command == "youtube":
        webbrowser.open_new_tab("https://www.youtube.com/@DaemonDuck16")

    elif args.command == "discord":
        webbrowser.open_new_tab("https://discord.gg/Pzn7yQR9gd")

    elif args.command == "docs":
        webbrowser.open_new_tab("https://github.com/TheDreadMatrix/RUDL-GameCore-Documentation")






def execute_console(execute_now: bool=False):
    if execute_now:
        from rudlgc.core.execute_game import Game
        Game()._Game__run()

    parser = _RUDLParser(prog="rudl", description="RUDL Engine ++", formatter_class=argparse.RawTextHelpFormatter)
    sub_parser = parser.add_subparsers(dest="command")

    run = sub_parser.add_parser("run", help="Running the game")
    build = sub_parser.add_parser("build", help="Building game into EXE")


