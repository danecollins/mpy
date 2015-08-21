#! /bin/bash

# list 1090921d49
# apikey apikey=0bd078c731d4a3c15201cc4e1dcda3d8-us1
# campaign

# base url: https://us1.api.mailchimp.com/3.0/


#curl -L 'https://us1.api.mailchimp.com/2.0/lists/member-info.json?apikey=0bd078c731d4a3c15201cc4e1dcda3d8-us1&id=1090921d49&array[]=stephendumas@gatech.edu'
curl -L 'https://us1.api.mailchimp.com/1.3?method=listMemberInfo&apikey=0bd078c731d4a3c15201cc4e1dcda3d8-us1&id=1090921d49&email_address=stephendumas@gatech.edu&merge_vars=&output=json'