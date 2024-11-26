**Example 1: 查询云原生网关分组信息**

查询云原生网关分组信息

Input: 

```
tccli tse DescribeNativeGatewayServerGroups --cli-unfold-argument  \
    --GatewayId gateway-dde03767 \
    --Offset 0 \
    --Limit 1 \
    --Filters.0.Name GroupId \
    --Filters.0.Values group-4se0czf7
```

Output: 
```
{
    "Response": {
        "RequestId": "7c6a2512-8040-4ce7-b8ba-30f1bf585867",
        "Result": {
            "GatewayGroupList": [
                {
                    "GatewayId": "gateway-dde03767",
                    "GroupId": "group-4se0czf7",
                    "Name": "默认分组",
                    "Description": "",
                    "NodeConfig": {
                        "Specification": "16c32g",
                        "Number": 10
                    },
                    "SubnetIds": "subnet-ec94pncc",
                    "InternetMaxBandwidthOut": 15,
                    "Status": "Running",
                    "CreateTime": "2024-03-29 11:02:32",
                    "ModifyTime": "2024-11-08 11:30:36",
                    "IsFirstGroup": 1,
                    "BindingStrategy": {
                        "StrategyId": "strategy-0c509e2d",
                        "StrategyName": "弹性伸缩",
                        "Description": "",
                        "GatewayId": "",
                        "Config": {
                            "MaxReplicas": 0,
                            "Metrics": null
                        },
                        "CreateTime": "",
                        "ModifyTime": "",
                        "CronConfig": {
                            "StrategyId": "",
                            "Enabled": false,
                            "Params": null,
                            "CreateTime": "",
                            "ModifyTime": ""
                        },
                        "MaxReplicas": 0
                    },
                    "DefaultWeight": 20
                }
            ],
            "TotalCount": 1
        }
    }
}
```

