# Interview prep

Thanks for interviewing at Stripe. To make sure that we can use our time best in the interview, we'd like to have you do some setup in advance.

First, clone this repository to your computer via the links on the right (creating a fork of the repository is not necessary). Next, ensure that you have `virtualenv` installed. If you're using Debian or Ubuntu, you likely want to run `sudo apt-get install python-virtualenv python-dev build-essential`. Otherwise, you can find installation instructions for `virtualenv` [here](https://virtualenv.pypa.io/en/latest/installation.html), and more general help with `pip` and Python package management [here](https://docs.python.org/2.7/installing/index.html). Note, we will be working with Python 2.7.

When you have `virtualenv` installed, create a new Python environment and activate it by running:
```bash
virtualenv interview_env --python=python2.7
source interview_env/bin/activate
```

Next, install some requirements by running: `pip install -r interview_requirements.txt`, where `interview_requirements.txt` is the path to the accompanying file. This may take several minutes. If you get a message like "no compiler found", you may need to install `gcc` or equivalent using your operating system's package manager. When you're able to install the packages in `interview_requirements.txt`, you're all done!
