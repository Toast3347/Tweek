import json
import time
import urllib.request
import urllib.error
import random

API_URL = "http://localhost:8080/messages"
INTERVAL_SECONDS = 5

MESSAGES = [

    {"author": "Kenny", "body": "What the fuck is wrong with this town?"},
    {"author": "Kenny", "body": "Shit happens. Mostly to me."},
    {"author": "Kenny", "body": "I'm too poor to die and too unlucky to live."},

    {"author": "Cartman", "body": "Respect my authoritah!"},
    {"author": "Cartman", "body": "Screw you guys, I'm going home!"},
    {"author": "Cartman", "body": "I'm not fat, I'm big-boned!"},
    {"author": "Cartman", "body": "You will respect my authority, you stupid assholes!"},
    {"author": "Cartman", "body": "Whatever, I do what I want!"},
    {"author": "Cartman", "body": "I'm surrounded by fucking idiots!"},

    {"author": "Stan", "body": "Dude, what the hell is going on?"},
    {"author": "Stan", "body": "Seriously, this town is messed up."},
    {"author": "Stan", "body": "I just wanted one normal fucking day."},
    {"author": "Stan", "body": "Oh my God, this is so stupid."},
    {"author": "Stan", "body": "Can we please stop making terrible decisions?"},
    {"author": "Stan", "body": "Oh my God, they killed Kenny!"},

    {"author": "Kyle", "body": "You guys are being complete idiots!"},
    {"author": "Kyle", "body": "Cartman, shut the hell up!"},
    {"author": "Kyle", "body": "I swear, you're the worst person I know."},
    {"author": "Kyle", "body": "This is the dumbest shit I've ever heard."},
    {"author": "Kyle", "body": "Why do I even bother with you people?"},
    {"author": "Kyle", "body": "You bastards!"},

    {"author": "Butters", "body": "Oh, hamburgers!"},
    {"author": "Butters", "body": "Aw, geez, I think I'm in trouble again."},
    {"author": "Butters", "body": "I didn't do anything! I swear!"},
    {"author": "Butters", "body": "Well, gosh darn it, that's just terrible!"},
    {"author": "Butters", "body": "I'm having a really bad day, fellas."},

    {"author": "Randy", "body": "I thought this was America!"},
    {"author": "Randy", "body": "I'm sorry, I thought this was America!"},
    {"author": "Randy", "body": "I'm white trash, and I'm in trouble!"},
    {"author": "Randy", "body": "This is fucking ridiculous, Sharon!"},
    {"author": "Randy", "body": "I didn't hear no bell!"},
    {"author": "Randy", "body": "It's time to get absolutely shitfaced!"},

    {"author": "Jimmy", "body": "W-wow, what a bunch of assholes."},
    {"author": "Jimmy", "body": "I mean, seriously, folks, what the hell?"},
    {"author": "Jimmy", "body": "Th-th-this is a complete disaster."},
    {"author": "Jimmy", "body": "That's not funny, you guys. Well, maybe a little."},

    {"author": "Towelie", "body": "Don't forget to bring a towel!"},
    {"author": "Towelie", "body": "I have no idea what's going on."},
    {"author": "Towelie", "body": "Wanna get high?"},
    {"author": "Towelie", "body": "You're a towel!"},
    {"author": "Towelie", "body": "I have no idea what's happening, but I'm having a great time."},

    {"author": "Mr. Garrison", "body": "Screw you guys, I'm going home!"},
    {"author": "Mr. Garrison", "body": "I don't trust anything that bleeds for five days and doesn't die."},
    {"author": "Mr. Garrison", "body": "Well, class, this is a complete shitshow."},

    {"author": "Chef", "body": "Hello there, children!"},
    {"author": "Chef", "body": "You don't have to be a scientist to know that's some bullshit."},
    {"author": "Chef", "body": "Now that's what I call a damn fine meal!"},

    {"author": "Mr. Mackey", "body": "Drugs are bad, mmkay?"},
    {"author": "Mr. Mackey", "body": "This behavior is completely unacceptable, mmkay?"},
    {"author": "Mr. Mackey", "body": "Swearing is bad, mmkay?"},
    {"author": "Mr. Mackey", "body": "You little bastards need to calm down, mmkay?"},

    {"author": "Craig", "body": "Whatever."},
    {"author": "Craig", "body": "This is fucking stupid."},
    {"author": "Craig", "body": "I don't care. Leave me alone."},
    {"author": "Craig", "body": "Can everyone just shut up for five minutes?"},

    {"author": "Wendy", "body": "You're all acting like complete morons."},
    {"author": "Wendy", "body": "Maybe try using your brains for once."},
    {"author": "Wendy", "body": "This is exactly why nobody takes you seriously."},

    {"author": "Token", "body": "Dude, that's messed up."},
    {"author": "Token", "body": "I'm not getting involved in this bullshit."},
    {"author": "Token", "body": "You guys need to get your shit together."},

    {"author": "PC Principal", "body": "That's not PC, bro!"},
    {"author": "PC Principal", "body": "Check your privilege, bro!"},
    {"author": "PC Principal", "body": "We are not tolerating that shit, bro!"},

    {"author": "Mr. Hankey", "body": "Howdy ho!"},
    {"author": "Mr. Hankey", "body": "Howdy ho, you filthy animals!"},
]


def send_message(message):
    data = json.dumps(message).encode("utf-8")

    request = urllib.request.Request(
        API_URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=5) as response:
            print(f"Sent: {message['author']}: {message['body']} "
                  f"(HTTP {response.status})")
    except (urllib.error.URLError, TimeoutError) as error:
        print(f"Failed to send message: {error}")


def main():
    print(f"Sending a message every {INTERVAL_SECONDS} seconds.")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            message = random.choice(MESSAGES)
            send_message(message)
            time.sleep(INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\nAutomates messages stopped. Goodbye!")


if __name__ == "__main__":
    main()