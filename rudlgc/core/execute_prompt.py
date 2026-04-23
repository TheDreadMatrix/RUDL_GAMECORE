from pathlib import Path
import argparse
import sys





class _RUDLParser(argparse.ArgumentParser):
    def error(self, message):
        print(f"\033[31m{message}\033[0m")
        exit(1)



def getRudlgcAllModulesParts():
    rudlgc_modules = []
    for module in sys.modules.keys():
        if "rudlgc" in module:
            rudlgc_modules.append(module)

    print(rudlgc_modules)



def _rudlgc_admin():
    import webbrowser
    from rudlgc.core.templates.templates import _PROHIBITED_WORDS, _EXAMPLE_PY, _ROUTER_PY, _SETTINGS_PY, _MANAGE_PY
    from rudlgc.core.templates.functions import is_valid_name

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
        all_folders = ["musics", "sounds", "images", "fonts", "shaders", ".config", ".saves"]
        for folder in all_folders:
            folder_path = PROJECT_BASE_PATH / "assets" / folder
            folder_path.mkdir(parents=True, exist_ok=True)

        (PROJECT_BASE_PATH / "__init__.py").write_text("#MODULE FILE")

        for folder in ["my_utils", "scenes"]:
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






def execute_console() -> int|None:
    import os
    import re
    import json
    import shutil
    import importlib
    import importlib.resources as res
    from rudlgc.core.templates.templates import _SCENE_PY, _BUILD_PY, check_security
    from rudlgc.core.templates.functions import is_valid_name, _group_by_category


    parser = _RUDLParser(prog="rudl", description="RUDL Engine ++", formatter_class=argparse.RawTextHelpFormatter)
    sub_parser = parser.add_subparsers(dest="command")

    #JUST COMMAND
    sub_parser.add_parser("test-health")

    #BASICS COMMAND
    sub_parser.add_parser("run", help="Running the game", aliases=["r", "start", "play"])
    sub_parser.add_parser("build", help="Building game into EXE")
    sub_parser.add_parser("settings", help="Shows list of settings")
    sub_parser.add_parser("collectstuff", help="Copy build-in images to your project for building")

    newscene = sub_parser.add_parser("newscene", help="Creates new scene for your project")
    newscene.add_argument("filename")
    newscene.add_argument("classname")


    args = parser.parse_args()

    if args.command == "test-health":
        check_security(parser)
        print("\033[32mManage is working very great!\033[0m")
        return 1
    

    if args.command in ["run", "r", "start", "play"]:
        from rudlgc.core.execute_game import Game
        game = Game()
        if game.settings.DEBUG:
            game.logger._system_log("WARNING", "DEBUG mode is enabled")
            game._connectDebugServer()
        game._initGame()
        game._run()
        return 1



    elif args.command == "settings":
        from rudlgc.core.subsystems import SettingsCore
        from rudlgc.core import _getOs

        CATEGORY = {
            "_PROHIBITED": ["OS_PLATFORM"],

            "WINDOW-SIZES": ["WINDOW_WIDTH", "WINDOW_HEIGHT", "WINDOW_MINWIDTH", "WINDOW_MINHEIGHT"],

            "WINDOW-ATTR": ["FULLSCREEN", "BORDERLESS", "RESIZABLE", "VSYNC"],

            "GAME-META": ["GAME_METADATA"],

            "DEBUG": ["DEBUG", "SHOW_INFO"],

            "STARTUP": ["FPS", "START_SCENE"],

            "AUDIO": ["MUSIC_VOLUME", "SOUND_VOLUME"],

            "CROSS-PLATFORM": ["OS_PLATFORM"],

            "RENDER-ATTR": ["LINE_SIZE", "POINT_SIZE"]
        } 
        
        settings_module = importlib.import_module(os.environ.get("RUDLGC_PROJECT_SETTINGS"))
        
        defaults = []
        defaults_not_dec = []
        custom = []

        for attr in SettingsCore._DEFAULTS:
            if attr not in dir(settings_module):
                defaults_not_dec.append((attr, SettingsCore._DEFAULTS.get(attr)))


        for attr in dir(settings_module):
            if attr.startswith("__"):
                continue

            if attr in SettingsCore._DEFAULTS:
                default_value = getattr(settings_module, attr)
                defaults.append((attr, default_value if attr not in CATEGORY["_PROHIBITED"] else _getOs()))
                continue

            if re.fullmatch(r"[A-Z_]+", attr):
                custom_value = getattr(settings_module, attr)
                custom.append((attr, custom_value))

        print("\033[33m==== SETTINGS ====\033[0m")

        if defaults:
            print("\n\033[33m[BUILT-IN]\033[0m")

            grouped = _group_by_category(defaults, CATEGORY)

            for group in sorted(grouped):
                print(f"\n\033[36m  •[{group}]\033[0m")

                for name, value in sorted(grouped[group]):
                    value_str = (json.dumps(value, indent=4, ensure_ascii=False) if isinstance(value, dict) else str(value))
                    print(f"\t\033[33m  • {name} - {value_str}\033[0m")

        
        if defaults_not_dec:
            print("\n\033[33m[NOT DECLARATED BUILD-IN]\033[0m")

            grouped = _group_by_category(defaults_not_dec, CATEGORY)

            for group in sorted(grouped):
                print(f"\n\033[36m  •[{group}]\033[0m")

                for name, value in sorted(grouped[group]):
                    value_str = (json.dumps(value, indent=2, ensure_ascii=False) if isinstance(value, dict) else str(value))
                    print(f"\t\033[33m  • {name} - {value_str}\033[0m")

        if custom:
            CUSTOM_CATEGORY = getattr(settings_module, "__CUSTOM_CATEGORY", {})
            
            print("\n\033[33m[CUSTOM]\033[0m")
            if not CUSTOM_CATEGORY:
                for name, value in sorted(custom):
                    print(f"\033[33m  • {name} - {value}\033[0m")
            else:
                grouped = _group_by_category(custom, CUSTOM_CATEGORY)
                for group in sorted(grouped):
                    print(f"\n\033[36m  *[{group}]\033[0m")

                    for name, value in sorted(grouped[group]):
                        value_str = (json.dumps(value, indent=4, ensure_ascii=False) if isinstance(value, dict) else str(value))
                        print(f"\t\033[33m  • {name} - {value_str}\033[0m")
        return 1
    
    
    elif args.command == "newscene":
        if not is_valid_name(args.filename):
            parser.error("Invalid filename!")

        if not is_valid_name(args.classname):
            parser.error("Invalid classname!")

        (Path.cwd() / os.environ.get("RUDLGC_PROJECT_NAME") / "scenes" / f"{args.filename}.py").write_text(_SCENE_PY(args.classname))
        print("\033[32mProject scene succesfully created!\033[0m")
        return 1



    elif args.command == "collectstuff":
        
        src_image = res.files("rudlgc") / "stuff"
        dst_image = Path.cwd() / os.environ.get("RUDLGC_PROJECT_NAME") / "assets" / "stuff"
        shutil.copytree(src_image, dst_image, dirs_exist_ok=True)

        print("\033[32mAdmin stuff succesfully copied to your dirs!\033[0m")
        return 1

    elif args.command == "build":
        check_security(parser)
        print("That command not working yet...")
        return 0
    
        # 1. Create file start build.py
        # 2. Uses Game core for creating propety game
        # 3. Creating version.txt 
        # 4. Building to exe create APP-FOLDER and dekstop icon
        # rudlgc-build/
        #       pre_build.py
        #       version.txt
        #       build.py
        #       post_build.py
        # 
        # build-game/MyGame.exe



    



if __name__ == "__main__":
    _rudlgc_admin()