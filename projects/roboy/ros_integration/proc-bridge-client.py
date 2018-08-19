from procbridge import procbridge


host = '127.0.0.1'
port = 8877

client = procbridge.ProcBridge(host, port)

print(client.request("",{"text_input": "hello how are you sir?"}))
