#!/bin/bash

export GOOGLE_APPLICATION_CREDENTIALS=/opt/picardtipshi/sa.json
cat <<<$GOOGLE_SA_JSON >$GOOGLE_APPLICATION_CREDENTIALS
python /opt/picardtipshi/main.py
