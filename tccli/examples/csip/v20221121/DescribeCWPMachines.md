**Example 1: 1**



Input: 

```
tccli csip DescribeCWPMachines --cli-unfold-argument  \
    --MemberId mem-a1f \
    --Filter.Limit 100 \
    --NeedTatStatus True \
    --MoreInformation True \
    --NeedContainerInfo True
```

Output: 
```
{
    "Response": {
        "Machines": [
            {
                "AgentStatus": "ONLINE",
                "AgentVersion": "5.4.4.133",
                "AppId": 260083796,
                "CloudFromEnum": "Tencent",
                "ContainerCount": 0,
                "ContainerDefendStatus": "Unknown",
                "CpuCoreCount": 2,
                "CsipProtectType": "BASIC",
                "ExposedStatus": "NONE",
                "InstanceID": "ins-*****nsn",
                "InstanceStatus": "RUNNING",
                "IpList": [
                    "fe80:************acc:c330"
                ],
                "IsNew": true,
                "KernelVersion": "6.6.117-45.7.3.tl4.x86_64",
                "LatestOfflineTime": 1781545140,
                "MachineIp": "10.216.0.85",
                "MachineName": "VM-0-85-tencentos",
                "MachineOs": "TencentOS Server 4",
                "MachineWanIp": "10*.******.*11",
                "NodeType": "NONE",
                "PayMode": "PREPAID",
                "ProjectId": 0,
                "ProtectType": "ULTIMATE",
                "Quuid": "969faa98-**************-55cf8ed1eccf",
                "RegionInfo": {
                    "Region": "ap-others",
                    "RegionCode": "others",
                    "RegionId": 47,
                    "RegionName": "其他地域（其他）",
                    "RegionNameEn": "Others (Other)"
                },
                "Remark": "",
                "TagModifyInfo": {
                    "AppID": 260083796,
                    "AssetType": "server_host",
                    "InstanceID": "ins-*****nsn",
                    "Provider": "tencent"
                },
                "TatStatus": "",
                "Uuid": "969faa98-***************55cf8ed1eccf",
                "VpcId": "vpc-j*****ox"
            }
        ],
        "Total": 18,
        "RequestId": "44f9ea21-c601-4974-b550-5bb988de4168"
    }
}
```

