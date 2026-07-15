**Example 1: 查询安全策略关联关系**



Input: 

```
tccli alb DescribeSecurityPolicyRelations --cli-unfold-argument  \
    --SecurityPolicyIds tls-t2ckydug
```

Output: 
```
{
    "Response": {
        "SecurityPolicyRelations": [
            {
                "SecurityPolicyId": "tls-t2ckydug",
                "RelatedListeners": [
                    {
                        "LoadBalancerId": "alb-f8q2xk9m",
                        "ListenerId": "lst-d9p3k7wa",
                        "ListenerProtocol": "HTTPS",
                        "ListenerPort": 443
                    }
                ]
            }
        ],
        "RequestId": "3b848733-70e5-4558-ae39-4b9938eb7609"
    }
}
```

