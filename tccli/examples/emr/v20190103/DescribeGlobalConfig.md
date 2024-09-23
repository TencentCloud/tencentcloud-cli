**Example 1: 查询YARN资源调度的全局配置**



Input: 

```
tccli emr DescribeGlobalConfig --cli-unfold-argument  \
    --InstanceId emr-xxx
```

Output: 
```
{
    "Response": {
        "EnableResourceSchedule": true,
        "ActiveScheduler": "abc",
        "CapacityGlobalConfig": {
            "EnableLabel": true,
            "LabelDir": "abc",
            "QueueMappingOverride": true,
            "DefaultSettings": [
                {
                    "Name": "abc",
                    "Desc": "abc",
                    "Prompt": "abc",
                    "Key": "abc",
                    "Value": "abc"
                }
            ]
        },
        "FairGlobalConfig": {
            "UserMaxAppsDefault": 0
        },
        "Scheduler": "abc",
        "RequestId": "abc"
    }
}
```

