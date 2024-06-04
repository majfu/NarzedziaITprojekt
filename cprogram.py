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



async def write_yaml(data, file_path):
    try:
        async with aiofiles.open(file_path, 'w', encoding='utf-8') as file:
            await file.write(yaml.dump(data, file))
        return f"Data successfully written to {file_path}"
    except TypeError as e:
        return f"Error writing to file: {e}"


async def read_xml(file_path):
    try:
        async with aiofiles.open(file_path, 'r', encoding='utf-8') as file:
            return xmltodict.parse(await file.read())
    except Exception as e:
        return f"Error parsing XML on input file: {e}"


async def write_xml(data, file_path):
    try:
        async with aiofiles.open(file_path, 'w', encoding='utf-8') as file:
            xml_string = xmltodict.unparse(data, pretty=True)
            await file.write(xml_string)
            return f"Data successfully written to {file_path}"
    except Exception as e:
        return f"Error writing to file: {e}"


async def process_files(input_file_path, output_file_path):
    try:
        if input_file_path.endswith('.json'):
            data = await read_json(input_file_path)
            if isinstance(data, str):
                return data

        elif input_file_path.endswith(('.yml', '.yaml')):
            data = await read_yaml(input_file_path)
            if isinstance(data, str):
                return data

        elif input_file_path.endswith('.xml'):
            data = await read_xml(input_file_path)
            if isinstance(data, str):
                return data

        else:
            return "Unsupported file format"

        if output_file_path.endswith('.json'):
            output = await write_json(data, output_file_path)
            return output

        elif output_file_path.endswith(('.yml', '.yaml')):
            output = await write_yaml(data, output_file_path)
            return output

        elif output_file_path.endswith('.xml'):
            output = await write_xml(data, output_file_path)
            return output

        else:
            return "Unsupported file format"

    except Exception as e:
        return f"Error occured: {e}"

async def on_convert():
    input_path = input_path_entry.get()
    output_path = output_path_entry.get()
    result = await process_files(input_path, output_path)
    messagebox.showinfo("Result", result)

root = tk.Tk()
root.title("Data Converter")

tk.Label(root, text="Input Path:").grid(row=0, column=0, padx=10, pady=10)
input_path_entry = tk.Entry(root, width=50)
input_path_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Output Path:").grid(row=1, column=0, padx=10, pady=10)
output_path_entry = tk.Entry(root, width=50)
output_path_entry.grid(row=1, column=1, padx=10, pady=10)

convert_button = tk.Button(root, text="Convert", command=async_handler(on_convert))
convert_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

def on_click1():
    input_path_entry.delete(0, 'end')
    file_path = filedialog.askopenfilename()
    input_path_entry.insert(0, file_path)

browse_button = tk.Button(root, text="Browse", command=on_click1)
browse_button.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

def on_click2():
    output_path_entry.delete(0, 'end')
    file_path = filedialog.askdirectory()
    output_path_entry.insert(0, file_path)

browse_button = tk.Button(root, text="Browse", command=on_click2)
browse_button.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

async_mainloop(root)
