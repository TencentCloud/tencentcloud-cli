**Example 1: 获取区域主机列表**

本接口 (DescribeMachines) 用于获取区域主机列表。

Input: 

```
tccli cwp DescribeMachines --cli-unfold-argument  \
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
                "BaselineNum": 0,
                "CloudTags": [
                    {
                        "TagKey": "Department",
                        "TagValue": "dev"
                    }
                ],
                "CyberAttackNum": 0,
                "HasAssetScan": 0,
                "InstanceId": "ins-111",
                "InstanceState": "NORMAL",
                "InvasionNum": 3,
                "IpList": "1.1.1.1",
                "IsAddedOnTheFifteen": 1,
                "IsProVersion": false,
                "KernelVersion": "3.10.0-1160.88.1.el7.x86_64",
                "LicenseStatus": 0,
                "MachineExtraInfo": {
                    "HostName": "demo-instance",
                    "InstanceID": "ins-111",
                    "NetworkName": "vpc-111",
                    "NetworkType": 1,
                    "PrivateIP": "1.1.1.1",
                    "WanIP": "1.1.1.1"
                },
                "MachineIp": "1.1.1.1",
                "MachineName": "name01",
                "MachineOs": "CentOS 7.6 64位",
                "MachineStatus": "ONLINE",
                "MachineType": "CVM",
                "MachineWanIp": "1.1.1.1",
                "MalwareNum": 0,
                "PayMode": "POSTPAY",
                "ProjectId": 0,
                "ProtectType": "BASIC_VERSION",
                "Quuid": "3377add2-ee61-4c9a-99a3-************",
                "RegionInfo": {
                    "Region": "ap-nanjing",
                    "RegionCode": "nj",
                    "RegionId": 33,
                    "RegionName": "华东地区（南京）",
                    "RegionNameEn": "East China (Nanjing)"
                },
                "Remark": "do not remove",
                "SecurityStatus": "RISK",
                "Tag": [
                    {
                        "Rid": 1001,
                        "Name": "cwp",
                        "TagId": 1022
                    }
                ],
                "Uuid": "3377add2-ee61-4c9a-99a3-************",
                "VpcId": "vpc-1dj4***",
                "VulNum": 0
            }
        ],
        "RequestId": "621b6063-12b2-43fa-809e-************",
        "TotalCount": 192
    }
}
```

