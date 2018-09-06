#!/usr/bin/env python3

from app import webapp

if __name__ == '__main__':
    webapp.run(host='0.0.0.0', port=8000, debug=True)
