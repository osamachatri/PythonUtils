# 🐍 Python Utils Collection

A comprehensive collection of ready-to-use utility functions for Python developers. Stop reinventing the wheel and focus on building your application.

## 📋 Description

This repository provides a curated set of battle-tested utility functions that solve common programming challenges. Whether you're working with strings, dates, files, or network requests, these utilities will save you time and reduce boilerplate code in your projects.

**Perfect for:**
- Rapidly prototyping applications
- Reducing code duplication across projects
- Learning Python best practices
- Having reliable, tested utility functions at your fingertips

## ✨ Features

### ✅ String Utils
Powerful string manipulation and formatting utilities including case conversion, sanitization, truncation, slug generation, and more.

### 🧪 Validation Utils
Comprehensive validation functions for emails, URLs, phone numbers, credit cards, IP addresses, and custom pattern matching.

### 📅 Date & Time Utils
Simplified date parsing, formatting, timezone conversion, date arithmetic, and relative time calculations.

### 🧮 Math Utils
Advanced mathematical operations including rounding, statistics, number formatting, range checks, and numerical conversions.

### 🧰 Collection Utils
Enhanced operations for lists, dictionaries, and sets including deep merging, filtering, grouping, chunking, and flattening.

### 📂 File Utils
Streamlined file operations with path manipulation, safe reading/writing, directory management, and file type detection.

### 🔐 Crypto Utils
Security-focused utilities for hashing, encryption, password generation, token creation, and secure random generation.

### 🔍 Reflection Utils
Dynamic code inspection tools for introspection, dynamic imports, attribute access, and class information retrieval.

### 🔗 Network Utils
Network-related helpers for HTTP requests, URL parsing, IP validation, downloading files, and API interactions.

### 🧵 Concurrency Utils
Threading and async utilities including thread pools, rate limiting, retry mechanisms, and parallel execution helpers.

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/python-utils.git
cd python-utils

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```python
from utils.string_utils import to_snake_case, truncate
from utils.validation_utils import is_email, is_url
from utils.date_utils import format_relative_time

# String operations
result = to_snake_case("HelloWorld")  # "hello_world"
short = truncate("Long text here", 10)  # "Long te..."

# Validation
is_email("user@example.com")  # True
is_url("https://example.com")  # True

# Date formatting
format_relative_time(datetime.now() - timedelta(hours=2))  # "2 hours ago"
```

## 📦 Modules Overview

| Module | Status | Purpose | Key Functions |
|--------|--------|---------|---------------|
| ✅ `string_utils` | **Ready** | String manipulation | `to_camel_case`, `to_snake_case`, `slugify`, `sanitize`, `truncate`, `remove_accents` |
| 🚧 `validation_utils` | **Coming Soo** | Input validation | `is_email`, `is_url`, `is_phone`, `validate_pattern`, `is_ipv4`, `is_credit_card` |
| 🚧 `date_utils` | **Coming Soo** | Date/time operations | `parse_date`, `format_date`, `add_days`, `get_timezone`, `format_relative_time` |
| 🚧 `math_utils` | **Coming Soo** | Mathematical operations | `safe_divide`, `clamp`, `percentage`, `round_decimal`, `average`, `median` |
| 🚧 `collection_utils` | **Coming Soo** | Collection operations | `deep_merge`, `flatten`, `chunk`, `group_by`, `unique`, `intersection` |
| 🚧 `file_utils` | **Coming Soo** | File operations | `safe_read`, `safe_write`, `ensure_dir`, `get_extension`, `file_exists`, `copy_file` |
| 📋 `crypto_utils` | **Planned** | Cryptography | `hash_password`, `generate_token`, `encrypt`, `decrypt`, `verify_password` |
| 📋 `reflection_utils` | **Planned** | Code introspection | `get_class_attrs`, `dynamic_import`, `has_method`, `get_annotations` |
| 📋 `network_utils` | **Planned** | Network operations | `fetch_url`, `download_file`, `parse_url`, `is_reachable`, `get_public_ip` |
| 📋 `concurrency_utils` | **Planned** | Parallel execution | `run_parallel`, `retry`, `rate_limit`, `async_gather`, `thread_pool` |
| 📋 `json_utils` | **Planned** | JSON operations | `safe_parse`, `pretty_print`, `deep_diff`, `merge_json` |
| 📋 `logging_utils` | **Planned** | Logging helpers | `setup_logger`, `log_decorator`, `context_logger` |
| 📋 `config_utils` | **Planned** | Configuration management | `load_config`, `env_var`, `merge_configs` |
| 📋 `text_utils` | **Planned** | Text processing | `extract_emails`, `word_count`, `sentiment_analysis` |
| 📋 `image_utils` | **Planned** | Image processing | `resize`, `compress`, `convert_format`, `add_watermark` |

### Status Legend
- ✅ **Ready**: Fully implemented, tested, and documented
- 🚧 **Coming Soon**: Currently in development
- 📋 **Planned**: Scheduled for future implementation

## 🧪 Testing

All utilities come with comprehensive unit tests to ensure reliability.

```bash
# Run all tests
pytest tests/

# Run specific module tests
pytest tests/test_string_utils.py

# Run with coverage
pytest --cov=utils tests/
```

## 📖 Documentation

Detailed documentation for each utility module is available in the `docs/` directory: (coming soon)

- [String Utils Documentation](docs/string_utils.md)
- [Validation Utils Documentation](docs/validation_utils.md)
- [Date Utils Documentation](docs/date_utils.md)
- [Complete API Reference](docs/api_reference.md)

## 🤝 Contributing

Contributions are welcome! Whether it's adding new utilities, improving existing ones, or fixing bugs:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-util`)
3. Commit your changes (`git commit -m 'Add amazing utility'`)
4. Push to the branch (`git push origin feature/amazing-util`)
5. Open a Pull Request

Please ensure:
- Your code follows PEP 8 style guidelines
- All tests pass
- New utilities include unit tests
- Documentation is updated accordingly

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Acknowledgments

Built with ❤️ for the Python community. Special thanks to all contributors who help make this collection better.

## 📞 Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/osamachatri/python-utils/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/osamachatri/python-utils/discussions)
- 📧 **Email**: oussamachatri7@gmail.com

---

⭐ If you find this project helpful, please consider giving it a star on GitHub!