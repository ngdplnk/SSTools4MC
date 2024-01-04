### SSTools4MC v2.0.0 ###
# SSTools4MC is a program that allows you to manage your Minecraft Server easily.
# Made by: @ngdplnk
# Github: https://github.com/NGDPLNk/SSTools4MC

#######################

### THINGS TO FIX ###
## START SERVER MENU
# - Fix console window not working properly
# - Fix command line not working properly
# - Fix "Stop Server" button not working properly
##################################################
### THINGS TO ADD ###
## License and Extras menu
# - Add more themes (maybe v2.1 update)
#########

import subprocess
import time
import tkinter as tk
import webbrowser
import os
import threading
import requests
import datetime
import ctypes

# Global variables
global running
global run
global props

# Conditional variables
running = False
run = False
props = os.path.join(os.path.dirname(os.getcwd()), "server.properties")

# Debug Mode selection
def sstdebug_mode(rt=False):
  global enabled_debug
  global appdata_path
  global sstools_folder_path
  global cfg_access
  appdata_path = os.getenv("APPDATA")
  sstools_folder_path = os.path.join(appdata_path, "SSTools4MC") # type: ignore
  cfg_access = os.path.join(sstools_folder_path, "sst.cfg")
  cfg = {}
  if not rt:
    if os.path.exists(sstools_folder_path):
      if os.path.exists(cfg_access):
        with open(cfg_access, 'r') as file:
          for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
              key, value = line.split('=')
              cfg[key.strip()] = value.strip()
        try:
          if cfg["debug"] == "true":
            enabled_debug = True
            theme()
          elif cfg["debug"] == "false":
            enabled_debug = False
            theme()
          else:
            cfg["debug"] = "false"
            with open(cfg_access, 'w') as file:
              for key, value in cfg.items():
                file.write(f'{key}={value}\n')
            enabled_debug = False
            theme()
        except KeyError:
          cfg["debug"] = "false"
          with open(cfg_access, 'w') as file:
            for key, value in cfg.items():
              file.write(f'{key}={value}\n')
          enabled_debug = False
          theme()
      else:
        with open(cfg_access, 'w') as archivo:
          archivo.write('debug=false\n')
        theme()
    else:
      os.makedirs(sstools_folder_path)
      with open(cfg_access, 'w') as archivo:
        archivo.write('debug=false\n')
      theme()
  else:
    if os.path.exists(sstools_folder_path):
      if os.path.exists(cfg_access):
        with open(cfg_access, 'r') as file:
          for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
              key, value = line.split('=')
              cfg[key.strip()] = value.strip()
        try:
          if cfg["debug"] == "false":
            return "Enable Debug Mode"
          elif cfg["debug"] == "true":
            return "Disable Debug Mode"
          else:
            return "Enable Debug Mode"
        except KeyError:
          cfg["debug"] = "false"
          with open(cfg_access, 'w') as file:
            for key, value in cfg.items():
              file.write(f'{key}={value}\n')
          return "Enable Debug Mode"
      else:
        with open(cfg_access, 'w') as archivo:
          archivo.write('debug=false\n')
        sstdebug_mode(rt=True)
    else:
      os.makedirs(sstools_folder_path)
      with open(cfg_access, 'w') as archivo:
        archivo.write('debug=false\n')
      sstdebug_mode(rt=True)

# Theme selection
def theme(rt=False):
  global bg_color
  global button_color
  global buttontxt_color
  global text_color
  global appdata_path
  global sstools_folder_path
  global cfg_access
  appdata_path = os.getenv("APPDATA")
  sstools_folder_path = os.path.join(appdata_path, "SSTools4MC") # type: ignore
  cfg_access = os.path.join(sstools_folder_path, "sst.cfg")
  cfg = {}
  if not rt:
    if os.path.exists(sstools_folder_path):
      if os.path.exists(cfg_access):
        with open(cfg_access, 'r') as file:
          for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
              key, value = line.split('=')
              cfg[key.strip()] = value.strip()
        try:
          if cfg["theme"] == "dark":
            bg_color = "#1A1A1A"  # rgb(26, 26, 26)
            button_color = "#D3D3D3"  # rgb(211, 211, 211)
            buttontxt_color = "#1A1A1A"  # rgb(26, 26, 26)
            text_color = "white"  # White
            main()
          elif cfg["theme"] == "light":
            bg_color = "white"  # White
            button_color = "white"  # White
            buttontxt_color = "black"  # Black
            text_color = "black"  # Black
            main()
          else:
            cfg["theme"] = "dark"
            with open(cfg_access, 'w') as file:
              for key, value in cfg.items():
                file.write(f'{key}={value}\n')
            bg_color = "#1A1A1A"  # rgb(26, 26, 26)
            button_color = "#D3D3D3"  # rgb(211, 211, 211)
            buttontxt_color = "#1A1A1A"  # rgb(26, 26, 26)
            text_color = "white"  # White
            main()
        except KeyError:
          cfg["theme"] = "dark"
          with open(cfg_access, 'w') as file:
            for key, value in cfg.items():
              file.write(f'{key}={value}\n')
          bg_color = "#1A1A1A"  # rgb(26, 26, 26)
          button_color = "#D3D3D3"
          buttontxt_color = "#1A1A1A"
          text_color = "white"
          main()
      else:
        with open(cfg_access, 'w') as archivo:
          archivo.write('theme=dark\n')
        theme()
    else:
      os.makedirs(sstools_folder_path)
      with open(cfg_access, 'w') as archivo:
        archivo.write('theme=dark\n')
      theme()
  else:
    if os.path.exists(sstools_folder_path):
      if os.path.exists(cfg_access):
        with open(cfg_access, 'r') as file:
          for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
              key, value = line.split('=')
              cfg[key.strip()] = value.strip()
        try:
          if cfg["theme"] == "dark":
            return "Light"
          elif cfg["theme"] == "light":
            return "Dark"
          else:
            return "Dark"
        except KeyError:
          cfg["theme"] = "dark"
          with open(cfg_access, 'w') as file:
            for key, value in cfg.items():
              file.write(f'{key}={value}\n')
          return "Dark"
      else:
        with open(cfg_access, 'w') as archivo:
          archivo.write('theme=dark\n')
        theme(rt=True)
    else:
      os.makedirs(sstools_folder_path)
      with open(cfg_access, 'w') as archivo:
        archivo.write('theme=dark\n')
      theme(rt=True)

# Check if fullscreen is enabled
def fullscreen():
  global appdata_path
  global sstools_folder_path
  global cfg_access
  appdata_path = os.getenv("APPDATA")
  sstools_folder_path = os.path.join(appdata_path, "SSTools4MC") # type: ignore
  cfg_access = os.path.join(sstools_folder_path, "sst.cfg")
  cfg = {}
  if os.path.exists(sstools_folder_path):
    if os.path.exists(cfg_access):
      with open(cfg_access, 'r') as file:
        for line in file:
          line = line.strip()
          if line and not line.startswith('#'):
            key, value = line.split('=')
            cfg[key.strip()] = value.strip()
      try:
        if cfg["fullscreen"] == "true":
          return True
        elif cfg["fullscreen"] == "false":
          return False
        else:
          cfg["fullscreen"] = "false"
          with open(cfg_access, 'w') as file:
            for key, value in cfg.items():
              file.write(f'{key}={value}\n')
          return False
      except KeyError:
        cfg["fullscreen"] = "false"
        with open(cfg_access, 'w') as file:
          for key, value in cfg.items():
            file.write(f'{key}={value}\n')
        return False
    else:
      with open(cfg_access, 'w') as archivo:
        archivo.write('fullscreen=false\n')
      fullscreen()
  else:
    os.makedirs(sstools_folder_path)
    with open(cfg_access, 'w') as archivo:
      archivo.write('fullscreen=false\n')
    fullscreen()

# Check last ram type used
def last_ramtype():
  global appdata_path
  global sstools_folder_path
  global cfg_access
  appdata_path = os.getenv("APPDATA")
  sstools_folder_path = os.path.join(appdata_path, "SSTools4MC") # type: ignore
  cfg_access = os.path.join(sstools_folder_path, "sst.cfg")
  cfg = {}
  if os.path.exists(sstools_folder_path):
    if os.path.exists(cfg_access):
      with open(cfg_access, 'r') as file:
        for line in file:
          line = line.strip()
          if line and not line.startswith('#'):
            key, value = line.split('=')
            cfg[key.strip()] = value.strip()
      try:
        if cfg["ramtype"] == "MB":
          return "MB"
        else:
          return "GB"
      except KeyError:
        cfg["ramtype"] = "GB"
        with open(cfg_access, 'w') as file:
          for key, value in cfg.items():
            file.write(f'{key}={value}\n')
        return "GB"
    else:
      with open(cfg_access, 'w') as archivo:
        archivo.write('ramtype=GB\n')
      last_ramtype()
  else:
    os.makedirs(sstools_folder_path)
    with open(cfg_access, 'w') as archivo:
      archivo.write('ramtype=GB\n')
    last_ramtype()

# Check last ram used
def last_ram():
  global appdata_path
  global sstools_folder_path
  global cfg_access
  appdata_path = os.getenv("APPDATA")
  sstools_folder_path = os.path.join(appdata_path, "SSTools4MC") # type: ignore
  cfg_access = os.path.join(sstools_folder_path, "sst.cfg")
  cfg = {}
  if os.path.exists(sstools_folder_path):
    if os.path.exists(cfg_access):
      with open(cfg_access, 'r') as file:
        for line in file:
          line = line.strip()
          if line and not line.startswith('#'):
            key, value = line.split('=')
            cfg[key.strip()] = value.strip()
      try:
        if last_ramtype() == "GB":
          if 0 < int(cfg["ram"]) <= 75:
            return cfg["ram"]
          else:
            cfg["ram"] = "1"
            with open(cfg_access, 'w') as file:
              for key, value in cfg.items():
                file.write(f'{key}={value}\n')
            return "1"
        else:
          if 842 <= int(cfg["ram"]) <= 76800:
            return cfg["ram"]
          else:
            cfg["ram"] = "1024"
            with open(cfg_access, 'w') as file:
              for key, value in cfg.items():
                file.write(f'{key}={value}\n')
            return "1024"
      except (KeyError, ValueError):
        if last_ramtype() == "GB":
          cfg["ram"] = "1"
          with open(cfg_access, 'w') as file:
            for key, value in cfg.items():
              file.write(f'{key}={value}\n')
          return "1"
        else:
          cfg["ram"] = "1024"
          with open(cfg_access, 'w') as file:
            for key, value in cfg.items():
              file.write(f'{key}={value}\n')
          return "1024"
    else:
      if last_ramtype() == "GB":
        with open(cfg_access, 'w') as archivo:
          archivo.write('ram=1\n')
        last_ram()
      else:
        with open(cfg_access, 'w') as archivo:
          archivo.write('ram=1024\n')
        last_ram()
  else:
    os.makedirs(sstools_folder_path)
    with open(cfg_access, 'w') as archivo:
      archivo.write('ram=1\n')
    last_ram()

# START SERVER MENU
def startserver_menu():
  global ramtype_var
  global ram_var
  global public_ip
  global server_port
  global minecraft_server_process
  global raam
  global ramtypee
  global run

  if run and minecraft_server_process.stdin:
    # Clear the window
      for widget in root.winfo_children():
        widget.destroy()

      # Main frame
      frame = tk.Frame(root, bg=bg_color)
      frame.place(relx=0.5, rely=0.5, anchor='center')

      # Title
      title_font = ("Arial", 30, "bold")
      title = tk.Label(frame, text=f"Server Running with {raam}{ramtypee}B of RAM", font=title_font, bg=bg_color, fg=text_color)
      title.grid(row=0, column=0, columnspan=4, pady=5)

      # Subtitle
      subtitle_text = "Your Server is running on a separated Terminal. Its status updates here every 1 minute\n"
      subtitle = tk.Label(frame, text=subtitle_text, font=("Arial", 12), wraplength=600, bg=bg_color, fg=text_color)
      subtitle.grid(row=1, column=0, columnspan=4, pady=5)

      # Get server IP
      def get_public_ip():
        try:
          ip = requests.get('https://api.ipify.org').text
        except requests.exceptions.RequestException as err:
          print ("Woops: Something Else Happened",err)
          ip = "Your Public IP"
        return ip
      public_ip = get_public_ip()

      # Get server port
      def get_port():
        global props
        properties = {}
        if not os.path.exists(props):
          return ""
        with open(props, 'r') as file:
          for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
              key, value = line.split('=')
              properties[key.strip()] = value.strip()
        try:
          port = properties["server-port"]
          if port == "25565":
            return ""
        except KeyError:
          return ""
        return f":{port}"
      server_port = get_port()

      # IP label
      ip_label = tk.Label(frame, text=f"Your Server IP is: {public_ip}{server_port}", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
      ip_label.grid(row=2, column=1, pady=5, sticky='e')

      # Copy IP to clipboard
      def copy_ip():
        global public_ip
        global server_port
        root.clipboard_clear()
        root.clipboard_append(f"{public_ip}{server_port}")
        
      # "Copy IP" button
      copy_button = tk.Button(frame, text="Copy IP", command=copy_ip, height=1, width=8, bg=button_color, fg=buttontxt_color)
      copy_button.grid(row=2, column=2, pady=5, padx=10, sticky='w')

      # "Your Server has been running for" label
      running_label = tk.Label(frame, text="Your Server has been running for", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
      running_label.grid(row=3, column=1, pady=5, sticky='e')

      # Time Running
      def time_running():
        global run
        global elapsed_minutes
        global elapsed_time
        global minecraft_server_process
        if run and minecraft_server_process.stdin:
          global start_time
          elapsed_time = time.time() - start_time
          elapsed_minutes = int(elapsed_time // 60)
          running_time.config(text=f"{elapsed_minutes} minutes")
          running_time.after(60000, time_running)  # Update every minute
        else:
          return

      # Time Running Label
      running_time = tk.Label(frame, text="0 minutes", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
      running_time.grid(row=3, column=2, pady=5, sticky='w')
      time_running()

      # Stop Server
      def stop_server():
        global run
        global minecraft_server_process
        if minecraft_server_process.stdin:
          command = "stop\n"
          minecraft_server_process.stdin.write(command.encode())
          minecraft_server_process.stdin.flush()
        run = False
        dnh_sys = datetime.datetime.now()
        stop_date = str(dnh_sys.strftime("%d/%m/%Y"))
        stop_hour = str(dnh_sys.strftime("%H:%M:%S"))

        # Clear the window
        for widget in root.winfo_children():
          widget.destroy()
        
        # Window title
        root.title("Server Stopped")

        # Main frame
        frame = tk.Frame(root, bg=bg_color)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        # Title
        title_font = ("Arial", 30, "bold")
        title = tk.Label(frame, text="Server Stopped", font=title_font, bg=bg_color, fg=text_color)
        title.grid(row=0, column=0, columnspan=4, pady=5)

        # Subtitle
        subtitle_text = "Server Stopped...\n"
        subtitle = tk.Label(frame, text=subtitle_text, font=("Arial", 12), wraplength=600, bg=bg_color, fg=text_color)
        subtitle.grid(row=1, column=0, columnspan=4, pady=5)

        # "Your Server has been closed at <close_time>" label
        close_label = tk.Label(frame, text=f"Your Server has been closed on {stop_date} at {stop_hour}\n\nYou can check the console log in the 'logs' folder.\n", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
        close_label.grid(row=2, column=0, columnspan=4, pady=5)

        # "Return to Main Menu" button
        main_button = tk.Button(frame, text="Return to Main Menu", command=main, height=2, width=30, bg=button_color, fg=buttontxt_color)
        main_button.grid(row=3, column=0, columnspan=4, pady=15, sticky="nsew")
      
      def check_process():
        global run
        global minecraft_server_process
        while run:
          if minecraft_server_process.poll() is not None:
            # The process has terminated
            run = False
            stop_server()
            break
          time.sleep(60)  # Wait for 1 minute

      # "Stop Server" Button
      stop_server_button = tk.Button(frame, text="STOP SERVER", command=stop_server, height=3, width=20, bg="red", fg="white")
      stop_server_button.grid(row=4, column=0, columnspan=4, pady=15, sticky='nsew')
      threading.Thread(target=check_process).start()

      # "Main Menu" Button
      main_button = tk.Button(frame, text="Return to Main Menu", command=main, height=2, width=30, bg=button_color, fg=buttontxt_color)
      main_button.grid(row=5, column=0, columnspan=4, pady=15, sticky="nsew")
  else:
    def validate_input(P):
      ram_type = last_ramtype()
      if P.isdigit():
        P = int(P)
        if (ram_type == "GB" and 1 <= P <= 99) or (ram_type == "MB" and 1 <= P <= 99999):
          return True
      elif P == "":
        return True
      return False

    # Clears the window
    for widget in root.winfo_children():
      widget.destroy()

    # Window title
    root.title("Start Server")

    # Set BG
    root.configure(bg=bg_color)

    # Main frame
    frame = tk.Frame(root, bg=bg_color)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    # Title
    title_font = ("Arial", 30, "bold")
    title = tk.Label(frame, text="Start Server", font=title_font, bg=bg_color, fg=text_color)
    title.grid(row=0, column=0, columnspan=4, pady=5)

    # Subtitle
    subtitle_text = "Be prepared to start your server!\n"
    subtitle = tk.Label(frame, text=subtitle_text, font=("Arial", 12), wraplength=600, bg=bg_color, fg=text_color)
    subtitle.grid(row=1, column=0, columnspan=4, pady=5)

    # "Start Server with" label
    startserver_label = tk.Label(frame, text="Start Server with", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
    startserver_label.grid(row=2, column=0, pady=5, sticky='e')

    # RAM Entry and Dropdown
    ram_var = tk.StringVar(value=last_ram())
    ramtype_var = tk.StringVar(value=last_ramtype())

    vcmd = frame.register(validate_input)

    ram_entry = tk.Entry(frame, textvariable=ram_var, validate="key", validatecommand=(vcmd, '%P'), width=6)
    ram_entry.grid(row=2, column=1, padx=5, pady=5)

    # RAM Type Change
    def ram_change(*args):
      cfg = {}
      if os.path.exists(sstools_folder_path):
        if os.path.exists(cfg_access):
          with open(cfg_access, 'r') as file:
            for line in file:
              line = line.strip()
              if line and not line.startswith('#'):
                key, value = line.split('=')
                cfg[key.strip()] = value.strip()
          try:
            cfg["ramtype"] = ramtype_var.get()
            with open(cfg_access, 'w') as file:
              for key, value in cfg.items():
                file.write(f'{key}={value}\n')
            startserver_menu()
          except KeyError:
            cfg["ramtype"] = "GB"
            with open(cfg_access, 'w') as file:
              for key, value in cfg.items():
                file.write(f'{key}={value}\n')
            startserver_menu()
        else:
          with open(cfg_access, 'w') as archivo:
            archivo.write('ramtype=GB\n')
          startserver_menu()
      else:
        os.makedirs(sstools_folder_path)
        with open(cfg_access, 'w') as archivo:
          archivo.write('ramtype=GB\n')
        startserver_menu()

    ramtype_var.trace_add('write', ram_change)

    ramtype_dropdown = tk.OptionMenu(frame, ramtype_var, "MB", "GB")
    ramtype_dropdown.grid(row=2, column=2, padx=5, pady=5)

    # "of RAM" label
    ram_label = tk.Label(frame, text="of RAM", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
    ram_label.grid(row=2, column=3, pady=5, sticky='w')

    def start_server():
      global ramtype_var
      global ram_var
      cfg = {}
      with open(cfg_access, 'r') as file:
        for line in file:
          line = line.strip()
          if line and not line.startswith('#'):
            key, value = line.split('=')
            cfg[key.strip()] = value.strip()
      try:
        if ramtype_var.get() == "MB":
          if ram_var.get() == "":
            ram_var.set("1024")
            cfg["ram"] = "1024"
            with open(cfg_access, 'w') as file:
              for key, value in cfg.items():
                file.write(f'{key}={value}\n')
          elif 842 <= int(ram_var.get()) <= 76800:
            cfg["ram"] = ram_var.get()
            with open(cfg_access, 'w') as file:
              for key, value in cfg.items():
                file.write(f'{key}={value}\n')
          else:
            ram_var.set("1024")
            cfg["ram"] = "1024"
            with open(cfg_access, 'w') as file:
              for key, value in cfg.items():
                file.write(f'{key}={value}\n')
        else:
          if ram_var.get() == "":
            ram_var.set("1")
            cfg["ram"] = "1"
            with open(cfg_access, 'w') as file:
              for key, value in cfg.items():
                file.write(f'{key}={value}\n')
          elif 0 < int(ram_var.get()) <= 75:
            cfg["ram"] = ram_var.get()
            with open(cfg_access, 'w') as file:
              for key, value in cfg.items():
                file.write(f'{key}={value}\n')
          else:
            ram_var.set("1")
            cfg["ram"] = "1"
            with open(cfg_access, 'w') as file:
              for key, value in cfg.items():
                file.write(f'{key}={value}\n')
      except (ValueError, KeyError):
        if ramtype_var.get() == "GB":
          ram_var.set("1")
          cfg["ram"] = "1"
          with open(cfg_access, 'w') as file:
            for key, value in cfg.items():
              file.write(f'{key}={value}\n')
        else:
          ram_var.set("1024")
          cfg["ram"] = "1024"
          with open(cfg_access, 'w') as file:
            for key, value in cfg.items():
              file.write(f'{key}={value}\n')

      # Set window title
      root.title("Server Running...")
      # Check if server.jar exists
      if not os.path.exists(os.path.join(os.path.dirname(os.getcwd()), "server.jar")):
        # Clear the window
        for widget in root.winfo_children():
          widget.destroy()

        # Window title
        root.title("Can't Start your Server")

        # Main frame
        frame = tk.Frame(root, bg=bg_color)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        # Title
        title_font = ("Arial", 30, "bold")
        title = tk.Label(frame, text="Can't Start your Server", font=title_font, bg=bg_color, fg=text_color)
        title.grid(row=0, column=0, columnspan=4, pady=5)

        # Subtitle
        subtitle_text = 'Uh oh, "server.jar" file not found :(\n'
        subtitle = tk.Label(frame, text=subtitle_text, font=("Arial", 12), wraplength=600, bg=bg_color, fg=text_color)
        subtitle.grid(row=1, column=0, columnspan=4, pady=5)

        # "Return to Main Menu" button
        main_button = tk.Button(frame, text="Return to Main Menu", command=main, height=2, width=30, bg=button_color, fg=buttontxt_color)
        main_button.grid(row=2, column=0, columnspan=4, pady=15, sticky="nsew")
        return
      else:
        global run
        global start_time
        global minecraft_server_process
        global public_ip
        global server_port
        global raam
        global ramtypee

        # Initialize variables
        run = True
        start_time = time.time()
        ram = ram_var.get()
        ramtype = ramtype_var.get()

        if ramtype == "MB":
          ramtypee = "M"
          if ram == "":
            raam = "1024"
          elif int(ram) > 76800:
            raam = "76800"
          elif int(ram) < 842:
            raam = "842"
          else:
            raam = ram
        else:
          ramtypee = "G"
          if ram == "":
            raam = "1"
          if int(ram) > 75:
            raam = "75"
          elif int(ram) < 1:
            raam = "1"
          else:
            raam = ram

        # Accept EULA
        with open(os.path.join(os.path.dirname(os.getcwd()), "eula.txt"), 'w') as file:
          file.write("eula=true\n")

        # Start the server
        command = f"java -Xmx{raam}{ramtypee} -Xms{raam}{ramtypee} -jar server.jar nogui"
        minecraft_server_process = subprocess.Popen(command, cwd=os.path.dirname(os.getcwd()), stdin=subprocess.PIPE)

        # Detach the console
        ctypes.windll.kernel32.FreeConsole()

        # Clear the window
        for widget in root.winfo_children():
          widget.destroy()

        # Main frame
        frame = tk.Frame(root, bg=bg_color)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        # Title
        title_font = ("Arial", 30, "bold")
        title = tk.Label(frame, text=f"Server Running with {raam}{ramtypee}B of RAM", font=title_font, bg=bg_color, fg=text_color)
        title.grid(row=0, column=0, columnspan=4, pady=5)

        # Subtitle
        subtitle_text = "Your Server is running on a separated Terminal. Its status updates here every 1 minute\n"
        subtitle = tk.Label(frame, text=subtitle_text, font=("Arial", 12), wraplength=600, bg=bg_color, fg=text_color)
        subtitle.grid(row=1, column=0, columnspan=4, pady=5)

        # Get server IP
        def get_public_ip():
          try:
            ip = requests.get('https://api.ipify.org').text
          except requests.exceptions.RequestException as err:
            print ("Woops: Something Else Happened",err)
            ip = "Your Public IP"
          return ip
        public_ip = get_public_ip()

        # Get server port
        def get_port():
          global props
          properties = {}
          if not os.path.exists(props):
            return ""
          with open(props, 'r') as file:
            for line in file:
              line = line.strip()
              if line and not line.startswith('#'):
                key, value = line.split('=')
                properties[key.strip()] = value.strip()
          try:
            port = properties["server-port"]
            if port == "25565":
              return ""
          except KeyError:
            return ""
          return f":{port}"
        server_port = get_port()

        # IP label
        ip_label = tk.Label(frame, text=f"Your Server IP is: {public_ip}{server_port}", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
        ip_label.grid(row=2, column=1, pady=5, sticky='e')

        # Copy IP to clipboard
        def copy_ip():
          global public_ip
          global server_port
          root.clipboard_clear()
          root.clipboard_append(f"{public_ip}{server_port}")
        
        # "Copy IP" button
        copy_button = tk.Button(frame, text="Copy IP", command=copy_ip, height=1, width=8, bg=button_color, fg=buttontxt_color)
        copy_button.grid(row=2, column=2, pady=5, padx=10, sticky='w')

        # "Your Server has been running for" label
        running_label = tk.Label(frame, text="Your Server has been running for", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
        running_label.grid(row=3, column=1, pady=5, sticky='e')

        # Time Running
        def time_running():
          global run
          global elapsed_minutes
          global elapsed_time
          global minecraft_server_process
          if run and minecraft_server_process.stdin:
            global start_time
            elapsed_time = time.time() - start_time
            elapsed_minutes = int(elapsed_time // 60)
            running_time.config(text=f"{elapsed_minutes} minutes")
            running_time.after(60000, time_running)  # Update every minute
          else:
            return

        # Time Running Label
        running_time = tk.Label(frame, text="0 minutes", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
        running_time.grid(row=3, column=2, pady=5, sticky='w')
        time_running()

        # Stop Server
        def stop_server():
          global run
          global minecraft_server_process
          if run and minecraft_server_process.stdin:
            command = "stop\n"
            minecraft_server_process.stdin.write(command.encode())
            minecraft_server_process.stdin.flush()
          run = False
          dnh_sys = datetime.datetime.now()
          stop_date = str(dnh_sys.strftime("%d/%m/%Y"))
          stop_hour = str(dnh_sys.strftime("%H:%M:%S"))

          # Clear the window
          for widget in root.winfo_children():
            widget.destroy()
          
          # Window title
          root.title("Server Stopped")

          # Main frame
          frame = tk.Frame(root, bg=bg_color)
          frame.place(relx=0.5, rely=0.5, anchor='center')

          # Title
          title_font = ("Arial", 30, "bold")
          title = tk.Label(frame, text="Server Stopped", font=title_font, bg=bg_color, fg=text_color)
          title.grid(row=0, column=0, columnspan=4, pady=5)

          # Subtitle
          subtitle_text = "Server Stopped...\n"
          subtitle = tk.Label(frame, text=subtitle_text, font=("Arial", 12), wraplength=600, bg=bg_color, fg=text_color)
          subtitle.grid(row=1, column=0, columnspan=4, pady=5)

          # "Your Server has been closed at <close_time>" label
          close_label = tk.Label(frame, text=f"Your Server has been closed on {stop_date} at {stop_hour}\n\nYou can check the console log in the 'logs' folder.\n", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
          close_label.grid(row=2, column=0, columnspan=4, pady=5)

          # "Return to Main Menu" button
          main_button = tk.Button(frame, text="Return to Main Menu", command=main, height=2, width=30, bg=button_color, fg=buttontxt_color)
          main_button.grid(row=3, column=0, columnspan=4, pady=15, sticky="nsew")
        
        def check_process():
          global run
          global minecraft_server_process
          while run:
            if not minecraft_server_process.stdin:
              # The process has terminated
              run = False
              stop_server()
              break
            time.sleep(60)  # Wait for 1 minute

        # "Stop Server" Button
        stop_server_button = tk.Button(frame, text="STOP SERVER", command=stop_server, height=3, width=20, bg="red", fg="white")
        stop_server_button.grid(row=4, column=0, columnspan=4, pady=15, sticky='nsew')
        threading.Thread(target=check_process).start()

        # "Main Menu" Button
        main_button = tk.Button(frame, text="Return to Main Menu", command=main, height=2, width=30, bg=button_color, fg=buttontxt_color)
        main_button.grid(row=5, column=0, columnspan=4, pady=15, sticky="nsew")
  
    # "Start Server" button
    start_button = tk.Button(frame, text="START SERVER", command=start_server, height=3, width=20, bg="green", fg="white")
    start_button.grid(row=3, column=0, columnspan=4, pady=5, sticky='nsew')

    # "Manage Server" button
    manage_button = tk.Button(frame, text="Manage Server", command=manageserver_menu, height=2, width=30, bg="blue", fg="white")
    manage_button.grid(row=4, column=0, columnspan=4, pady=5, sticky='nsew')

    # "Return to Main Menu" button
    main_button = tk.Button(frame, text="Return to Main Menu", command=main, height=2, width=30, bg=button_color, fg=buttontxt_color)
    main_button.grid(row=5, column=0, columnspan=4, pady=15, sticky="nsew")

# MANAGE SERVER MENU
def manageserver_menu():
  global props
  # Clears the window
  for widget in root.winfo_children():
    widget.destroy()

  # Window title
  root.title("Server Management")

  # Set BG
  root.configure(bg=bg_color)

  # Main frame
  frame = tk.Frame(root, bg=bg_color)
  frame.place(relx=0.5, rely=0.5, anchor='center')

  # Title
  title_font = ("Arial", 30, "bold")
  title = tk.Label(frame, text="Server Management", font=title_font, bg=bg_color, fg=text_color)
  title.grid(row=0, column=0, columnspan=5, pady=5)

  # Check if server.properties exists
  props = os.path.join(os.path.dirname(os.getcwd()), "server.properties")
  if os.path.exists(props):
    global properties
    properties = {}
    with open(props, 'r') as file:
      for line in file:
        line = line.strip()
        if line and not line.startswith('#'):
          key, value = line.split('=')
          properties[key.strip()] = value.strip()
    
    # Subtitle
    subtitle_text = "Welcome to the server management menu\nThese settings will apply the next time you start your server\n"
    subtitle = tk.Label(frame, text=subtitle_text, font=("Arial", 12), wraplength=600, bg=bg_color, fg=text_color)
    subtitle.grid(row=1, column=0, columnspan=5, pady=5)

    # Enable/Disable Online Mode
    def onlinemode(rt=False):
      global properties
      if not rt:
        try:
          if properties["online-mode"] == "true":
            properties["online-mode"] = "false"
            with open(props, 'w') as file:
              for key, value in properties.items():
                file.write(f'{key}={value}\n')
            manageserver_menu()
          elif properties["online-mode"] == "false":
            properties["online-mode"] = "true"
            with open(props, 'w') as file:
              for key, value in properties.items():
                file.write(f'{key}={value}\n')
            manageserver_menu()
          else:
            properties["online-mode"] = "true"
            with open(props, 'w') as file:
              for key, value in properties.items():
                file.write(f'{key}={value}\n')
            manageserver_menu()
        except KeyError:
          properties["online-mode"] = "true"
          with open(props, 'w') as file:
            for key, value in properties.items():
              file.write(f'{key}={value}\n')
          manageserver_menu()
      else:
        try:
          if properties["online-mode"] == "true":
            return True
          elif properties["online-mode"] == "false":
            return False
          else:
            properties["online-mode"] = "true"
            with open(props, 'w') as file:
              for key, value in properties.items():
                file.write(f'{key}={value}\n')
            return True
        except KeyError:
          properties["online-mode"] = "true"
          with open(props, 'w') as file:
            for key, value in properties.items():
              file.write(f'{key}={value}\n')
          return True

    # "Enable/Disable Online Mode" button
    if onlinemode(True):
      # "Online Mode:" label
      online_label = tk.Label(frame, text="Online Mode:", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
      online_label.grid(row=2, column=0, pady=5, sticky='e')

      # "ENABLED" label
      onlinemode_button = tk.Button(frame, text="ENABLED", command=onlinemode, height=2, width=20, bg=button_color, fg="green")
      onlinemode_button.grid(row=2, column=1, padx=5, pady=5, sticky='w')
    else:
      # "Online Mode:" label
      online_label = tk.Label(frame, text="Online Mode:", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
      online_label.grid(row=2, column=0, pady=5, sticky='e')

      # "DISABLED" label
      onlinemode_button = tk.Button(frame, text="DISABLED", command=onlinemode, height=2, width=20, bg=button_color,fg="red")
      onlinemode_button.grid(row=2, column=1, padx=5, pady=5, sticky='w')

    # Enable/Disable Hardcore Mode
    def hardcoremode(rt=False):
      global properties
      if not rt:
        try:
          if properties["hardcore"] == "true":
            properties["hardcore"] = "false"
            with open(props, 'w') as file:
              for key, value in properties.items():
                file.write(f'{key}={value}\n')
            manageserver_menu()
          elif properties["hardcore"] == "false":
            properties["hardcore"] = "true"
            with open(props, 'w') as file:
              for key, value in properties.items():
                file.write(f'{key}={value}\n')
            manageserver_menu()
          else:
            properties["hardcore"] = "true"
            with open(props, 'w') as file:
              for key, value in properties.items():
                file.write(f'{key}={value}\n')
            manageserver_menu()
        except KeyError:
          properties["hardcore"] = "false"
          with open(props, 'w') as file:
            for key, value in properties.items():
              file.write(f'{key}={value}\n')
          manageserver_menu()
      else:
        try:
          if properties["hardcore"] == "true":
            return True
          elif properties["hardcore"] == "false":
            return False
          else:
            properties["hardcore"] = "true"
            with open(props, 'w') as file:
              for key, value in properties.items():
                file.write(f'{key}={value}\n')
            return True
        except KeyError:
          properties["hardcore"] = "false"
          with open(props, 'w') as file:
            for key, value in properties.items():
              file.write(f'{key}={value}\n')
          return False
    
    # "Enable/Disable Hardcore Mode" button
    if hardcoremode(True):
      # "Hardcore Mode:" label
      hardcore_label = tk.Label(frame, text="Hardcore:", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
      hardcore_label.grid(row=3, column=0, pady=5, sticky='e')

      # "ENABLED" label
      hardcoremode_button = tk.Button(frame, text="ENABLED", command=hardcoremode, height=2, width=20, bg=button_color, fg="green")
      hardcoremode_button.grid(row=3, column=1, padx=5, pady=5, sticky='w')
    else:
      # "Hardcore Mode:" label
      hardcore_label = tk.Label(frame, text="Hardcore:", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
      hardcore_label.grid(row=3, column=0, pady=5, sticky='e')

      # "DISABLED" label
      hardcoremode_button = tk.Button(frame, text="DISABLED", command=hardcoremode, height=2, width=20, bg=button_color, fg="red")
      hardcoremode_button.grid(row=3, column=1, padx=5, pady=5, sticky='w')

    # Enable/Disable Command Blocks
    def commandblocks(rt=False):
      global properties
      if not rt:
        try:
          if properties["enable-command-block"] == "true":
            properties["enable-command-block"] = "false"
            with open(props, 'w') as file:
              for key, value in properties.items():
                file.write(f'{key}={value}\n')
            manageserver_menu()
          elif properties["enable-command-block"] == "false":
            properties["enable-command-block"] = "true"
            with open(props, 'w') as file:
              for key, value in properties.items():
                file.write(f'{key}={value}\n')
            manageserver_menu()
          else:
            properties["enable-command-block"] = "true"
            with open(props, 'w') as file:
              for key, value in properties.items():
                file.write(f'{key}={value}\n')
            manageserver_menu()
        except KeyError:
          properties["enable-command-block"] = "true"
          with open(props, 'w') as file:
            for key, value in properties.items():
              file.write(f'{key}={value}\n')
          manageserver_menu()
      else:
        try:
          if properties["enable-command-block"] == "true":
            return True
          elif properties["enable-command-block"] == "false":
            return False
          else:
            properties["enable-command-block"] = "true"
            with open(props, 'w') as file:
              for key, value in properties.items():
                file.write(f'{key}={value}\n')
            return True
        except KeyError:
          properties["enable-command-block"] = "true"
          with open(props, 'w') as file:
            for key, value in properties.items():
              file.write(f'{key}={value}\n')
          return True
    
    # "Enable/Disable Command Blocks" button
    if commandblocks(True):
      # "Command Blocks:" label
      commandblocks_label = tk.Label(frame, text="Command Blocks:", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
      commandblocks_label.grid(row=4, column=0, pady=5, sticky='e')

      # "ENABLED" label
      commandblocks_button = tk.Button(frame, text="ENABLED", command=commandblocks, height=2, width=20, bg=button_color, fg="green")
      commandblocks_button.grid(row=4, column=1, padx=5, pady=5, sticky='w')
    else:
      # "Command Blocks:" label
      commandblocks_label = tk.Label(frame, text="Command Blocks:", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
      commandblocks_label.grid(row=4, column=0, pady=5, sticky='e')

      # "DISABLED" label
      commandblocks_button = tk.Button(frame, text="DISABLED", command=commandblocks, height=2, width=20, bg=button_color, fg="red")
      commandblocks_button.grid(row=4, column=1, padx=5, pady=5, sticky='w')

    # Enable/Disable PVP
    def pvp(rt=False):
      global properties
      if not rt:
        try:
          if properties["pvp"] == "true":
            properties["pvp"] = "false"
            with open(props, 'w') as file:
              for key, value in properties.items():
                file.write(f'{key}={value}\n')
            manageserver_menu()
          elif properties["pvp"] == "false":
            properties["pvp"] = "true"
            with open(props, 'w') as file:
              for key, value in properties.items():
                file.write(f'{key}={value}\n')
            manageserver_menu()
          else:
            properties["pvp"] = "true"
            with open(props, 'w') as file:
              for key, value in properties.items():
                file.write(f'{key}={value}\n')
            manageserver_menu()
        except KeyError:
          properties["pvp"] = "true"
          with open(props, 'w') as file:
            for key, value in properties.items():
              file.write(f'{key}={value}\n')
          manageserver_menu()
      else:
        try:
          if properties["pvp"] == "true":
            return True
          elif properties["pvp"] == "false":
            return False
          else:
            properties["pvp"] = "true"
            with open(props, 'w') as file:
              for key, value in properties.items():
                file.write(f'{key}={value}\n')
            return True
        except KeyError:
          properties["pvp"] = "true"
          with open(props, 'w') as file:
            for key, value in properties.items():
              file.write(f'{key}={value}\n')
          return True
    
    # "Enable/Disable PVP" button
    if pvp(True):
      # "PVP:" label
      pvp_label = tk.Label(frame, text="PvP:", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
      pvp_label.grid(row=5, column=0, pady=5, sticky='e')

      # "ENABLED" label
      pvp_button = tk.Button(frame, text="ENABLED", command=pvp, height=2, width=20, bg=button_color, fg="green")
      pvp_button.grid(row=5, column=1, padx=5, pady=5, sticky='w')
    else:
      # "PVP:" label
      pvp_label = tk.Label(frame, text="PvP:", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
      pvp_label.grid(row=5, column=0, pady=5, sticky='e')

      # "DISABLED" label
      pvp_button = tk.Button(frame, text="DISABLED", command=pvp, height=2, width=20, bg=button_color, fg="red")
      pvp_button.grid(row=5, column=1, padx=5, pady=5, sticky='w')

    # Change Gamemode
    def gamemode_change(*args):
      global properties
      properties["gamemode"] = gamemode_var.get().lower()
      with open(props, 'w') as file:
        for key, value in properties.items():
          file.write(f'{key}={value}\n')
      manageserver_menu()
    
    # "Change Gamemode" Button
    global gamemode_var
    gamemode_var = tk.StringVar()
    gamemode_var.set(f"{properties['gamemode'].upper()}")
    gamemode_var.trace_add("write", gamemode_change)
    gamemode_options = ["SURVIVAL", "CREATIVE", "ADVENTURE", "SPECTATOR"]
    space_label = tk.Label(frame, text=" ", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
    space_label.grid(row=2, column=2, padx=15, pady=5)
    gamemode_label = tk.Label(frame, text="Gamemode:", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
    gamemode_label.grid(row=2, column=3, pady=5, sticky='e')
    gamemode_menu = tk.OptionMenu(frame, gamemode_var, *gamemode_options)
    gamemode_menu.grid(row=2, column=4, padx=5, pady=5, sticky='w')

    # Change Difficulty
    def difficulty_change(*args):
      global properties
      properties["difficulty"] = difficulty_var.get().lower()
      with open(props, 'w') as file:
        for key, value in properties.items():
          file.write(f'{key}={value}\n')
      manageserver_menu()
    
    # "Change Difficulty" Button
    global difficulty_var
    difficulty_var = tk.StringVar()
    difficulty_var.set(f"{properties['difficulty'].upper()}")
    difficulty_var.trace_add("write", difficulty_change)
    difficulty_options = ["PEACEFUL", "EASY", "NORMAL", "HARD"]
    space_label = tk.Label(frame, text=" ", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
    space_label.grid(row=3, column=2, padx=15, pady=5)
    difficulty_label = tk.Label(frame, text="Difficulty:", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
    difficulty_label.grid(row=3, column=3, pady=5, sticky='e')
    difficulty_menu = tk.OptionMenu(frame, difficulty_var, *difficulty_options)
    difficulty_menu.grid(row=3, column=4, padx=5, pady=5, sticky='w')

    # Change Level Type
    def leveltype_change(*args):
      global properties
      properties["level-type"] = f"minecraft:{leveltype_var.get().lower()}"
      with open(props, 'w') as file:
        for key, value in properties.items():
          file.write(f'{key}={value}\n')
      manageserver_menu()
    
    # "Change Level Type" Button
    global leveltype_var
    leveltype_var = tk.StringVar()
    leveltype_var.set(f"{properties['level-type'].upper().replace('MINECRAFT:', '')}")
    leveltype_var.trace_add("write", leveltype_change)
    leveltype_options = ["DEFAULT", "FLAT", "LARGEBIOMES", "AMPLIFIED"]
    space_label = tk.Label(frame, text=" ", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
    space_label.grid(row=4, column=2, padx=15, pady=5)
    leveltype_label = tk.Label(frame, text="Level Type:", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
    leveltype_label.grid(row=4, column=3, pady=5, sticky='e')
    leveltype_menu = tk.OptionMenu(frame, leveltype_var, *leveltype_options)
    leveltype_menu.grid(row=4, column=4, padx=5, pady=5, sticky='w')

    # Change Max Players
    def maxplayers_change(*args):
      global properties
      if maxplayers_var.get() == "":
        maxplayers_var.set("1")
      elif int(maxplayers_var.get()) > 10000:
        maxplayers_var.set("10000")
      properties["max-players"] = maxplayers_var.get()
      with open(props, 'w') as file:
        for key, value in properties.items():
          file.write(f'{key}={value}\n')
      manageserver_menu()
    
    # "Change Max Players" Button
    global maxplayers_var
    maxplayers_var = tk.StringVar()
    maxplayers_var.set(f"{properties['max-players']}")
    space_label = tk.Label(frame, text=" ", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
    space_label.grid(row=5, column=2, padx=15, pady=5)
    maxplayers_label = tk.Label(frame, text="Max Players:", font=("Arial", 12, "bold"), bg=bg_color, fg=text_color)
    maxplayers_label.grid(row=5, column=3, pady=5, sticky='e')
    def validate_input(P):
      # P is the new text after the edit
      if str.isdigit(P) and 1 <= int(P) <= 99999999:
          return True
      elif P == "":
          return True
      else:
          return False
    vcmd = frame.register(validate_input)
    maxplayers_entry = tk.Entry(frame, textvariable=maxplayers_var, width=8, validate="key", validatecommand=(vcmd, '%P'))
    maxplayers_entry.grid(row=5, column=4, padx=5, pady=5, sticky='w')
    save_button = tk.Button(frame, text="Save", command=maxplayers_change, height=1, width=5, bg=button_color, fg=buttontxt_color)
    save_button.grid(row=5, column=4, pady=5, sticky='e')

    # Open server.properties
    def open_props():
      global props
      try:
        os.startfile(props)
      except ValueError:
        print("Error opening file")
    
    # "Open server.properties" button
    open_button = tk.Button(frame, text="Open server.properties", command=open_props, height=3, width=30, bg="purple", fg="white")
    open_button.grid(row=6, column=0, columnspan=2, pady=15, padx=5, sticky='nsew')

    # "Go to Start Server Menu" button
    start_button = tk.Button(frame, text="Go to Start Server Menu", command=startserver_menu, height=3, width=30, bg="blue", fg="white")
    start_button.grid(row=6, column=2, columnspan=3, pady= 15, padx=5, sticky='nsew')

    # "Return to Main Menu" button
    main_button = tk.Button(frame, text="Return to Main Menu", command=main, height=2, width=30, bg=button_color, fg=buttontxt_color)
    main_button.grid(row=7, column=0, columnspan=5, pady=5, sticky="nsew")

  else:
    # Subtitle
    subtitle_text = "The server configuration files do not exist yet or are not available.\nYou must start the server properly at least once before you can configure it\n"
    subtitle = tk.Label(frame, text=subtitle_text, font=("Arial", 12), wraplength=600, bg=bg_color, fg=text_color)
    subtitle.grid(row=1, column=0, columnspan=2, pady=5)

    # "Return to Main Menu" button
    main_button = tk.Button(frame, text="Return to Main Menu", command=main, height=3, width=30, bg=button_color, fg=buttontxt_color)
    main_button.grid(row=2, column=0, columnspan=2, pady=15, sticky="nsew")

# LICENSE AND EXTRAS MENU
def licensextras_menu():
  global ntheme
  global screenmode
  global deb
  # Clears the window
  for widget in root.winfo_children():
    widget.destroy()

  # Window title
  root.title("License and Extras")

  # Min window size
  root.minsize(850, 600)

  # Set window size
  root.geometry("850x600")

  # Set BG
  root.configure(bg=bg_color)

  # Main frame
  frame = tk.Frame(root, bg=bg_color)
  frame.place(relx=0.5, rely=0.5, anchor='center')

  # Title
  title_font = ("Arial", 30, "bold")
  title = tk.Label(frame, text="License and Extras", font=title_font, bg=bg_color, fg=text_color)
  title.grid(row=0, column=0, columnspan=2, pady=5)

  # Subtitle
  subtitle_text = "SSTools4MC PRIVATE BUILD\nBETA 3.2106 FOR V2.0REL\n-------------------------------------\n\nMIT License - Copyright © 2023 NGDPL Nk\n\nHelpers:\n@naicoooossj\n@LegalizeNuclearBombs\n"
  subtitle = tk.Label(frame, text=subtitle_text, font=("Arial", 12), wraplength=600, bg=bg_color, fg=text_color)
  subtitle.grid(row=1, column=0, columnspan=2, pady=5)

  # Check current debug mode status
  def new_debug():
    global deb
    global enabled_debug
    cfg = {}
    if os.path.exists(sstools_folder_path):
      if os.path.exists(cfg_access):
        with open(cfg_access, 'r') as file:
          for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
              key, value = line.split('=')
              cfg[key.strip()] = value.strip()
        if deb == "Enable Debug Mode":
          cfg["debug"] = "true"
          with open(cfg_access, 'w') as file:
            for key, value in cfg.items():
              file.write(f'{key}={value}\n')
          enabled_debug = True
          licensextras_menu()
        elif deb == "Disable Debug Mode":
          cfg["debug"] = "false"
          with open(cfg_access, 'w') as file:
            for key, value in cfg.items():
              file.write(f'{key}={value}\n')
          enabled_debug = False
          licensextras_menu()
      else:
        with open(cfg_access, 'w') as archivo:
          archivo.write('debug=false\n')
        deb = "Enable Debug Mode"
        new_debug()
    else:
      os.makedirs(sstools_folder_path)
      with open(cfg_access, 'w') as archivo:
        archivo.write('debug=false\n')
      deb = "Enable Debug Mode"
      new_debug()

  # "Debug Change" button
  deb = sstdebug_mode(True)
  debugchange_button = tk.Button(frame, text=f"{deb}", command=new_debug, height=3, width=30, bg=button_color, fg=buttontxt_color)
  debugchange_button.grid(row=2, column=0, padx=3, pady=5, sticky='nsew')

  # Open cfg
  def open_cfg():
    try:
      os.startfile(cfg_access)
    except FileNotFoundError:
      print("Error opening file")
  
  # "Open cfg" button
  cfg_button = tk.Button(frame, text="Open Tool Config File", command=open_cfg, height=3, width=30, bg=button_color, fg=buttontxt_color)
  cfg_button.grid(row=2, column=1, padx=3, pady=5, sticky='nsew')

  # Check current theme
  def new_theme():
    global bg_color
    global button_color
    global buttontxt_color
    global text_color
    global ntheme
    cfg = {}
    if os.path.exists(sstools_folder_path):
      if os.path.exists(cfg_access):
        with open(cfg_access, 'r') as file:
          for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
              key, value = line.split('=')
              cfg[key.strip()] = value.strip()
        if ntheme == "Dark":
          cfg["theme"] = "dark"
          with open(cfg_access, 'w') as file:
            for key, value in cfg.items():
              file.write(f'{key}={value}\n')
          bg_color = "#1A1A1A"  # rgb(26, 26, 26)
          button_color = "#D3D3D3"  # rgb(211, 211, 211)
          buttontxt_color = "#1A1A1A"  # rgb(26, 26, 26)
          text_color = "white"  # White
          licensextras_menu()
        elif ntheme == "Light":
          cfg["theme"] = "light"
          with open(cfg_access, 'w') as file:
            for key, value in cfg.items():
              file.write(f'{key}={value}\n')
          bg_color = "white"  # White
          button_color = "white"  # White
          buttontxt_color = "black"  # Black
          text_color = "black"  # Black
          licensextras_menu()
      else:
        with open(cfg_access, 'w') as archivo:
          archivo.write('theme=dark\n')
        ntheme = "Dark"
        new_theme()
    else:
      os.makedirs(sstools_folder_path)
      with open(cfg_access, 'w') as archivo:
        archivo.write('theme=dark\n')
      ntheme = "Dark"
      new_theme()

  # "Change Theme" button
  ntheme = theme(True)
  ntheme_button = tk.Button(frame, text=f"Set theme to {ntheme}", command=new_theme, height=3, width=30, bg=button_color, fg=buttontxt_color)
  ntheme_button.grid(row=3, column=0, padx=3, pady=5, sticky='nsew')

  # Change screen mode
  def new_screenmode():
    global screenmode
    cfg = {}
    if os.path.exists(sstools_folder_path):
      if os.path.exists(cfg_access):
        with open(cfg_access, 'r') as file:
          for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
              key, value = line.split('=')
              cfg[key.strip()] = value.strip()
        if screenmode == "Fullscreen":
          cfg["fullscreen"] = "true"
          with open(cfg_access, 'w') as file:
            for key, value in cfg.items():
              file.write(f'{key}={value}\n')
          root.attributes('-fullscreen', True)
          licensextras_menu()
        elif screenmode == "Windowed":
          cfg["fullscreen"] = "false"
          with open(cfg_access, 'w') as file:
            for key, value in cfg.items():
              file.write(f'{key}={value}\n')
          root.attributes('-fullscreen', False)
          licensextras_menu()
      else:
        with open(cfg_access, 'w') as archivo:
          archivo.write('fullscreen=false\n')
        screenmode = "Windowed"
        new_screenmode()
  
  # "Change Screen Mode" button
  if fullscreen():
    screenmode = "Windowed"
  else:
    screenmode = "Fullscreen"
  screenmode_button = tk.Button(frame, text=f"Set window mode to {screenmode}", command=new_screenmode, height=3, width=30, bg=button_color, fg=buttontxt_color)
  screenmode_button.grid(row=3, column=1, padx=3, pady=5, sticky='nsew')

  # Open GitHub Repo
  def view_repo():
    webbrowser.open("https://github.com/NGDPLNk/SSTools4MC")
  
  # "Open GitHub Repo" button
  repo_button = tk.Button(frame, text="Open GitHub Repo", command=view_repo, height=3, width=30, bg=button_color, fg=buttontxt_color)
  repo_button.grid(row=4, column=0, padx=3, pady=5, sticky='nsew')

  # Open Text Formatting for MOTD's
  def view_motdsformat():
    webbrowser.open("https://minecraft.wiki/w/Formatting_codes")
  
  # "Open Text Formatting for MOTD's" button
  motd_button = tk.Button(frame, text="Open Text Formatting for MOTD's", command=view_motdsformat, height=3, width=30, bg=button_color, fg=buttontxt_color)
  motd_button.grid(row=4, column=1, padx=3, pady=5, sticky='nsew')

  # Open server.properties wiki
  def view_serverproperties():
    webbrowser.open("https://minecraft.wiki/w/Server.properties")

  # "Open server.properties wiki" button
  serverproperties_button = tk.Button(frame, text="Open server.properties wiki", command=view_serverproperties, height=3, width=30, bg=button_color, fg=buttontxt_color)
  serverproperties_button.grid(row=5, column=0, padx=3, pady=5, sticky='nsew')

  # Open License
  def view_license():
    webbrowser.open("https://github.com/NGDPLNk/SSTools4MC/blob/main/LICENSE")
  
  # "Open License" button
  license_button = tk.Button(frame, text="Open License", command=view_license, height=3, width=30, bg=button_color, fg=buttontxt_color)
  license_button.grid(row=5, column=1, padx=3, pady=5, sticky='nsew')

  # "Return to Main Menu" button
  main_button = tk.Button(frame, text="Return to Main Menu", command=main, height=3, width=30, bg=button_color, fg=buttontxt_color)
  main_button.grid(row=6, column=0, columnspan=2, pady=15, sticky="nsew")

# EXIT MENU
def exit_menu():
  global run
  if run and minecraft_server_process.stdin:
    # Clears the window
    for widget in root.winfo_children():
      widget.destroy()
    
    # Window title
    root.title("Your Server is still running")

    # Main frame
    frame = tk.Frame(root, bg=bg_color)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    # Title
    title_font = ("Arial", 30, "bold")
    title = tk.Label(frame, text="Your Server is still running", font=title_font, bg=bg_color, fg=text_color)
    title.grid(row=0, column=0, pady=5)

    # Subtitle
    subtitle_text = "ATTENTION! Your Server is still running. What do you want to do?\n"
    subtitle = tk.Label(frame, text=subtitle_text, font=("Arial", 12), wraplength=600, bg=bg_color, fg=text_color)
    subtitle.grid(row=1, column=0, pady=5)

    # Stop and close
    def stopnclose():
      global run
      global m
      run = False
      global minecraft_server_process
      if minecraft_server_process.stdin:
        command = "stop\n"
        minecraft_server_process.stdin.write(command.encode())
        minecraft_server_process.stdin.flush()
      run = False
      # Clears the window
      for widget in root.winfo_children():
        widget.destroy()

      # Window title
      root.title("Thank you for using this tool")

      # Main frame
      frame = tk.Frame(root, bg=bg_color)
      frame.place(relx=0.5, rely=0.5, anchor='center')

      # Title
      title_font = ("Arial", 24, "bold")
      title = tk.Label(frame, text="Thank you for using this tool\nMIT License - Copyright © 2023 NGDPL Nk", font=title_font, bg=bg_color, fg=text_color)
      title.pack(pady=5)

      # Close program after 1.8 seconds
      root.after(1800, root.destroy)

    # "Stop Server" button
    stop_button = tk.Button(frame, text="SEND STOP COMMAND AND EXIT", command=stopnclose, height=3, width=30, bg="red", fg="white")
    stop_button.grid(row=2, column=0, pady=5)

    # "Return to Main Menu" button
    main_button = tk.Button(frame, text="Return to Main Menu", command=main, height=2, width=30, bg=button_color, fg=buttontxt_color)
    main_button.grid(row=3, column=0, pady=15)
  else:
    # Clears the window
    for widget in root.winfo_children():
      widget.destroy()

    # Window title
    root.title("Thank you for using this tool")

    # Main frame
    frame = tk.Frame(root, bg=bg_color)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    # Title
    title_font = ("Arial", 24, "bold")
    title = tk.Label(frame, text="Thank you for using this tool\nMIT License - Copyright © 2023 NGDPL Nk", font=title_font, bg=bg_color, fg=text_color)
    title.pack(pady=5)

    # Close program after 1.8 seconds
    root.after(1800, root.destroy)

# MAIN MENU
def main():
  global root
  global running
  
  # Check if return from another menu
  if not running:
    running = True
    root = tk.Tk()
    root.state("zoomed")

  root.iconbitmap("assets\\icon.ico")  # Icon
  root.title("SSTools4MC")  # Window title

  # Clears the window
  for widget in root.winfo_children():
    widget.destroy()

  # Set BG
  root.configure(bg=bg_color)
  
  if fullscreen():
    root.attributes('-fullscreen', True)
  else:
    # Min window size
    root.minsize(850, 500)

    # Set window size
    root.geometry("850x500")

  # Main frame
  frame = tk.Frame(root, bg=bg_color)
  frame.place(relx=0.5, rely=0.5, anchor='center')

  # Title
  title_font = ("Arial", 30, "bold")
  title = tk.Label(frame, text="SSTools4MC", font=title_font, bg=bg_color, fg=text_color)
  title.grid(row=0, column=0, columnspan=5, pady=5)

  # Subtitle
  subtitle_text = "Welcome to SSTools4MC, a tool that allows you to manage your Minecraft server in a simple way\n\nPlease select an option below\n"
  subtitle = tk.Label(frame, text=subtitle_text, font=("Arial", 12), wraplength=600, bg=bg_color, fg=text_color)
  subtitle.grid(row=1, column=0, columnspan=5, pady=5)

  # "Start Server" button
  start_button = tk.Button(frame, text="Start Server", command=startserver_menu, height=3, width=20, bg=button_color, fg=buttontxt_color)
  start_button.grid(row=2, column=1, columnspan=3, pady=5, sticky='nsew')

  # "Manage Server" button
  manage_button = tk.Button(frame, text="Manage Server", command=manageserver_menu, height=3, width=20, bg=button_color, fg=buttontxt_color)
  manage_button.grid(row=3, column=1, columnspan=3, pady=5, sticky='nsew')

  # "License and Extras" button
  extras_button = tk.Button(frame, text="License and Extras", command=licensextras_menu, height=3, width=20, bg=button_color, fg=buttontxt_color)
  extras_button.grid(row=4, column=1, columnspan=3, pady=5, sticky='nsew')

  # "Exit" button
  exit_button = tk.Button(frame, text="Exit", command=exit_menu, height=3, width=20, bg=button_color, fg=buttontxt_color)
  exit_button.grid(row=5, column=1, columnspan=3, pady=5, sticky='nsew')

  root.mainloop()

########################
# PROGRAM START
theme()