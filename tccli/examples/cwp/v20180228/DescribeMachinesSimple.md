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
        "TotalCount": 1,
        "RequestId": "xx",
        "Machines": [
            {
                "KernelVersion": "xx",
                "IsProVersion": false,
                "MachineOs": "xx",
                "Uuid": "xx",
                "MachineName": "xx",
                "MachineIp": "xx",
                "PayMode": "xx",
                "RegionInfo": {
                    "RegionCode": "xx",
                    "Region": "xx",
                    "RegionId": 1,
                    "RegionNameEn": "xx",
                    "RegionName": "xx"
                },
                "Tag": [
                    {
                        "TagId": 1,
                        "Rid": 0,
                        "Name": "xx"
                    }
                ],
                "Quuid": "xx",
                "ProtectType": "xx",
                "ProjectId": 1,
                "MachineWanIp": "xx",
                "InstanceState": "xx",
                "MachineType": "xx",
                "LicenseOrder": null,
                "CloudTags": []
            }
        ]
    }
}
```

