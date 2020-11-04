**Example 1: 获取黑石负载均衡四层监听器**



Input: 

```
tccli bmlb DescribeL4Listeners --cli-unfold-argument  \
    --LoadBalancerId lb-m1i50ynj
```

Output: 
```
{
    "Response": {
        "ListenerSet": [
            {
                "ListenerId": "lbl-7liurquj",
                "ListenerName": "1000",
                "Protocol": "tcp",
                "LoadBalancerPort": 1000,
                "Bandwidth": 0,
                "ListenerType": "L4Listener",
                "SessionExpire": 0,
                "HealthSwitch": 0,
                "TimeOut": 2,
                "IntervalTime": 5,
                "HealthNum": 2,
                "UnhealthNum": 2,
                "CustomHealthSwitch": 0,
                "InputType": "",
                "LineSeparatorType": 0,
                "HealthRequest": "",
                "HealthResponse": "",
                "ToaFlag": 0,
                "Status": 1,
                "AddTimestamp": "2018-10-22 15:10:00",
                "BalanceMode": ""
            }
        ],
        "RequestId": "54902038-e18f-4ba6-90d2-a4b5a099d67c"
    }
}
```

