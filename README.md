# Animal Behavior Analyzer

The **Animal Behavior Analyzer** is a tool designed to process videos of animals and analyze their behavior to identify potential diseases or health conditions. By leveraging a Retrieval-Augmented Generation (RAG) system, it provides insights into animal health based on observed behaviors.

## Features

- **Video Processing**: Analyze animal behavior from video files.
- **Health Assessment**: Identify potential diseases or health conditions based on behavior patterns.
- **RAG System**: Uses a Retrieval-Augmented Generation system to enhance understanding and provide detailed health insights.
- **Customizable Prompts**: Includes pre-defined prompts for health assessments, which can be tailored for specific use cases.

## Project Structure

```
.
├── Makefile                 # Build and automation tasks
├── pyproject.toml           # Python project configuration
├── README.md                # Project documentation
├── demo/                    # Demo scripts and prompts
│   ├── demo.py              # Example script for running the tool
│   ├── prompt/              # Pre-defined health assessment prompts
│   └── rag_papers/          # RAG-related resources
├── src/                     # Source code
│   └── anakin_library/      # Core library for video processing and analysis
└── cceb594d-cd8d-4681-96e2-7cd9a2f5be46/
    ├── data_level0.bin      # Binary data for processing
    ├── header.bin           # Metadata for video analysis
    ├── length.bin           # Length data for video processing
    └── link_lists.bin       # Link lists for RAG system
```

## Getting Started

### Prerequisites

- Python 3.8 or later
- Required dependencies (listed in [`pyproject.toml`](pyproject.toml))

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd animal-behavior-analyzer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the demo script to analyze a sample video:
   ```bash
   python demo/demo.py
   ```

2. Customize prompts in the [`demo/prompt`](demo/prompt) directory to tailor health assessments for specific animals or conditions.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- The RAG system implementation is inspired by state-of-the-art research in retrieval-augmented generation.
- Special thanks to contributors and researchers in the field of animal health and behavior analysis.

---

For more information, please refer to the documentation or contact the project maintainers.