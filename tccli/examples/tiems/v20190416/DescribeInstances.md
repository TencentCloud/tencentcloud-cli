**Example 1: 展示用户当前地域下所有节点**



Input: 

```
tccli tiems DescribeInstances --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Instances": [
            {
                "AbnormalReason": "",
                "Cpu": 24,
                "CpuRequested": 0,
                "Created": "2019-11-06T16:18:22+08:00",
                "DeadlineTime": "2020-02-06T16:18:36+08:00",
                "Gpu": 0,
                "GpuRequested": 0,
                "Id": "ins-19a065ev",
                "InstanceChargeType": "PREPAID",
                "InstanceType": "sv_tiems_instance_24c48g",
                "Memory": 48,
                "MemoryRequested": 0,
                "Region": "ap-beijing",
                "RenewFlag": "DISABLE_NOTIFY_AND_MANUAL_RENEW",
                "ResourceGroupId": "fl2hrhgp97jcg8pf",
                "State": "Running",
                "Updated": "2019-11-07T20:50:34+08:00",
                "Zone": "ap-beijing-2"
            },
            {
                "AbnormalReason": "",
                "Cpu": 24,
                "CpuRequested": 0,
                "Created": "2019-11-06T16:18:22+08:00",
                "DeadlineTime": "2020-02-06T16:18:29+08:00",
                "Gpu": 0,
                "GpuRequested": 0,
                "Id": "ins-19a066i9",
                "InstanceChargeType": "PREPAID",
                "InstanceType": "sv_tiems_instance_24c48g",
                "Memory": 48,
                "MemoryRequested": 0,
                "Region": "ap-beijing",
                "RenewFlag": "DISABLE_NOTIFY_AND_MANUAL_RENEW",
                "ResourceGroupId": "pf2kdwlmn9s2wq5m",
                "State": "Running",
                "Updated": "2019-11-07T20:50:34+08:00",
                "Zone": "ap-beijing-2"
            }
        ],
        "RequestId": "675e9ba8-f0ad-4727-83cc-384ee8089ac6",
        "TotalCount": 2
    }
}
```

**Example 2: 展示用户当前地域下某资源组的所有节点**



Input: 

```
tccli tiems DescribeInstances --cli-unfold-argument  \
    --ResourceGroupId pf2kdwlmn9s2wq5m
```

Output: 
```
{
    "Response": {
        "Instances": [
            {
                "AbnormalReason": "",
                "Cpu": 24,
                "CpuRequested": 0,
                "Created": "2019-11-06T16:18:22+08:00",
                "DeadlineTime": "2020-02-06T16:18:29+08:00",
                "Gpu": 0,
                "GpuRequested": 0,
                "Id": "ins-19a066i9",
                "InstanceChargeType": "PREPAID",
                "InstanceType": "sv_tiems_instance_24c48g",
                "Memory": 48,
                "MemoryRequested": 0,
                "Region": "ap-beijing",
                "RenewFlag": "DISABLE_NOTIFY_AND_MANUAL_RENEW",
                "ResourceGroupId": "pf2kdwlmn9s2wq5m",
                "State": "Running",
                "Updated": "2019-11-07T20:50:34+08:00",
                "Zone": "ap-beijing-2"
            }
        ],
        "RequestId": "6c6ebb92-5ede-491e-ab88-d49cb3dc22a1",
        "TotalCount": 1
    }
}
```

