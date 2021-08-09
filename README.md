# Operating-System-Agnostic-File-System-Analyzer [![GitHub stars](https://img.shields.io/github/stars/badges/shields.svg?style=social&label=Stars)](https://github.com/buraktokman/Operating-System-Agnostic-File-System-Analyzer/)

[![Travis](https://img.shields.io/travis/rust-lang/rust.svg)](https://github.com/buraktokman/Operating-System-Agnostic-File-System-Analyzer)
[![Repo](https://img.shields.io/badge/source-GitHub-303030.svg?maxAge=3600&style=flat-square)](https://github.com/buraktokman/Operating-System-Agnostic-File-System-Analyzer)
[![Requires.io](https://img.shields.io/requires/github/celery/celery.svg)](https://requires.io/github/buraktokman/Operating-System-Agnostic-File-System-Analyzer/requirements/?branch=master)
[![Scrutinizer](https://img.shields.io/scrutinizer/g/filp/whoops.svg)](https://github.com/buraktokman/Operating-System-Agnostic-File-System-Analyzer)
[![DUB](https://img.shields.io/dub/l/vibe-d.svg)](https://choosealicense.com/licenses/mit/)
[![Donate with Bitcoin](https://img.shields.io/badge/Donate-BTC-orange.svg)](https://blockchain.info/address/17dXgYr48j31myKiAhnM5cQx78XBNyeBWM)
[![Donate with Ethereum](https://img.shields.io/badge/Donate-ETH-blue.svg)](https://etherscan.io/address/91dd20538de3b48493dfda212217036257ae5150)

Analyze file count, size and type information on different operating systems with Python script.

Python script that analyzes file size, type information and file count, size in folder on different operating systems. Script testing done on Windows 10 and macOS systems. Both forking fine, haven’t done the testing but it will most likely work on Linux and more other operating systems.

Accomplishing the aim of this project be done with standard & external python modules, system calls and executing command on the system. That’s why the output of the script separated into two parts. Part 1: Python Modules and Part 2: Commands & System Calls.


### Instructions
------

0. Fork, clone or download this repository

    `git clone https://github.com/buraktokman/Operating-System-Agnostic-File-System-Analyzer.git`

1. Navigate to the directory

    `cd Operating-System-Agnostic-File-System-Analyzer`

2. Install requirements

    `pip install -r requirements.txt`

3. Run the script with parameters. Provide directory or folder path to the script.

    `python3 analyze.py --file="./" `

### LICENSE
------

MIT License
