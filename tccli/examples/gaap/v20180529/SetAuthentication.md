**Example 1: 认证高级配置**



Input: 

```
tccli gaap SetAuthentication --cli-unfold-argument  \
    --ListenerId 0 \
    --Domain a.a.com \
    --BasicAuth 1 \
    --BasicAuthConfId xxx \
    --GaapAuth 1 \
    --GaapCertificateId xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

