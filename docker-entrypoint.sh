#!/bin/bash
EGG_DIR=src/collective.z3cform.mapwidget

set -e

args=("$@")

case $1 in
    run)

        cd $EGG_DIR
        if [ ! -d ./src/collective.z3cform.mapwidget.egg-info ]; then
             python setup.py egg_info
        fi

        /srv/webapp/bin/debuginstance fg
        ;;
    *)
        exec "$@"
        ;;
esac
