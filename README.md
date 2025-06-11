			 LoadScope

LoadScope is a lightweight Linux system load monitoring tool that comes with both a slick CLI interface and a Flask-based web dashboard. It shows you real-time CPU, RAM, and system usage, perfect for devs, sysadmins, and anyone who vibes with terminal magic and web UIs.


📦 Features

- ✅ Real-time system load stats (CPU, RAM, disk)
- 🌐 Flask web dashboard with live updating charts
- 🖥️ CLI interface with rich formatting
- 💡 Clean modular codebase (separated into `cli`, `web`, and `utils`)
- 🔒 SELinux & firewall friendly (once configured)


📸 Web UI Preview

> Add screenshots or GIFs of your dashboard here once it's up.  
> Use tools like `peek` or `flameshot` to grab those clean snaps.

 🧰 Tech Stack

- Python 3
- Flask
- Rich (for CLI)
- psutil (for system data)
- Gunicorn (optional, for production deployment)



🛠️ Installation

git clone git@github.com:ariful420/loadscope.git

cd loadscope

pip install -r requirements.txt

    If you face issues with rich or psutil, make sure you're using Python 3.7+.

🚦 Usage
🖥️ CLI Mode

python loadscope_cli.py

🌐 Web Dashboard

python loadscope_web.py

Then open your browser and visit:

http://<your-ip>:5000

    If running on a VM, don’t forget to allow port 5000 through firewall and handle SELinux rules accordingly.

🌍 Remote Access

If accessing from outside:

    Allow port 5000 in firewall

    Set host='0.0.0.0' in app.run()

    Fix SELinux with:

sudo setsebool -P httpd_can_network_connect 1

🧠 Future Plans

    Dark mode support

    User authentication

    Live notifications

    Export stats to CSV or Grafana integration

🧑💻 Author

Md. Ariful Islam
📬 arifular85@gmail.com
🔗 GitHub: @ariful420
