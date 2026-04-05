**Example 1: 查询监听器**



Input: 

```
tccli ga2 DescribeListeners --cli-unfold-argument  \
    --GlobalAcceleratorId ga-80bzejka
```

Output: 
```
{
    "Response": {
        "ListenerSet": [
            {
                "GlobalAcceleratorId": "ga-reu65tl8",
                "ListenerId": "lsr-cu9t0glx",
                "Name": "diozhou_tcp_test_8888",
                "Description": "",
                "Protocol": "TCP",
                "PortRanges": {
                    "FromPort": 8888,
                    "ToPort": 8888
                },
                "XForwardedForRealIp": false,
                "ClientAffinity": "Close",
                "ClientAffinityTime": 0,
                "RequestTimeout": 60,
                "CertificationType": "UNIDIRECTIONAL",
                "ServerCertificates": [],
                "ClientCaCertificates": [],
                "CipherPolicyId": "",
                "HttpVersion": "HTTP/1.1",
                "CreateTime": "2025-04-04 14:11:42",
                "ListenerType": "Standard",
                "Status": "ACTIVE",
                "EndpointGroupCounts": 1
            }
        ],
        "RequestId": "7ecf173c-1cd3-46a9-afe0-5c18fbd04202",
        "TotalCount": 1
    }
}
```

