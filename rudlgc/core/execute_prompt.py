from pathlib import Path
import importlib.resources as res
import argparse
import webbrowser
import yaml




class _RUDLParser(argparse.ArgumentParser):
    def error(self, message):
        print(f"\033[31m{message}\033[0m")
        exit(1)






def _rudlgc_admin():
    from rudlgc.core.templates_test.templates import _PROHIBITED_WORDS, _EXAMPLE_PY, _ROUTER_PY, _SETTINGS_PY, _MANAGE_PY, is_valid_name

    parser = _RUDLParser(prog="rudl", description="RUDL Engine ++", formatter_class=argparse.RawTextHelpFormatter)
    sub_parser = parser.add_subparsers(dest="command")

    start_project = sub_parser.add_parser("newproject", help="Creates game project")
    start_project.add_argument("project_name")

    switch_project = sub_parser.add_parser("setproject", help="Switch active project to another")
    switch_project.add_argument("project_name")

    start_scene = sub_parser.add_parser("newscene", help="Creates new game scene")
    start_scene.add_argument("filename")
    start_scene.add_argument("classname")
    start_scene.add_argument("--project-name", default=None)

    

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

        #BINDING TO CORE CONFIG
        with open(res.files("rudlgc.core").joinpath("config.yaml"), "r") as f:
            data_config = yaml.safe_load(f)

        data_config["project-name"] = args.project_name
                

        with open(res.files("rudlgc.core").joinpath("config.yaml"), "w") as f:
            yaml.dump(data_config, f, sort_keys=False, default_flow_style=False)


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
        (PROJECT_BASE_PATH / "router.py").write_text(_ROUTER_PY)
        (PROJECT_BASE_PATH / "settings.py").write_text(_SETTINGS_PY(args.project_name))
        (Path.cwd() / f"manage_{args.project_name}.py").write_text(_MANAGE_PY(args.project_name))

        print("\033[32mProject succesfully created!\033[0m")
        return 1
                
    
    elif args.command == "setproject":
        #SWITCHING TO PROJECT
        if not (Path.cwd() / args.project_name).exists():
            parser.error(f"Project {args.project_name} does not exists!")

        data_config = {"project-name": args.project_name}
                
        with open(res.files("rudlgc.core").joinpath("config.yaml"), "w") as f:
            yaml.dump(data_config, f, sort_keys=False, default_flow_style=False)
        
        print("\033[32mProject succesfully switched!\033[0m")
        return 1


    elif args.command == "newscene":
        pass

    #CONTENT COMMANDS
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
    settings = sub_parser.add_parser("settings", help="Shows list of settings")



_rudlgc_admin()