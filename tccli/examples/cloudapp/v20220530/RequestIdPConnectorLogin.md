**Example 1: 生成IdP连接器登录请求**



Input: 

```
tccli cloudapp RequestIdPConnectorLogin --cli-unfold-argument  \
    --CloudappId cloudapp-1m42xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "72cc6463-0f4b-b376-2a19-6d936e7d10a2",
        "SAMLRequestBase64": "9IiIgQXNzZXJ0aW9uQ29uc...",
        "SingleSignOnService": "https://your.idp/login"
    }
}
```

