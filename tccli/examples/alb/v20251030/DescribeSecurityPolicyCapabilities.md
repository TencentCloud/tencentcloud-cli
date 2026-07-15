**Example 1: 获取支持的安全策略加密套件设置**



Input: 

```
tccli alb DescribeSecurityPolicyCapabilities --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "SecurityPolicyCapabilities": [
            {
                "TLSVersion": "TLSv1.3",
                "Ciphers": [
                    "TLS_AES_128_GCM_SHA256"
                ]
            }
        ],
        "RequestId": "3b848733-70e5-4558-ae39-4b9938eb7609"
    }
}
```

