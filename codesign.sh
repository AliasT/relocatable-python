#!/bin/bash

echo $1;


codesign -s $APP_SIGN_ID --deep --force --entitlements=entitlements.mac.plist --preserve-metadata=flags,runtime $1
# function sign {
# }


# fd ".+\.so$" -x sign
# fd ".+\.dylib$" -x sign
# fd ".+\.a$" -x sign


