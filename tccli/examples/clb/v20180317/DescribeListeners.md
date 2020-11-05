**Example 1: Querying listeners by port, protocol, and listener ID**



Input: 

```
tccli clb DescribeListeners --cli-unfold-argument  \
    --LoadBalancerId lb-aniq7ewx\
    --Protocol TCP\
    --Port 333\
    --ListenerIds lbl-pt4dgkjn
```

Output: 
```
{
    "Response": {
        "Listeners": [
            {
                "ListenerId": "lbl-pt4dgkjn",
                "ListenerName": "333",
                "Protocol": "TCP",
                "Port": 333,
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
                "Rules": null
            }
        ],
        "RequestId": "0dc33bce-5fe5-4ce0-9734-d8212c258d36"
    }
}
```

**Example 2: Querying the information of all listeners in a CLB instance**



Input: 

```
tccli clb DescribeListeners --cli-unfold-argument  \
    --LoadBalancerId lb-aniq7ewx
```

Output: 
```
{
    "Response": {
        "Listeners": [
            {
                "ListenerId": "lbl-mdam9r0l",
                "ListenerName": "ds",
                "Protocol": "HTTPS",
                "Port": 1,
                "HealthCheck": null,
                "Certificate": {
                    "SSLMode": "UNIDIRECTIONAL",
                    "CertId": "V0ODELy7",
                    "CertCaId": ""
                },
                "Scheduler": null,
                "SessionExpireTime": null,
                "SniSwitch": 0,
                "Rules": [
                    {
                        "ListenerId": "lbl-mdam9r0l",
                        "LocationId": "loc-33laioar",
                        "Domain": "4.com",
                        "Url": "/df",
                        "Certificate": null,
                        "HealthCheck": {
                            "HealthSwitch": 1,
                            "TimeOut": 2,
                            "IntervalTime": 5,
                            "HealthNum": 3,
                            "UnHealthNum": 3,
                            "HttpCode": 15,
                            "HttpCheckPath": "/",
                            "HttpCheckDomain": "4.com",
                            "HttpCheckMethod": "get",
                            "CheckPort": null,
                            "CheckType": null,
                            "HttpVersion": null,
                            "ContextType": null,
                            "SendContext": null,
                            "RecvContext": null
                        },
                        "RewriteTarget": {
                            "TargetListenerId": null,
                            "TargetLocationId": null
                        },
                        "SessionExpireTime": 0,
                        "Scheduler": "WRR",
                        "HttpGzip": true,
                        "BeAutoCreated": false,
                        "DefaultServer": false,
                        "Http2": false,
                        "ForwardType": "HTTP"
                    }
                ]
            },
            {
                "ListenerId": "lbl-pt4dgkjn",
                "ListenerName": "333",
                "Protocol": "TCP",
                "Port": 333,
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
                "Rules": null
            }
        ],
        "RequestId": "a031471a-332d-4c45-a123-0bc6fb212780"
    }
}
```

