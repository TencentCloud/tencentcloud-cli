**Example 1: 获取区域主机列表**

本接口 (DescribeMachinesSimple) 用于获取区域主机列表。

Input: 

```
tccli cwp DescribeMachinesSimple --cli-unfold-argument  \
    --Limit 10 \
    --MachineRegion ap-shanghai \
    --MachineType CVM \
    --Filters.0.Values 10.0.1.1 \
    --Filters.0.Name Keywords \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Machines": [
            {
                "MachineName": "test-name",
                "MachineOs": "abc",
                "Uuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                "Quuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                "MachineIp": "10.0.0.11",
                "IsProVersion": true,
                "MachineWanIp": "110.84.0.11",
                "PayMode": "abc",
                "Tag": [
                    {
                        "Rid": 0,
                        "Name": "test-name",
                        "TagId": 1
                    }
                ],
                "RegionInfo": {
                    "Region": "abc",
                    "RegionName": "test-name",
                    "RegionId": 1,
                    "RegionCode": "abc",
                    "RegionNameEn": "test-name"
                },
                "InstanceState": "abc",
                "ProjectId": 0,
                "MachineType": "abc",
                "KernelVersion": "0.1.1",
                "ProtectType": "abc",
                "LicenseOrder": {
                    "LicenseId": 1,
                    "LicenseType": 1,
                    "Status": 1,
                    "SourceType": 1,
                    "ResourceId": "abc"
                },
                "CloudTags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "InstanceId": "abc"
            }
        ],
        "TotalCount": 1,
        "RequestId": "37b6df34-68f1-4ab8-a3d8-7b89de604c82"
    }
}
```

