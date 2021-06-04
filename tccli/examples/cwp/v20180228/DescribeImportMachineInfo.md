**Example 1: 查询批量导入机器信息**



Input: 

```
tccli cwp DescribeImportMachineInfo --cli-unfold-argument  \
    --MachineList xx \
    --ImportType xx \
    --IsQueryProMachine True
```

Output: 
```
{
    "Response": {
        "InvalidMachineList": [
            "xx"
        ],
        "RequestId": "xx",
        "EffectiveMachineInfoList": [
            {
                "MachineName": "xx",
                "MachineTag": [
                    {
                        "TagId": 1,
                        "Rid": 0,
                        "Name": "xx"
                    }
                ],
                "MachinePublicIp": "xx",
                "Quuid": "xx",
                "MachinePrivateIp": "xx"
            }
        ]
    }
}
```

