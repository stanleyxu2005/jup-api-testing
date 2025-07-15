#!/usr/bin/env bash

# https://zhuanlan.zhihu.com/p/341481537
VENV_DIR=venv
if [ ! -d "$VENV_DIR" ]; then
  echo "[INFO] Creating virtual python env..."
  python -m venv "$VENV_DIR"
fi

VENV_BIN_DIR="$VENV_DIR"/bin
if [ ! -d $VENV_BIN_DIR ]; then
  VENV_BIN_DIR="$VENV_DIR"/Scripts
fi
if [ ! -d $VENV_BIN_DIR ]; then
  echo "[ERROR] Failed to create env"
  exit 1
fi

echo "[INFO] Activating env $VENV_BIN_DIR"
source $VENV_BIN_DIR/activate

#if [ ! -f "$VENV_BIN_DIR/django-admin" ]; then
#  echo "[INFO] Check install dependencies..."
#  pip install --upgrade -r requirements.txt \
#    --require-virtualenv \
#    --disable-pip-version-check
#fi

echo "[INFO] Project is ready to start"
