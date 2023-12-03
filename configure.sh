#!/bin/bash
pip install requests
(crontab -l 2>/dev/null; echo "@reboot /usr/bin/python $PWD/CheerTree.py") | crontab -
