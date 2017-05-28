#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# MD5

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    pass

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')
