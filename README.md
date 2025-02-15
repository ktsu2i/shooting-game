# Shooting Game

## Set up

### 1. Clone this repository

```
git clone 
```

### 1. Install Python

#### For Mac

Python 3 should be already installed in Mac.
If you run this following command on terminal, you should get the version.

```
python3 -V
```

e.g.
```
Python 3.9.6
```

#### For Windows

Go to [here](https://www.python.org/) to install the latest version of Python.
Then, run this following command and check if you installed it successfully.

```
python --version
```

e.g.
```
Python 3.9.6
```

### 2. Set up for a virtual environment

If you work on multiple projects in Python, package version conflicts could happen, so it is essential to create a virtual environment for each project to avoid any unexpected errors.

After Python 3.3, it comes with the built-in package called `venv`.

#### Create a virtual environment. 

You can name it whatever you want.

```
python -m venv [env name]
or
python3 -m venv [env name]
```

#### Activate

For Mac

```
. [env name]/bin/activate
```

For Windows

```
.=\[env name]\Scripts\activate
```

### 3. Install Pygame

```
pip install pygame
```

### 4. R# shooting-game
