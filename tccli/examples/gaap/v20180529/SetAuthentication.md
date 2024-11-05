**Example 1: 认证高级配置**



Input: 

```
tccli gaap SetAuthentication --cli-unfold-argument  \
    --Domain www.baidu.com \
    --GaapAuth 1 \
    --GaapCertificateId cert-ndqyqw8h \
    --ListenerId listener-0s9kb7qt \
    --BasicAuth 0 \
    --RealServerAuth 0
```

Output: 
```
{
    "Response": {
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

