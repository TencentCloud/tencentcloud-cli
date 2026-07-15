**Example 1: 修改安全策略**



Input: 

```
tccli alb ModifySecurityPolicyAttributes --cli-unfold-argument  \
    --Ciphers TLS_AES_128_GCM_SHA256 \
    --SecurityPolicyId tls-t2ckydug \
    --SecurityPolicyName test-policy2 \
    --TLSVersions TLSv1.1 TLSv1.2
```

Output: 
```
{
    "Response": {
        "RequestId": "3b848733-70e5-4558-ae39-4b9938eb7609"
    }
}
```

