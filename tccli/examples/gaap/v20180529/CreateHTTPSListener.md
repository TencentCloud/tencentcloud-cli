**Example 1: 创建HTTPS监听器**



Input: 

```
tccli gaap CreateHTTPSListener --cli-unfold-argument  \
    --ListenerName listener-name-https \
    --Port 8092 \
    --CertificateId cert-etww5bkh \
    --ForwardProtocol HTTP \
    --ProxyId link-p9888rix
```

Output: 
```
{
    "Response": {
        "ListenerId": "listener-0ld1mlud",
        "RequestId": "a0a814a0-aa2e-41bb-a139-e2ec2915acb6"
    }
}
```

