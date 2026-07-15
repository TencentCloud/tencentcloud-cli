**Example 1: 查询监听器详情**



Input: 

```
tccli alb DescribeListenerDetail --cli-unfold-argument  \
    --LoadBalancerId alb-f8q2xk9m \
    --ListenerId lst-d9p3k7wa
```

Output: 
```
{
    "Response": {
        "LoadBalancerId": "alb-f8q2xk9m",
        "ListenerId": "lst-d9p3k7wa",
        "ListenerName": "443",
        "ListenerPort": 80,
        "ListenerProtocol": "HTTPS",
        "ListenerStatus": "Active",
        "CertificateIds": [
            "Fm8Wp7x8"
        ],
        "CaCertificateIds": [],
        "GzipEnabled": false,
        "CaEnabled": false,
        "Http2Enabled": false,
        "SecurityPolicyId": "tls-t2ckydug",
        "IdleTimeout": 15,
        "RequestTimeout": 60,
        "XForwardedForConfig": {
            "XForwardedForMode": "append",
            "XForwardedForProtoEnabled": false,
            "XForwardedForPortEnabled": false,
            "XForwardedForHostEnabled": false,
            "XForwardedForClientSrcPortEnabled": false,
            "XTencentClientSDNEnabled": false,
            "XTencentClientIDNEnabled": false,
            "XTencentClientSerialEnabled": false,
            "XTencentClientVerifyEnabled": false
        },
        "DefaultActions": [
            {
                "Type": "TargetGroup",
                "TargetGroupConfig": {
                    "TargetGroups": [
                        {
                            "TargetGroupId": "lbtg-0zrnc9qa",
                            "Weight": 10
                        }
                    ]
                }
            }
        ],
        "Tags": [],
        "RequestId": "cb7e17c7-9e71-42d2-9fa6-ed98bef10c93"
    }
}
```

