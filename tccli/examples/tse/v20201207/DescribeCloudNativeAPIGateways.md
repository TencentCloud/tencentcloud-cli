**Example 1: 测试获取云原生API网关实例列表**



Input: 

```
tccli tse DescribeCloudNativeAPIGateways --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "adc44984-762c-42e0-b39a-80777e5c3bcc",
        "Result": {
            "TotalCount": 1,
            "GatewayList": [
                {
                    "CreateTime": "2021-09-09 11:52:30",
                    "Description": "测试",
                    "GatewayId": "gateway-7bb4fcb0",
                    "GatewayVersion": "2.4.1",
                    "Name": "test",
                    "NodeConfig": {
                        "Number": 2,
                        "Specification": "1c2g"
                    },
                    "Status": "Creating",
                    "Type": "Kong",
                    "VpcConfig": {
                        "SubnetId": "subnet-xxx",
                        "VpcId": "vpc-xxx"
                    },
                    "Tags": [
                        {
                            "TagKey": "xx",
                            "TagValue": "xx"
                        }
                    ]
                }
            ]
        }
    }
}
```

