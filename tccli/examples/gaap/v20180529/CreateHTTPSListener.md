**Example 1: 创建HTTPS监听器**

创建HTTPS监听器

Input: 

```
tccli gaap CreateHTTPSListener --cli-unfold-argument  \
    --InstanceId link-cuxw2rm0 \
    --ListenerName listener-1 \
    --Port 443 \
    --CertificateId N4Al2mhF \
    --ForwardProtocol HTTP
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

