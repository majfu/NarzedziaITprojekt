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


async def write_json(data, file_path):
    try:
        async with aiofiles.open(file_path, 'w', encoding='utf-8') as file:
            await file.write(json.dumps(data, indent=4))
        return f"Data successfully written to {file_path}"
    except TypeError as e:
        return f"Error writing to file: {e}"



async def read_yaml(file_path):
    async with aiofiles.open(file_path, 'r', encoding='utf-8') as file:
        try:
            return yaml.safe_load(await file.read())
        except yaml.YAMLError as e:
            return f"Error parsing YAML on input file: {e}"



