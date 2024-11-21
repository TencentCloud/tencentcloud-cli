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
                "MachineOs": "Windows Server 2022 数据中心版 64位 中文版",
                "Uuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                "Quuid": "24c9be55-c743-4a75-a5c7-2a2912341234",
                "MachineIp": "10.0.0.11",
                "IsProVersion": true,
                "MachineWanIp": "110.84.0.11",
                "PayMode": "PREPAY",
                "Tag": [
                    {
                        "Rid": 0,
                        "Name": "test-name",
                        "TagId": 1
                    }
                ],
                "RegionInfo": {
                    "Region": "ap-guangzhou",
                    "RegionName": "test-name",
                    "RegionId": 1,
                    "RegionCode": "gz",
                    "RegionNameEn": "test-name"
                },
                "InstanceState": "EXPIRED",
                "ProjectId": 0,
                "MachineType": "CVM",
                "KernelVersion": "0.1.1",
                "ProtectType": "BASIC_VERSION",
                "LicenseOrder": {
                    "LicenseId": 1,
                    "LicenseType": 1,
                    "Status": 1,
                    "SourceType": 1,
                    "ResourceId": "uf6iskfrpy4g3xg2k1jm"
                },
                "CloudTags": [],
                "InstanceId": "i-uf6iskfrpy4g3xg2k1jm"
            }
        ],
        "TotalCount": 1,
        "RequestId": "37b6df34-68f1-4ab8-a3d8-7b89de604c82"
    }
}
```

