**Example 1: 查询云原生网关分组信息**



Input: 

```
tccli tse DescribeNativeGatewayServerGroups --cli-unfold-argument  \
    --GatewayId xx
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "GatewayGroupList": [
                {
                    "Status": "xx",
                    "Description": "xx",
                    "GroupId": "xx",
                    "NodeConfig": {
                        "Specification": "xx",
                        "Number": 0
                    },
                    "IsFirstGroup": 0,
                    "CreateTime": "xx",
                    "Name": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

