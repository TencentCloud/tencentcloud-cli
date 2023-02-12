**Example 1: 指定转发规则ID查询重定向关系**

指定转发规则ID查询重定向关系

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
                "DefaultServer": false,
                "Certificate": {
                    "SSLMode": "UNIDIRECTIONAL",
                    "CertCaId": "xx",
                    "CertId": "xx",
                    "ExtCertIds": [
                        "xx"
                    ]
                },
                "TrpcCallee": "abc",
                "ListenerId": "lbl-xxxxxxxx",
                "WafDomainId": "xx",
                "HttpGzip": true,
                "Scheduler": "WRR",
                "TargetGroupList": [
                    {
                        "TargetGroupId": "lbtg-xxxxxxxx",
                        "TargetGroupName": "testGroup"
                    }
                ],
                "TargetGroup": {
                    "TargetGroupId": "lbtg-xxxxxxxx",
                    "TargetGroupName": "testGroup"
                },
                "Url": "/",
                "HealthCheck": {
                    "RecvContext": "test",
                    "HealthSwitch": 1,
                    "HttpCheckPath": "/check",
                    "HttpCheckMethod": "head",
                    "UnHealthNum": 3,
                    "IntervalTime": 5,
                    "HttpCode": 15,
                    "SourceIpType": 0,
                    "CheckPort": 0,
                    "ContextType": "HTTP",
                    "HttpCheckDomain": "test.xxx.com",
                    "ExtendedCode": "12",
                    "HealthNum": 3,
                    "TimeOut": 2,
                    "CheckType": "TCP ",
                    "SendContext": "abc",
                    "HttpVersion": "HTTP/1.0"
                },
                "TrpcFunc": "trpcfunc_xxx",
                "Http2": false,
                "Domains": [
                    "test.abc.com"
                ],
                "BeAutoCreated": false,
                "Domain": "test.abc.com",
                "ForwardType": "HTTP",
                "RewriteTarget": {
                    "TargetListenerId": "lbl-xxxxxxxx",
                    "RewriteType": "Manual",
                    "RewriteCode": 0,
                    "TargetLocationId": "loc-xxxxxxxx",
                    "TakeUrl": true
                },
                "QuicStatus": "OFF",
                "LocationId": "loc-xxxxxxxx",
                "SessionExpireTime": 0,
                "CreateTime": "2022-03-23 10:37:16"
            }
        ],
        "RequestId": "63bee47c-2bf9-4909-a8f7-67495dfe7b42"
    }
}
```

