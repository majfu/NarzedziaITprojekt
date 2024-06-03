import json
import yaml
import xmltodict
import tkinter as tk
from tkinter import messagebox
import asyncio
import aiofiles
from async_tkinter_loop import async_handler, async_mainloop


async def read_json(file_path):
    try:
        async with aiofiles.open(file_path, 'r', encoding='utf-8') as file:
            return json.load(await file.read())
    except json.JSONDecodeError as e:
        return f"Error parsing JSON on input file: {e}"
