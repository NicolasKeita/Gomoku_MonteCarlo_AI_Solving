#!/usr/bin/python3

from cx_Freeze import setup, Executable

setup(
    name="pbrain-gomoku-ai",
    version="0.1",
    description="This is Gomoku !",
    executables=[Executable("pbrain-gomoku-ai.py")]
)
