**Example 1: 获取机器组列表**

获取包含指定标签的机器组列表

Input: 

```
tccli cls DescribeMachineGroups --cli-unfold-argument  \
    --Filters.0.Key tagKey \
    --Filters.0.Values k1 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "MachineGroups": [
            {
                "GroupId": "4a4ee397-xxxx-466f-a04c-b3413b9db40c",
                "GroupName": "cos-recharge",
                "MachineGroupType": {
                    "Type": "label",
                    "Values": [
                        "cos-recharge"
                    ]
                },
                "CreateTime": "2022-02-13 21:07:54",
                "AutoUpdate": "",
                "UpdateStartTime": "",
                "UpdateEndTime": "",
                "ServiceLogging": true,
                "DelayCleanupTime": 30,
                "MetaTags": [],
                "Tags": []
            }
        ],
        "TotalCount": 1,
        "RequestId": "2dc17eaa-xxxx-40ea-8cdc-650aa85ccb80"
    }
}
```

