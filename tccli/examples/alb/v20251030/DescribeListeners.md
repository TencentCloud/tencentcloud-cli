**Example 1: 查询监听器列表**



Input: 

```
tccli alb DescribeListeners --cli-unfold-argument  \
    --LoadBalancerId alb-f8q2xk9m \
    --MaxResults 10
```

Output: 
```
{
    "Response": {
        "LoadBalancerId": "alb-f8q2xk9m",
        "Listeners": [
            {
                "ListenerId": "lst-d9p3k7wa",
                "ListenerName": "443",
                "ListenerProtocol": "HTTPS",
                "ListenerPort": 80,
                "ListenerStatus": "Active",
                "GzipEnabled": false,
                "Http2Enable": false,
                "CaEnable": false,
                "RequestTimeout": 60,
                "IdleTimeout": 15,
                "TlsSecurityPolicyId": "tls-t2ckydug",
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
                "Tags": []
            }
        ],
        "TotalCount": 1,
        "MaxResults": 1,
        "NextToken": "",
        "RequestId": "1d92eab2-8e5b-4c29-b1b8-4454479c7196"
    }
}
```

