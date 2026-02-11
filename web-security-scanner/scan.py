#!/usr/bin/env python3
"""
Simple Security Header Scanner
Checks websites for missing security headers
"""

import requests
import sys

def scan_website(url):
    """Scan a website for security headers"""
    
    # Ensure URL has protocol
    if not url.startswith('http'):
        url = 'https://' + url
    
    print(f"\n🔍 Scanning: {url}\n")
    
    try:
        # Make request
        response = requests.get(url, timeout=10)
        headers = response.headers
        
        # Security headers to check
        security_headers = {
            'Strict-Transport-Security': 'Protects against SSL stripping',
            'Content-Security-Policy': 'Prevents XSS attacks',
            'X-Frame-Options': 'Prevents clickjacking',
            'X-Content-Type-Options': 'Prevents MIME sniffing',
            'Referrer-Policy': 'Controls referrer information',
        }
        
        score = 0
        found = 0
        
        print("📊 Security Headers:")
        print("-" * 50)
        
        # Check each header
        for header, description in security_headers.items():
            if header in headers:
                print(f"✅ {header}")
                print(f"   {description}")
                print(f"   Value: {headers[header][:60]}...")
                found += 1
                score += 20
            else:
                print(f"❌ {header} - MISSING")
                print(f"   {description}")
            print()
        
        # Calculate grade
        if score >= 80:
            grade = "A"
        elif score >= 60:
            grade = "B"
        elif score >= 40:
            grade = "C"
        else:
            grade = "F"
        
        # Show results
        print("=" * 50)
        print(f"📈 SCORE: {score}/100")
        print(f"📝 GRADE: {grade}")
        print(f"✅ Headers Found: {found}/{len(security_headers)}")
        print("=" * 50)
        
        # Recommendations
        if score < 100:
            print("\n💡 Recommendations:")
            for header, desc in security_headers.items():
                if header not in headers:
                    print(f"   • Add {header} header")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scanner.py <url>")
        print("Example: python scanner.py https://github.com")
        sys.exit(1)
    
    scan_website(sys.argv[1])