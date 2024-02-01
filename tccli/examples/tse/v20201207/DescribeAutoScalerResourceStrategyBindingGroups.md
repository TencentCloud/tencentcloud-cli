**Example 1: 查看弹性伸缩策略绑定的网关分组**

查看弹性伸缩策略绑定的网关分组

Input: 

```
tccli tse DescribeAutoScalerResourceStrategyBindingGroups --cli-unfold-argument  \
    --GatewayId <GatewayId> \
    --StrategyId strategy-7bb4fcb0 \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "RequestId": "adc44984-762c-42e0-b39a-80777e5c3bcc",
        "Result": {
            "TotalCount": 1,
            "GroupInfos": [
                {
                    "GroupId": "group-2e781178",
                    "GroupName": "test",
                    "NodeConfig": {
                        "Specification": "1c2g",
                        "Number": 2
                    },
                    "BindTime": "2021-09-09 11:52:30",
                    "Status": "bound"
                }
            ]
        }
    }
}
```

