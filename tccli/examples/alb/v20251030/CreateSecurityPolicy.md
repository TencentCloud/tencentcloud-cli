**Example 1: 创建自定义安全策略**



Input: 

```
tccli alb CreateSecurityPolicy --cli-unfold-argument  \
    --Ciphers TLS_AES_128_GCM_SHA256 \
    --SecurityPolicyName test-policy \
    --TLSVersions TLSv1.2 TLSv1.3 \
    --Tags.0.TagKey key-xxx \
    --Tags.0.TagValue value-xxx
```

Output: 
```
{
    "Response": {
        "SecurityPolicyId": "tls-t2ckydug",
        "RequestId": "3b848733-70e5-4558-ae39-4b9938eb7609"
    }
}
```

