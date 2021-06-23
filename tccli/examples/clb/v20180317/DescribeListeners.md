**Example 1: 查询负载均衡实例下的全部监听器信息**



Input: 

```
tccli clb DescribeListeners --cli-unfold-argument  \
    --LoadBalancerId lb-aniq7ewx
```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "Listeners": [
            {
                "ListenerId": "lbl-2ytsji1u",
                "ListenerName": "555",
                "CreateTime": "2020-12-31 11:36:18",
                "Protocol": "HTTP",
                "Port": 555,
                "EndPort": 0,
                "HealthCheck": null,
                "Certificate": null,
                "Scheduler": null,
                "SessionExpireTime": null,
                "SniSwitch": 0,
                "Rules": [
                    {
                        "ListenerId": "lbl-2ytsji1u",
                        "LocationId": "loc-nq5fuotq",
                        "Domain": "www.123.com",
                        "Url": "/123",
                        "CreateTime": "2020-12-31 11:36:48",
                        "Certificate": null,
                        "HealthCheck": {
                            "HealthSwitch": 1,
                            "TimeOut": 5,
                            "IntervalTime": 5,
                            "HealthNum": 3,
                            "UnHealthNum": 3,
                            "HttpCode": 15,
                            "HttpCheckPath": "/",
                            "HttpCheckDomain": "www.123.com",
                            "HttpCheckMethod": "get",
                            "CheckPort": null,
                            "CheckType": "TCP",
                            "HttpVersion": null,
                            "ContextType": null,
                            "SendContext": null,
                            "RecvContext": null
                        },
                        "RewriteTarget": {
                            "TargetListenerId": null,
                            "TargetLocationId": null,
                            "RewriteCode": null,
                            "TakeUrl": null,
                            "RewriteType": null
                        },
                        "SessionExpireTime": 0,
                        "Scheduler": "WRR",
                        "HttpGzip": true,
                        "BeAutoCreated": false,
                        "DefaultServer": true,
                        "Http2": false,
                        "ForwardType": "HTTP",
                        "TargetType": "NODE",
                        "TargetGroup": null,
                        "WafDomainId": "",
                        "TrpcCallee": "",
                        "TrpcFunc": "",
                        "QuicStatus": "OFF"
                    }
                ],
                "TargetType": null,
                "TargetGroup": null,
                "KeepaliveEnable": 0,
                "SessionType": "NORMAL",
                "Toa": false,
                "DeregisterTargetRst": false
            },
            {
                "ListenerId": "lbl-a459zzae",
                "ListenerName": "222",
                "CreateTime": "2020-12-10 20:26:54",
                "Protocol": "HTTP",
                "Port": 222,
                "EndPort": 0,
                "HealthCheck": null,
                "Certificate": null,
                "Scheduler": null,
                "SessionExpireTime": null,
                "SniSwitch": 0,
                "Rules": [
                    {
                        "ListenerId": "lbl-a459zzae",
                        "LocationId": "loc-7pbxg3d4",
                        "Domain": "www.123.com",
                        "Url": "/",
                        "CreateTime": "2020-12-10 20:33:14",
                        "Certificate": null,
                        "HealthCheck": {
                            "HealthSwitch": 1,
                            "TimeOut": 5,
                            "IntervalTime": 5,
                            "HealthNum": 3,
                            "UnHealthNum": 3,
                            "HttpCode": 15,
                            "HttpCheckPath": "/",
                            "HttpCheckDomain": "www.123.com",
                            "HttpCheckMethod": "get",
                            "CheckPort": null,
                            "CheckType": "TCP",
                            "HttpVersion": null,
                            "ContextType": null,
                            "SendContext": null,
                            "RecvContext": null
                        },
                        "RewriteTarget": {
                            "TargetListenerId": null,
                            "TargetLocationId": null,
                            "RewriteCode": null,
                            "TakeUrl": null,
                            "RewriteType": null
                        },
                        "SessionExpireTime": 0,
                        "Scheduler": "WRR",
                        "HttpGzip": true,
                        "BeAutoCreated": false,
                        "DefaultServer": true,
                        "Http2": false,
                        "ForwardType": "HTTP",
                        "TargetType": "NODE",
                        "TargetGroup": null,
                        "WafDomainId": "",
                        "TrpcCallee": "",
                        "TrpcFunc": "",
                        "QuicStatus": "OFF"
                    }
                ],
                "TargetType": null,
                "TargetGroup": null,
                "KeepaliveEnable": 0,
                "SessionType": "NORMAL",
                "Toa": false,
                "DeregisterTargetRst": false
            }
        ],
        "RequestId": "2682e290-3f8c-4766-98fa-716610e2d351"
    }
}
```

**Example 2: 按照端口、协议及监听器ID查询监听器**



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
                    "RecvContext": null
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
                "DeregisterTargetRst": false
            }
        ],
        "RequestId": "3ddae670-4a89-4919-af6e-0d6bf195c92e"
    }
}
```

