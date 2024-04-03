**Example 1: 按照端口、协议及监听器ID查询监听器**



Input: 

```
tccli clb DescribeListeners --cli-unfold-argument  \
    --LoadBalancerId lb-aniq7ewx \
    --Protocol TCP \
    --Port 333 \
    --ListenerIds lbl-hd9nfp6o
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Listeners": [
            {
                "ListenerId": "lbl-hd9nfp6o",
                "ListenerName": "12345",
                "CreateTime": "2020-12-31 12:03:36",
                "Protocol": "TCP",
                "Port": 333,
                "EndPort": 0,
                "HealthCheck": {
                    "HealthSwitch": 1,
                    "TimeOut": 2,
                    "IntervalTime": 5,
                    "HealthNum": 3,
                    "UnHealthNum": 3,
                    "CheckPort": null,
                    "CheckType": "TCP",
                    "HttpCheckDomain": null,
                    "HttpCheckPath": null,
                    "HttpCheckMethod": null,
                    "HttpVersion": null,
                    "HttpCode": null,
                    "ContextType": null,
                    "SendContext": null,
                    "RecvContext": null,
                    "ExtendedCode": null,
                    "SourceIpType": 0
                },
                "Certificate": null,
                "Scheduler": "WRR",
                "SessionExpireTime": 0,
                "SniSwitch": 0,
                "Rules": null,
                "TargetType": "NODE",
                "TargetGroup": null,
                "KeepaliveEnable": null,
                "SessionType": "NORMAL",
                "Toa": false,
                "DeregisterTargetRst": false,
                "MaxConn": 100,
                "MaxCps": 100,
                "IdleConnectTimeout": 0,
                "AttrFlags": [
                    "abc"
                ],
                "TargetGroupList": null
            }
        ],
        "RequestId": "3ddae670-4a89-4919-af6e-0d6bf195c92e"
    }
}
```

**Example 2: 查询负载均衡实例下的全部监听器信息**



Input: 

```
tccli clb DescribeListeners --cli-unfold-argument  \
    --LoadBalancerId lb-aniq7ewx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Listeners": [
            {
                "ListenerId": "lbl-hd9nfp6o",
                "ListenerName": "12345",
                "CreateTime": "2020-12-31 12:03:36",
                "Protocol": "TCP",
                "Port": 333,
                "EndPort": 0,
                "HealthCheck": {
                    "HealthSwitch": 1,
                    "TimeOut": 2,
                    "IntervalTime": 5,
                    "HealthNum": 3,
                    "UnHealthNum": 3,
                    "CheckPort": null,
                    "CheckType": "TCP",
                    "HttpCheckDomain": null,
                    "HttpCheckPath": null,
                    "HttpCheckMethod": null,
                    "HttpVersion": null,
                    "HttpCode": null,
                    "ContextType": null,
                    "SendContext": null,
                    "RecvContext": null,
                    "ExtendedCode": null,
                    "SourceIpType": 0
                },
                "Certificate": null,
                "Scheduler": "WRR",
                "SessionExpireTime": 0,
                "SniSwitch": 0,
                "Rules": null,
                "TargetType": "NODE",
                "TargetGroup": null,
                "KeepaliveEnable": null,
                "SessionType": "NORMAL",
                "Toa": false,
                "DeregisterTargetRst": false,
                "MaxConn": 100,
                "MaxCps": 100,
                "IdleConnectTimeout": 0,
                "AttrFlags": [
                    "abc"
                ],
                "TargetGroupList": null
            }
        ],
        "RequestId": "3ddae670-4a89-4919-af6e-0d6bf195c92e"
    }
}
```

