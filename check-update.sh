#!/bin/sh
git ls-remote --tags https://github.com/luceneplusplus/LucenePlusPlus 2>/dev/null |awk '{ print $2; }' |sed -e 's,\^{},,' |grep ^refs/tags/rel_ |cut -d_ -f2- |sort -V |tail -n1
