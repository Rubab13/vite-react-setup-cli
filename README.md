# Vite React Setup 🚀

A simple automation script that turns a fresh Vite + React project into a production-ready codebase in seconds.

Instead of manually setting up Tailwind, folder structure, and boilerplate cleanup every time, this tool handles it for you automatically.

---

## ⚡ What It Does

When you run the script, it automatically:

- Installs and configures Tailwind CSS
- Updates `vite.config` with proper plugins
- Cleans default Vite boilerplate
- Sets up a production-grade folder structure
- Adds global CSS reset + Tailwind setup
- Organizes code into scalable architecture
- Prepares feature-based development structure

---

## 📁 Final Folder Structure


src/

├── assets/
├── components/
├── features/
│ └── auth/
│ ├── api/
│ ├── components/
│ ├── hooks/
│ └── index.ts
├── hooks/
├── layouts/
├── pages/
├── routes/
├── services/
├── store/
├── types/
└── utils/


---

## 🚀 How to Use

1. Create a fresh Vite React project

```bash
npm create vite@latest my-app
cd my-app
npm install
Copy app.py into the project root
Run the script
python app.py
Done.

Your project is now structured and ready for real development.

🧠 Why I Built This

Every time I started a React project, I had to repeat the same setup:

Tailwind installation
Folder structure creation
Boilerplate cleanup
Config adjustments

It was small work—but repetitive and annoying.

So I automated it.

Now I can start building features immediately instead of wasting time on setup.

📌 Tech Used
Python (automation script)
Vite
React
Tailwind CSS
💡 Future Improvements
Add Redux/Zustand setup option
Add React Router setup
Add ESLint + Prettier config
Convert into CLI tool (npx style)
Add multiple templates (basic / advanced / enterprise)
🤝 Contributing

Feel free to fork it and modify it for your own workflow.

If you improve it, share it back.
