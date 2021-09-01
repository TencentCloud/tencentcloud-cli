**Example 1: 查找绑定了某主机或者指定监听器名称的黑石负载均衡四层监听器**



Input: 

```
tccli bmlb DescribeL4ListenerInfo --cli-unfold-argument  \
    --LoadBalancerId lb-dyxceyv5
```

Output: 
```
{
    "Response": {
        "ListenerSet": [
            {
                "ListenerId": "lbl-i4go349z",
                "ListenerName": "test_name",
                "Protocol": "tcp",
                "LoadBalancerPort": 3000,
                "Bandwidth": 0,
                "ListenerType": "L4Listener",
                "SessionExpire": 900,
                "HealthSwitch": 1,
                "TimeOut": 50,
                "IntervalTime": 300,
                "HealthNum": 3,
                "UnhealthNum": 4,
                "Status": 1,
                "AddTimestamp": "2018-10-22 09:41:44"
            },
            {
                "ListenerId": "lbl-e9ao84sl",
                "ListenerName": "4000",
                "Protocol": "udp",
                "LoadBalancerPort": 4000,
                "Bandwidth": 0,
                "ListenerType": "L4Listener",
                "SessionExpire": 0,
                "HealthSwitch": 0,
                "TimeOut": 2,
                "IntervalTime": 5,
                "HealthNum": 2,
                "UnhealthNum": 2,
                "Status": 1,
                "AddTimestamp": "2018-10-22 09:44:05"
            }
        ],
        "RequestId": "37542dd8-359b-4482-8736-b36001ad363c"
    }
}
```

