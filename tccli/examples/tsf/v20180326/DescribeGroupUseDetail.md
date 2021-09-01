**Example 1: 查询网关分组监控明细数据**



Input: 

```
tccli tsf DescribeGroupUseDetail --cli-unfold-argument  \
    --Count 10 \
    --GroupId group-i54lzdrq \
    --EndTime '2020-09-22 00:00:00' \
    --StartTime '2020-09-22 00:00:00' \
    --GatewayDeployGroupId group-dasdas
```

Output: 
```
{
    "Response": {
        "Result": {
            "TopReqAmount": [
                {
                    "ApiPath": "/v1/user/{userId}",
                    "ServiceName": "provider-demo",
                    "ApiId": "xx",
                    "Value": "16000"
                }
            ],
            "TopFailureRate": [
                {
                    "ApiPath": "/v1/user/{userId}",
                    "ServiceName": "provider-demo",
                    "ApiId": "xx",
                    "Value": "0.80000"
                }
            ],
            "TopAvgTimeCost": [
                {
                    "ApiPath": "/v1/user/{userId}",
                    "ServiceName": "provider-demo",
                    "ApiId": "xx",
                    "Value": "0.23265"
                }
            ]
        },
        "RequestId": "5d996e05507e42d5970cd2e25ed5267a"
    }
}
```

