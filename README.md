# 🧙‍♂️ Digital Necromancer

[![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)](https://nodejs.org/)
[![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)

## 📖 Description

Digital Necromancer is a powerful full-stack web application that breathes new life into old, legacy codebases. Like a necromancer who revives the dead, this tool uses openai/gpt-oss-20b to analyze, explain, and modernize outdated code snippets and entire legacy projects.

Whether you're dealing with callback hell from the early 2010s, deprecated jQuery patterns, or ancient PHP code that makes you cry, Digital Necromancer transforms your legacy nightmares into modern, maintainable masterpieces.

**Problem it solves:**
- Legacy code migration and modernization
- Understanding complex, undocumented codebases
- Learning modern alternatives to outdated patterns
- Reducing technical debt in existing projects

## ✨ Key Features

- **🔮 AI-Powered Code Analysis:** Leverages Hugging Face's GPT OSS 20B model for intelligent code understanding
- **⚡ Modern Code Generation:** Converts legacy patterns to modern equivalents (callbacks → async/await, jQuery → vanilla JS, etc.)
- **📚 Intelligent Explanations:** Provides detailed, plain-English explanations of code transformations
- **🔒 Secure Code Input:** Safe and secure interface for submitting sensitive legacy code
- **💾 Transformation History:** Save and manage your code modernization projects (optional user profiles)
- **🎨 Beautiful UI:** Modern, responsive interface built with Tailwind CSS and Shadcn/UI
- **⚡ Fast Performance:** Built on Next.js 14 with App Router for optimal performance

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| **Frontend** | Next.js 14 (App Router), React, TypeScript |
| **Styling** | Tailwind CSS, Shadcn/UI |
| **Backend** | Python FastAPI |
| **AI/ML** | Hugging Face API (GPT OSS 20B) |
| **Development** | Vite, ESLint, Prettier |

## 🚀 Getting Started

### Prerequisites

- Node.js (v18 or higher)
- Python (v3.8 or higher)
- npm or yarn package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/digital-necromancer.git
   cd digital-necromancer
   ```

2. **Install Frontend Dependencies**
   ```bash
   # Navigate to frontend directory
   cd src/gptoss
   npm install
   ```

3. **Install Backend Dependencies**
   ```bash
   # Navigate to backend directory (assuming backend is in separate folder)
   cd ../backend
   pip install -r requirements.txt
   ```

4. **Set up Environment Variables**
   
   Create a `.env.local` file in the frontend root and `.env` in the backend root:

   **Frontend (.env.local):**
   ```env
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```

   **Backend (.env):**
   ```env
   HUGGINGFACE_API_KEY=your_huggingface_token_here
   CORS_ORIGINS=http://localhost:3000
   ```

5. **Start the Development Servers**

   **Backend (Terminal 1):**
   ```bash
   cd backend
   uvicorn main:app --reload --port 8000
   ```

   **Frontend (Terminal 2):**
   ```bash
   cd src/gptoss
   npm run dev
   ```

6. **Open your browser**
   
   Navigate to `http://localhost:3000` to see the application running.

## 🎯 Usage

1. **Paste Your Legacy Code:** Use the secure input interface to submit your old code
2. **Select Transformation Type:** Choose the type of modernization you need
3. **AI Analysis:** The system analyzes your code using advanced AI models
4. **Review Results:** Get modernized code alongside detailed explanations
5. **Save & Export:** Save your transformations and export the results

*Screenshot placeholder: Add a screenshot of the main interface showing the before/after code comparison*

## 🏆 Hackathon Innovation

**What makes Digital Necromancer special:**

- **🎯 Real Problem, Real Solution:** Addresses a $85B industry pain point
- **🤖 AI-First Approach:** Leverages cutting-edge open-source AI models  
- **⚡ Full-Stack Excellence:** Modern tech stack with optimal performance
- **🎨 User-Centric Design:** Intuitive interface that anyone can use
- **🔧 Production Ready:** Scalable architecture ready for real-world deployment

**Technical Innovation:**
- Custom AI prompting for code analysis and transformation
- Real-time code processing with FastAPI backend
- Modern React components with TypeScript safety
- Responsive design that works on all devices

## 🚧 What's Next?

**Future Roadmap:**
- [ ] Support for more programming languages (Go, Rust, Swift)
- [ ] Integration with GitHub for direct repository processing  
- [ ] AI-powered code review and security analysis
- [ ] Team collaboration features
- [ ] Enterprise deployment options

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Backend      │    │  Hugging Face   │
│   (Next.js)     │◄──►│   (FastAPI)     │◄──►│   AI Models     │
│                 │    │                 │    │                 │  
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `HUGGINGFACE_API_KEY` | Your Hugging Face API token for AI model access | Yes | - |
| `NEXT_PUBLIC_API_URL` | Backend API URL for frontend requests | Yes | `http://localhost:8000` |
| `CORS_ORIGINS` | Allowed CORS origins for the backend | Yes | `http://localhost:3000` |

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Contribution Guidelines

- Follow the existing code style and conventions
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

### Usage Rights

You are free to use this project by:

1. **Creating your own Hugging Face token** at [Hugging Face](https://huggingface.co/settings/tokens)
2. **Setting up your environment** by adding your token to the backend `.env` file
3. **Running the application** following the installation instructions above

The Apache 2.0 license allows you to freely use, modify, and distribute this software for both personal and commercial purposes.

## 🙏 Acknowledgments

- Hugging Face for providing powerful AI models
- The open-source community for the amazing tools and libraries
- All contributors who help improve this project

## 📞 Support

If you encounter any issues or have questions:

- Open an issue on GitHub
- Check the documentation
- Join our community discussions

---

**Made with ❤️ and a touch of digital necromancy**
