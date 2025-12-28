import http.server
import socketserver
import os

class RedirectHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 记录原始请求路径
        original_path = self.path
        
        # 如果是根目录访问，强制重定向到index.html
        if self.path == '/':
            self.path = '/index.html'
            print(f"🔀 重定向: / -> /index.html")
        
        # 调用父类方法处理修改后的路径
        super().do_GET()
        
        # 记录访问日志
        if original_path != self.path:
            print(f"📊 访问统计: {original_path} -> {self.path}")

PORT = 12345

print("=" * 50)
print("🚀 强制重定向服务器启动")
print("=" * 50)

# 检查index.html是否存在
if not os.path.exists('index.html'):
    print("❌ 错误: 未找到index.html文件!")
    print("💡 请确保你的主页文件命名为'index.html'")
    exit(1)

print("✅ 找到index.html文件")

with socketserver.TCPServer(("", PORT), RedirectHandler) as httpd:
    print(f"📍 访问地址: http://localhost:{PORT}")
    print("🎯 现在访问根目录会自动显示index.html")
    print("=" * 50)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 服务器已关闭")