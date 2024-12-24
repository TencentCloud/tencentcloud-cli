**Example 1: 查询网关分组监控明细数据**



Input: 

```
tccli tsf DescribeGroupUseDetail --cli-unfold-argument  \
    --GatewayDeployGroupId group-yd3b588a \
    --GroupId grp-nb08ur29 \
    --StartTime 2024-12-16 16:36:40 \
    --EndTime 2024-12-23 16:36:40 \
    --Count 10
```

Output: 
```
{
    "Response": {
        "RequestId": "76917645-69a0-4692-9555-75e8da464914",
        "Result": {
            "TopAvgTimeCost": [
                {
                    "ApiId": "api-dtbc5cf0",
                    "ApiPath": "/echo/{param}",
                    "ServiceName": "provider-demo",
                    "Value": "12.22782"
                }
            ],
            "TopFailureRate": [
                {
                    "ApiId": "api-dtbc5cf0",
                    "ApiPath": "/echo/{param}",
                    "ServiceName": "provider-demo",
                    "Value": "0.02182"
                }
            ],
            "TopReqAmount": [
                {
                    "ApiId": "api-dtbc5cf0",
                    "ApiPath": "/echo/{param}",
                    "ServiceName": "provider-demo",
                    "Value": "1.3412689E7"
                }
            ]
        }
    }
}
```

