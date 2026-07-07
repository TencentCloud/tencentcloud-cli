**Example 1: 查询自定义安全策略**



Input: 

```
tccli alb DescribeSecurityPolicies --cli-unfold-argument  \
    --MaxResults 20 \
    --SecurityPolicyIds tls-t2ckydug
```

Output: 
```
{
    "Response": {
        "NextToken": "",
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

