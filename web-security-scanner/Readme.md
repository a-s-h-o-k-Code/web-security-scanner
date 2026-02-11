# Security Header Scanner

A simple tool to check if websites have important security headers.

## What it does

Scans websites and checks for 5 critical security headers:
- **Strict-Transport-Security** - Forces HTTPS
- **Content-Security-Policy** - Prevents XSS attacks  
- **X-Frame-Options** - Prevents clickjacking
- **X-Content-Type-Options** - Prevents MIME sniffing
- **Referrer-Policy** - Controls referrer info

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python scanner.py https://example.com
```

## Example Output

```
🔍 Scanning: https://github.com

📊 Security Headers:
--------------------------------------------------
✅ Strict-Transport-Security
   Protects against SSL stripping
   Value: max-age=31536000; includeSubDomains; preload...

❌ Content-Security-Policy - MISSING
   Prevents XSS attacks

==================================================
📈 SCORE: 60/100
📝 GRADE: B
✅ Headers Found: 3/5
==================================================
```

## How it works

1. Takes a URL as input
2. Makes HTTP request to the website
3. Checks response headers for security headers
4. Gives a score (0-100) and grade (A-F)
5. Shows which headers are missing

## Grading

- **A**: 80-100 points (4-5 headers)
- **B**: 60-79 points (3 headers)
- **C**: 40-59 points (2 headers)
- **F**: 0-39 points (0-1 headers)

## Why This Matters

Security headers protect websites from:
- Man-in-the-middle attacks
- Cross-site scripting (XSS)
- Clickjacking
- Data theft
- Session hijacking

## License

MIT