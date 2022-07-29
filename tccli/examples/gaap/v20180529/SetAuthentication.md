**Example 1: 认证高级配置**



Input: 

```
tccli gaap SetAuthentication --cli-unfold-argument  \
    --Domain a.a.com \
    --GaapAuth 1 \
    --GaapCertificateId xxx \
    --ListenerId 0 \
    --BasicAuthConfId xxx \
    --BasicAuth 1
```

Output: 
```
{
    "Response": {
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

