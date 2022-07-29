**Example 1: 创建HTTPS监听器**

创建HTTPS监听器

Input: 

```
tccli gaap CreateHTTPSListener --cli-unfold-argument  \
    --ProxyId link-cuxw2rm0 \
    --ForwardProtocol HTTP \
    --CertificateId N4Al2mhF \
    --ListenerName listener-1 \
    --Port 443
```

Output: 
```
{
    "Response": {
        "RequestId": "9aeda369-17c7-429f-be39-745c1e92fc71",
        "ListenerId": "listener-o0f3at99"
    }
}
```

