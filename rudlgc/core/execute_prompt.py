from pathlib import Path
import argparse
import webbrowser




class _RUDLParser(argparse.ArgumentParser):
    def error(self, message):
        print(f"\033[31m{message}\033[0m")
        exit(1)






def _rudlgc_admin():
    from rudlgc.core.templates_test.templates import _PROHIBITED_WORDS, _EXAMPLE_PY, _ROUTER_PY, _SETTINGS_PY, _MANAGE_PY, is_valid_name, _SCENE_PY

    parser = _RUDLParser(prog="rudl", description="RUDL Engine ++", formatter_class=argparse.RawTextHelpFormatter)
    sub_parser = parser.add_subparsers(dest="command")

    start_project = sub_parser.add_parser("newproject", help="Creates game project")
    start_project.add_argument("project_name")
    

    sub_parser.add_parser("tg", help="Open TG channel")
    sub_parser.add_parser("youtube", help="Open YT channel")
    sub_parser.add_parser("discord", help="Open discord server")
    sub_parser.add_parser("docs", help="Open github s documentation repo")



    args = parser.parse_args()
    if args.command == "newproject":
        #WORKING TO CREATE AND REGISTER DIRECTORY
        if (args.project_name.lower() in _PROHIBITED_WORDS) or (not is_valid_name(args.project_name)):
            parser.error(f"Invalid project name!")
            
        PROJECT_BASE_PATH = Path.cwd() / args.project_name
        if PROJECT_BASE_PATH.exists():
            parser.error(f"Project {args.project_name} already exists!")


        #CREATING ALL FOLDERS AND FILES
        all_folders = ["musics", "sounds", "assets", "fonts", "shaders", ".config", ".saves", "scenes", "utils"]
        for folder in all_folders:
            folder_path = PROJECT_BASE_PATH / folder
            folder_path.mkdir(parents=True, exist_ok=True)

        (PROJECT_BASE_PATH / "__init__.py").write_text("#MODULE FILE")

        for folder in ["utils", "scenes"]:
            code_folder_path = PROJECT_BASE_PATH / folder
            code_folder_path.mkdir(parents=True, exist_ok=True)
            (code_folder_path / "__init__.py").write_text("#SUBMODULE FILE")

        #HERE WE WRITES EXAMPLE CODE
        (PROJECT_BASE_PATH / "scenes" / "example.py").write_text(_EXAMPLE_PY)
        (PROJECT_BASE_PATH / "router.py").write_text(_ROUTER_PY(args.project_name))
        (PROJECT_BASE_PATH / "settings.py").write_text(_SETTINGS_PY(args.project_name))
        (Path.cwd() / f"manage_{args.project_name.lower()}.py").write_text(_MANAGE_PY(args.project_name))

        print("\033[32mProject succesfully created!\033[0m")
        return 1
                
            

    #CONTENT COMMANDS
    elif args.command == "tg":
        webbrowser.open_new_tab("https://www.youtube.com/@DaemonDuck16")

    elif args.command == "youtube":
        webbrowser.open_new_tab("https://www.youtube.com/@DaemonDuck16")

    elif args.command == "discord":
        webbrowser.open_new_tab("https://discord.gg/Pzn7yQR9gd")

    elif args.command == "docs":
        webbrowser.open_new_tab("https://github.com/TheDreadMatrix/RUDL-GameCore-Documentation")






def execute_console(execute_now: bool=False) -> int|None:
    import os
    import importlib
    from rudlgc.core.execute_game import Game
    from rudlgc.core.templates_test.templates import _SCENE_PY, _BUILD_PY, is_valid_name

    if execute_now:
        Game()._Game__run()

    parser = _RUDLParser(prog="rudl", description="RUDL Engine ++", formatter_class=argparse.RawTextHelpFormatter)
    sub_parser = parser.add_subparsers(dest="command")

    #JUST COMMAND
    sub_parser.add_parser("test-health")

    #BASICS COMMAND
    sub_parser.add_parser("run", help="Running the game", aliases=["r", "start", "play"])
    sub_parser.add_parser("build", help="Building game into EXE")
    sub_parser.add_parser("settings", help="Shows list of settings")

    newscene = sub_parser.add_parser("newscene", help="Creates new scene for your project")
    newscene.add_argument("filename")
    newscene.add_argument("classname")


    args = parser.parse_args()

    if args.command == "test-health":
        print("Manage is working very great!")
        return 1
    

    if args.command in ["run", "r", "start", "play"]:
        Game()._Game__run()


    elif args.command == "build":
        pass

    elif args.command == "settings":
        settings_module = importlib.import_module(os.environ.get("RUDLGC_PROJECT_SETTINGS"))
        print("----Settings attributes----")
        for attr in dir(settings_module):
            if attr.isupper():
                print(attr)




    elif args.command == "newscene":
        if not is_valid_name(args.filename):
            parser.error("Invalid filename!")

        if not is_valid_name(args.classname):
            parser.error("Invalid classname!")

        (Path.cwd() / os.environ.get("RUDLGC_PROJECT_NAME") / "scenes" / f"{args.filename}.py").write_text(_SCENE_PY(args.classname))
        print("\033[32mProject scene succesfully created!\033[0m")
        return 1



if __name__ == "__main__":
    _rudlgc_admin()