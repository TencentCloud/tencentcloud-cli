**Example 1: 查询终端节点服务列表**



Input: 

```
tccli vpc DescribeVpcEndPointService --cli-unfold-argument  \
    --EndPointServiceIds vpcsvc-kngiybxl \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "EndPointServiceSet": [
            {
                "VpcId": "vpc-hj3he929",
                "EndPointSet": {},
                "AutoAcceptFlag": "False",
                "ServiceInstanceId": "lb-nswq8wkq",
                "ServiceName": "test_002",
                "EndPointServiceId": "vpcsvc-pnpcflil",
                "ServiceVip": "10.101.1.11",
                "CreateTime": "2021-04-12 19:22:43",
                "ServiceOwner": "1254277469",
                "EndPointCount": 0
            }
        ],
        "RequestId": "452e8b38-10a1-4d8a-8a31-a64b89c8f565"
    }
}
```

