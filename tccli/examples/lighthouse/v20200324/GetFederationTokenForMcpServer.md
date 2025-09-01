**Example 1: 获取MCP Server上传凭证**

获取MCP Server上传凭证。

Input: 

```
tccli lighthouse GetFederationTokenForMcpServer --cli-unfold-argument  \
    --McpServerProjectId lhmsp-12345678
```

Output: 
```
{
    "Response": {
        "Credentials": {
            "SecretId": "AKID***",
            "SecretKey": "q95K***",
            "Token": "da1e***"
        },
        "CosBucketName": "lighthouse-mcp-server-123456789",
        "CosRegion": "ap-guangzhou",
        "CosKeyPrefix": "mcp_server_agent_generated/actived/12345/lhmsp-12345678/",
        "CosDomain": "lighthouse-mcp-server-123456789.cos.ap-guangzhou.myqcloud.com",
        "RequestId": "f3b2a1b5-f2c1-4e5a-8b9c-0d1e2f3a4b5c"
    }
}
```

