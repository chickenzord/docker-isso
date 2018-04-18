#!/bin/sh -e

export ISSO_SETTINGS="$(isso_settings.py $ISSO_SETTINGS)"
exec "$@"
