import json
import os
import sys

from email.message import EmailMessage
from email.utils import formatdate
from imaplib import IMAP4_SSL


def main():
    filename = os.path.expanduser("~/.shlrc")
    with open(filename) as fp:
        config = json.load(fp)

    msg = EmailMessage()
    msg["Date"] = formatdate()
    msg["From"] = config["from"]
    msg.set_content(" ".join(sys.argv[1:]))
    msg = bytes(msg)

    with IMAP4_SSL(config["host"]) as mbox:
        mbox.login(config["user"], config["pass"])
        print(mbox.append(config["mbox"], None, None, msg))
