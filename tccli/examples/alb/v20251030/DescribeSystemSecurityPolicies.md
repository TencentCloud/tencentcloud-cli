**Example 1: 查询系统安全策略**



Input: 

```
tccli alb DescribeSystemSecurityPolicies --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "SecurityPolicies": [
            {
                "SecurityPolicyId": "tls-t2ckydug",
                "SecurityPolicyName": "test-policy",
                "Status": "Active",
                "TLSVersions": [
                    "TLSv1.2",
                    "TLSv1.3"
                ],
                "Ciphers": [
                    "TLS_AES_128_GCM_SHA256"
                ],
                "CreateTime": "2025-01-01T08:30:00+08:00",
                "Tags": []
            }
        ],
        "TotalCount": 1,
        "RequestId": "3b848733-70e5-4558-ae39-4b9938eb7609"
    }
}
```

