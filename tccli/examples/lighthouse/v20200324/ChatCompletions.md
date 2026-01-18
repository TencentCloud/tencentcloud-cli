**Example 1: 流式调用对话生成接口**

通过对话的方式实现自定义 MCP Server 的需求澄清、代码生成和代码修改

Input: 

```
tccli lighthouse ChatCompletions --cli-unfold-argument  \
    --Messages.0.Role user \
    --Messages.0.Content 帮我写一个Python的HTTP服务器 \
    --SessionId sess_31180231ca66
```

Output: 
```
HTTP/1.1 200 OK
Cache-Control: no-cache
Connection: keep-alive
Content-Type: text/event-stream
Date: Tue, 21 Nov 2025 06:56:00 GMT
Transfer-Encoding: chunked
X-TC-RequestId: 61a8459b-27c8-4868-af8f-f374db0223d6

data: {"Content": "输出","SessionId":"sess_31180231ca66","Node":"code_generation","RequestId": "61a8459b-27c8-4868-af8f-f374db0223d6"}
data: {"Content": "示例","SessionId":"sess_31180231ca66","Node":"code_generation","RequestId": "61a8459b-27c8-4868-af8f-f374db0223d6"}
```

