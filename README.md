# Python-template

## Description

This is a template for Python projects including a script to generate requirements.txt
and a virtual environment that loads the system site packages to avoid having to
install large libraries multiple times on the same machine.

Inspired by [romaine's python template](https://github.com/rom1504/python-template).

## Development

### Use base virtual environment

```bash
conda activate base
```

### Create virtual environment

```bash
python -m venv venv --system-site-packages
```

### Activate virtual environment

```bash
source venv/bin/activate
```

### Create requirements.txt

```bash
python scripts/generate_requirements.py
```

## Usage

### Installation

```bash
pip install -r requirements.txt
```

### Testing

```bash
pytest
```

### Formatting

```bash
black .
```
