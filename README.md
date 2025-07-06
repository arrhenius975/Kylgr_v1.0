# Kylgr - Cross-Platform Keylogger

A simple, lightweight keylogger written in Python with both Linux and Windows versions.

## ⚠️ DISCLAIMER

**This tool is for educational and authorized testing purposes only.**
- Only use on systems you own or have explicit permission to test
- Respect privacy laws and regulations in your jurisdiction
- The authors are not responsible for misuse of this software

## Project Structure

```
Kylgr/
├── kylgr/
│   ├── keylgr.py      # Linux version
│   └── winkylgr.py    # Windows version
├── requirements.txt    # Dependencies
└── README.md          # This file
```

## Quick Start

### Prerequisites
```bash
pip install -r requirements.txt
```

### Linux Usage
```bash
python kylgr/keylgr.py
```

### Windows Usage
```bash
python kylgr/winkylgr.py
```

## Features

### Current Features
- **Cross-platform support** (Linux & Windows)
- **Timestamped logging** with detailed timestamps
- **Special key handling** (Ctrl, Alt, Shift, etc.)
- **Automatic log file creation** with timestamps
- **Provided error handling for basic edge cases**
- **Easy stop mechanism** (Ctrl+C)

### Linux Version (`keylgr.py`)
- Logs to `./logs/log_YYYYMMDD_HHMMSS.txt`
- Simple keystroke capture
- Optional stealth mode (commented)

### Windows Version (`winkylgr.py`)
- Smart log directory detection (Documents folder preferred)
- UTF-8 encoding support
- Windows-specific error handling
- Platform detection warnings
- Enhanced stealth options (optional)

## Log Format

```
2024-01-15 14:30:25 - a
2024-01-15 14:30:26 - b
2024-01-15 14:30:27 - Key.space
2024-01-15 14:30:28 - Key.enter
```

## Configuration

### Log Directory
- **Linux**: `./logs/` in current directory
- **Windows**: `~/Documents/logs/` (fallback to `./logs/`)

### Stealth Mode
Uncomment the stealth section in either file for:
- Hidden log directories
- Disguised file names
- Reduced console output

## Dependencies

```
pynput>=1.7.6
```

Install with:
```bash
pip install pynput
```


## Security Considerations

### For Users
- Always run with appropriate permissions
- Monitor log file sizes to prevent disk space issues
- Regularly review and clean old logs
- Use encryption for sensitive environments

### For Developers
- Implement proper access controls
- Add audit logging for administrative actions
- Consider implementing rate limiting
- Add data retention policies

## Troubleshooting

### Common Issues

**Permission Denied**
```bash
# Linux: Run with sudo (if needed)
sudo python keylgr.py

# Windows: Run as Administrator
```

**Import Errors**
```bash
# Install missing dependencies
pip install pynput
```

**Log File Not Created**
- Check write permissions in target directory
- Ensure sufficient disk space
- Verify Python has file creation rights

## Development Notes

### Code Structure
- **Modular design** for easy feature addition
- **Error handling** for robust operation
- **Cross-platform compatibility** considerations
- **Clean code practices** for maintainability

### Testing
- Test on multiple Windows versions (7, 10, 11)
- Test on various Linux distributions
- Verify Unicode character handling
- Test with different keyboard layouts

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is for educational purposes. Use responsibly and in accordance with applicable laws.

## 📞 Support

For issues or questions:
- Check the troubleshooting section
- Review error messages carefully
- Ensure all dependencies are installed
- Test on a clean system first

---

**Remember**: Always use this tool ethically and legally. Respect privacy and only test on systems you own or have explicit permission to monitor. 