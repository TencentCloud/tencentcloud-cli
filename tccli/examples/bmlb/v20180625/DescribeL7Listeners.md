**Example 1: 获取黑石负载均衡七层监听器列表信息**



Input: 

```
tccli bmlb DescribeL7Listeners --cli-unfold-argument  \
    --LoadBalancerId lb-47gazeml
```

Output: 
```
{
    "Response": {
        "ListenerSet": [
            {
                "ListenerId": "lbl-n0sfq477",
                "ListenerName": "http81",
                "Protocol": "http",
                "LoadBalancerPort": 81,
                "Bandwidth": 0,
                "ListenerType": "L7Listener",
                "SslMode": 0,
                "CertId": "",
                "CertCaId": "",
                "Status": 1,
                "AddTimestamp": "2018-11-06 15:01:49",
                "ForwardProtocol": 0
            },
            {
                "ListenerId": "lbl-ab1tk2vd",
                "ListenerName": "http81",
                "Protocol": "http",
                "LoadBalancerPort": 82,
                "Bandwidth": 0,
                "ListenerType": "L7Listener",
                "SslMode": 0,
                "CertId": "",
                "CertCaId": "",
                "Status": 1,
                "AddTimestamp": "2018-11-06 15:03:43",
                "ForwardProtocol": 0
            }
        ],
        "RequestId": "d1b58ff2-6117-40a8-9429-86644a6ece45"
    }
}
```

