#!/bin/bash
re='^[0-9]+$'
if ! [[ $1 =~ $re ]] || [ "$#" -ne 1 ]
then
  echo "Not a valid bug ID, search link is here"
  for i in $*;
  do
    searchterm=$searchterm"+$i"
  done
  url="https://bugzilla.mozilla.org/buglist.cgi?quicksearch=$searchterm"
  echo $url
else
  url="https://bugzilla.mozilla.org/show_bug.cgi?id=$1"
  echo $url
  wget --quiet -O - $url \
    | paste -s -d " "  \
    | sed -e 's!.*<head>\(.*\)</head>.*!\1!' \
    | sed -e 's!.*<title>\(.*\)</title>.*!\1!'\
    | sed -e 's|&ndash;|-|g'\
    | sed -e 's|&quot;|"|g'
fi
