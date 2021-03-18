**Example 1: 指定转发规则ID查询重定向关系**



Input: 

```
tccli clb DescribeRewrite --cli-unfold-argument  \
    --LoadBalancerId lb-qc2iq5yc \
    --SourceListenerIds lbl-j36caqde \
    --SourceLocationIds loc-5t7526km
```

Output: 
```
{
    "Response": {
        "RewriteSet": [
            {
                "TargetType": "Node",
                "ListenerId": "lbl-j36caqde",
                "LocationId": "loc-5t7526km",
                "Domain": "www.123.com",
                "Url": "/",
                "Certificate": null,
                "HealthCheck": {
                    "HealthSwitch": 1,
                    "TimeOut": 2,
                    "IntervalTime": 5,
                    "HealthNum": 3,
                    "UnHealthNum": 3,
                    "HttpCode": 15,
                    "HttpCheckPath": "/",
                    "HttpCheckDomain": "www.123.com",
                    "HttpCheckMethod": "get"
                },
                "RewriteTarget": {
                    "TargetListenerId": "lbl-9nj07x0m",
                    "TargetLocationId": "loc-8gdc4qcq"
                },
                "SessionExpireTime": 0,
                "Scheduler": "WRR",
                "HttpGzip": true,
                "BeAutoCreated": false,
                "DefaultServer": false,
                "Http2": false,
                "ForwardType": "HTTP",
                "TrpcCallee": "",
                "QuicStatus": "OFF",
                "TargetGroup": null,
                "WafDomainId": "",
                "TrpcFunc": "",
                "CreateTime": "2020-06-18 19:51:13"
            }
        ],
        "RequestId": "6b4b80ba-12f6-4b7c-9eba-c9203b3bbf1e"
    }
}
```

