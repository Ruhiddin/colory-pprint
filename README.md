# Colory PPrint

**Colory PPrint** is a Python logging package that outputs color-coded and formatted JSON logs. It allows for easy-to-read logs with foreground and background color customizations, text styles (like bold, underline), and ensures that even non-serializable objects are logged correctly.

## Features:
- Color-coded JSON logs with support for foreground and background colors.
- Supports various text styles such as bold, underline, reverse, and concealed.
- Customizable logging for Python applications, ideal for debugging and data visualization.
- Handles non-serializable objects gracefully by displaying their type and memory address.

## Installation

You can install the package via `pip` from the GitHub repository:

```bash
pip install git+https://github.com/your-username/colory_pprint.git
```

Alternatively, you can clone the repository and install manually:

```bash
git clone https://github.com/your-username/colory_pprint.git
cd colory_pprint
pip install .
```

## Usage

### Basic Usage:

```python
from colory_pprint import ColoryLogger

log = ColoryLogger()

log({"message": "Hello, World!"})
```

### Logging with Colors and Styles:

You can chain colors, background colors, and styles:

```python
log.red.bold({"status": "error", "message": "An error occurred!"})
log.green.on_black.underline({"status": "success", "message": "Operation successful."})
```

### Handling Non-Serializable Objects:

The logger can handle non-serializable objects (e.g., custom objects) and log their `repr()`:

```python
class CustomObject:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

custom_obj = CustomObject(name="Test", value=100)

log.red.bold({
    "status": "error", 
    "message": "An error occurred!",
    "object": custom_obj
})
```

The output will show:

```json
{
   "status": "error",
   "message": "An error occurred!",
   "object": "<CustomObject object at 0x7f8a3f8b93d0>"
}
```

### Available Colors:

- **Foreground:** black, red, green, yellow, blue, magenta, cyan, white, grey, light_red, light_green, light_yellow, light_blue, light_magenta, light_cyan, light_white.
- **Background:** on_black, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white, on_grey, on_light_red, on_light_green, on_light_yellow, on_light_blue, on_light_magenta, on_light_cyan, on_light_white.

### Available Text Styles:

- bold
- underline
- reverse
- concealed

### Debug Mode:

You can enable debug mode to print raw JSON data:

```python
log = ColoryLogger(debug=True)
log({"message": "Debug mode enabled!"})
```

This will print the JSON output with applied styles and formatting, allowing you to verify that the data is being serialized as expected.
