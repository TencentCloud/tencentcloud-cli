**Example 1: 获取一个传统型负载均衡的监听器信息**



Input: 

```
tccli clb DescribeClassicalLBListeners --cli-unfold-argument  \
    --LoadBalancerId lb-a3u5l5zc
```

Output: 
```
{
    "Response": {
        "Listeners": [
            {
                "ListenerId": "lbl-3jur3gei",
                "ListenerPort": 80,
                "InstancePort": 8080,
                "ListenerName": "HTTP-LISTENER",
                "Protocol": "tcp",
                "SessionExpire": 0,
                "HealthSwitch": 1,
                "TimeOut": 2,
                "IntervalTime": 5,
                "HealthNum": 3,
                "UnhealthNum": 3,
                "HttpHash": "",
                "HttpCode": 31,
                "HttpCheckPath": "",
                "SSLMode": "",
                "CertId": "",
                "CertCaId": "",
                "Status": 1
            }
        ],
        "RequestId": "5da375f4-214d-42bb-8d50-e74bf556b38f"
    }
}
```

