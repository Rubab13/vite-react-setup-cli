import os
import json
import subprocess
from pathlib import Path

# =========================================================
# React + TypeScript + Tailwind Industrial Structure Setup
# Run this file from the ROOT of your Vite React project
# =========================================================

ROOT = Path.cwd()
SRC = ROOT / "src"

print("\n🚀 Setting up professional React codebase...\n")

# =========================================================
# 1. INSTALL TAILWIND
# =========================================================

print("📦 Installing Tailwind...")

subprocess.run(
    "npm install tailwindcss @tailwindcss/vite",
    shell=True,
    check=True,
)

# =========================================================
# 2. UPDATE vite.config.ts / vite.config.js
# =========================================================

vite_ts = ROOT / "vite.config.ts"
vite_js = ROOT / "vite.config.js"

vite_content = """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss()],
})
"""

if vite_ts.exists():
    vite_ts.write_text(vite_content, encoding="utf-8")
    print("✅ Updated vite.config.ts")

elif vite_js.exists():
    vite_js.write_text(vite_content, encoding="utf-8")
    print("✅ Updated vite.config.js")

# =========================================================
# 3. CREATE APP.CSS
# =========================================================

app_css = """@import "tailwindcss";

/* =========================================
   Global Reset
========================================= */

*,
*::before,
*::after {
  box-sizing: border-box;
}

* {
  margin: 0;
  padding: 0;
}

/* =========================================
   Root
========================================= */

html,
body,
#root {
  width: 100%;
  min-height: 100vh;
}

body {
  font-family: Inter, sans-serif;
  background: #ffffff;
  color: #111827;
  line-height: 1.5;
  text-rendering: optimizeLegibility;
}

/* =========================================
   Media Defaults
========================================= */

img,
picture,
video,
canvas,
svg {
  display: block;
  max-width: 100%;
}

/* =========================================
   Form Elements
========================================= */

input,
button,
textarea,
select {
  font: inherit;
}

button {
  cursor: pointer;
  border: none;
  background: none;
}

/* =========================================
   Links
========================================= */

a {
  color: inherit;
  text-decoration: none;
}

/* =========================================
   Lists
========================================= */

ul,
ol {
  list-style: none;
}
"""

(SRC / "App.css").write_text(app_css, encoding="utf-8")
print("✅ Updated App.css")

# =========================================================
# 4. REMOVE DEFAULT FILES
# =========================================================

files_to_remove = [
    SRC / "index.css",
    SRC / "assets" / "react.svg",
]

for file in files_to_remove:
    if file.exists():
        file.unlink()
        print(f"🗑 Removed {file.name}")

# =========================================================
# 5. UPDATE main.jsx / main.tsx
# =========================================================

main_jsx = SRC / "main.jsx"
main_tsx = SRC / "main.tsx"

main_content_js = """import React from 'react'
import ReactDOM from 'react-dom/client'
import './App.css'
import App from './App'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
"""

main_content_ts = """import React from 'react'
import ReactDOM from 'react-dom/client'
import './App.css'
import App from './App'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
"""

if main_jsx.exists():
    main_jsx.write_text(main_content_js, encoding="utf-8")
    print("✅ Updated main.jsx")

if main_tsx.exists():
    main_tsx.write_text(main_content_ts, encoding="utf-8")
    print("✅ Updated main.tsx")

# =========================================================
# 6. UPDATE APP FILE
# =========================================================

app_jsx = SRC / "App.jsx"
app_tsx = SRC / "App.tsx"

app_content = """function App() {
  return (
    <div className="flex min-h-screen items-center justify-center">
      <h1 className="text-3xl font-bold">
        Professional React Setup Ready 🚀
      </h1>
    </div>
  )
}

export default App
"""

if app_jsx.exists():
    app_jsx.write_text(app_content, encoding="utf-8")
    print("✅ Updated App.jsx")

if app_tsx.exists():
    app_tsx.write_text(app_content, encoding="utf-8")
    print("✅ Updated App.tsx")

# =========================================================
# 7. CREATE INDUSTRIAL FOLDER STRUCTURE
# =========================================================

folders = [
    "assets",
    "components",
    "features",
    "features/auth",
    "features/auth/api",
    "features/auth/components",
    "features/auth/hooks",
    "hooks",
    "layouts",
    "pages",
    "routes",
    "services",
    "store",
    "types",
    "utils",
]

for folder in folders:
    path = SRC / folder
    path.mkdir(parents=True, exist_ok=True)

    gitkeep = path / ".gitkeep"
    gitkeep.touch(exist_ok=True)

print("✅ Created industrial folder structure")

# =========================================================
# 8. CREATE FEATURE INDEX FILE
# =========================================================

feature_index = SRC / "features" / "auth" / "index.ts"

feature_index.write_text(
    """// Auth feature exports
""",
    encoding="utf-8",
)

print("✅ Created auth/index.ts")

# =========================================================
# 9. UPDATE INDEX.HTML
# =========================================================

index_html = ROOT / "index.html"

if index_html.exists():
    html_content = index_html.read_text(encoding="utf-8")

    if '<link rel="stylesheet"' not in html_content:
        html_content = html_content.replace(
            "</head>",
            '  <link rel="stylesheet" href="/src/App.css" />\n</head>',
        )

    index_html.write_text(html_content, encoding="utf-8")
    print("✅ Updated index.html")

# =========================================================
# DONE
# =========================================================

print("\n🎉 PROFESSIONAL REACT SETUP COMPLETE!")
print("👉 Now run: npm run dev\n")
