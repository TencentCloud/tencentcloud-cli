**Example 1: 获取采集规则配置所绑定的机器组**



Input: 

```
tccli cls DescribeConfigMachineGroups --cli-unfold-argument  \
    --ConfigId xxxxxxxxxx
```

Output: 
```
{
    "Response": {
        "MachineGroups": [
            {
                "GroupId": "xxxx-xx-xx-xx-yyyyyyyy",
                "GroupName": "testgroup",
                "MachineGroupType": {
                    "Type": "ip",
                    "Values": [
                        "10.10.1.119"
                    ]
                },
                "CreateTime": "xx"
            }
        ],
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

