**Example 1: 获取采集规则配置所绑定的机器组**

获取采集规则配置所绑定的机器组

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
                "AutoUpdate": "",
                "CreateTime": "2023-11-24 10:22:58",
                "DelayCleanupTime": 0,
                "GroupId": "59613f03-304e-492d-8bcc-af04716f4111",
                "GroupName": "test-filter",
                "MachineGroupType": {
                    "Type": "ip",
                    "Values": [
                        "9.1.9.1"
                    ]
                },
                "MetaTags": [],
                "OSType": 0,
                "ServiceLogging": false,
                "Tags": [],
                "UpdateEndTime": "",
                "UpdateStartTime": ""
            }
        ],
        "RequestId": "f32611a9-c1ff-48f3-97b3-32e28fe5b359"
    }
}
```

