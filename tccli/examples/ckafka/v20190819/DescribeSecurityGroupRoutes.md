**Example 1: 获取安全组路由信息列表**



Input: 

```
tccli ckafka DescribeSecurityGroupRoutes --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Result": {
            "SecurityGroupRoutes": [
                {
                    "InstanceRoute": {
                        "InstanceId": "ckafka-test",
                        "RouteId": 1234
                    },
                    "SecurityGroupIds": [],
                    "InstanceName": "ckafka测试",
                    "VpcId": "vpc-test",
                    "Vip": "10.0.0.5"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "test-reqId-1134"
    }
}
```

