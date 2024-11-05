**Example 1: 查询批量导入机器信息**



Input: 

```
tccli cwp DescribeImportMachineInfo --cli-unfold-argument  \
    --MachineList 0.0.0.0 \
    --ImportType Ip \
    --IsQueryProMachine True
```

Output: 
```
{
    "Response": {
        "EffectiveMachineInfoList": [
            {
                "MachineName": "tke-np-ol06goby-worker",
                "MachinePublicIp": "10.0.1.92",
                "MachinePrivateIp": "172.17.2.23",
                "MachineTag": [
                    {
                        "Rid": 10,
                        "Name": "dev",
                        "TagId": 10021
                    }
                ],
                "CloudTags": [
                    {
                        "TagKey": "cwp",
                        "TagValue": "dev"
                    }
                ],
                "Quuid": "a9fe0359-04d9-417f-ab6d-4941891d6c4b",
                "Uuid": "a9fe0359-04d9-417f-ab6d-4941891d6c4b",
                "KernelVersion": "5.4.241-19-0017.1_plus",
                "MachineStatus": "OFFLINE",
                "LicenseOrder": {
                    "LicenseId": 136621,
                    "LicenseType": 2,
                    "SourceType": 1,
                    "ResourceId": "white_883011a2fb7a2ce8f032025ec0437f52",
                    "Status": 1
                },
                "VulNum": 0,
                "InstanceID": "eks-h847trlg"
            }
        ],
        "InvalidMachineList": [
            "a9fe0359-04d9-417f-ab6d-****"
        ],
        "RequestId": "633204c8-383a-4dbb-940b-2e92d0674529"
    }
}
```

