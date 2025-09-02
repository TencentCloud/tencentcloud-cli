**Example 1: 关闭MCP Server**

关闭指定实例下的MCP Server。

Input: 

```
tccli lighthouse StopMcpServers --cli-unfold-argument  \
    --InstanceId lhins-5h3s0lht \
    --McpServerIds lhms-p2dophob
```

Output: 
```
{
    "Response": {
        "RequestId": "6cab721b-7a7f-4438-82f9-d19f1bb5a45a"
    }
}
```

