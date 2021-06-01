**Example 1: 获取机器组列表**



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
        "TotalCount": 10,
        "MachineGroups": [
            {
                "GroupId": "57f5808c-4a55-11eb-b378-0242ac130002",
                "GroupName": "testgroup",
                "MachineGroupType": {
                    "Type": "ip",
                    "Values": [
                        "10.10.1.119"
                    ]
                },
                "CreateTime": "2020-10-11 19:22:33"
            }
        ],
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

