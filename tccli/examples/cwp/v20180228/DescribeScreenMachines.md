**Example 1: 示例**

主机3D图数据


Input: 

```
tccli cwp DescribeScreenMachines --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AttackCnt": 0,
                "IgnoreCnt": 0,
                "Machines": [
                    {
                        "BaselineNum": 147,
                        "CoreVersion": "3.10.0",
                        "CpuLoad": "低",
                        "CpuSize": 2,
                        "CyberAttackNum": 162,
                        "DiskLoad": "32.07",
                        "DiskSize": 50,
                        "InvasionNum": 38479,
                        "MachineExtraInfo": {
                            "HostName": "",
                            "InstanceID": "ins-xxx",
                            "NetworkName": "",
                            "NetworkType": 0,
                            "PrivateIP": "xx.xx.xx.xx",
                            "WanIP": "xx.xx.xx.xx"
                        },
                        "MachineIp": "xx.xx.xx.xx",
                        "MachineName": "ha2",
                        "MachineOs": "CentOS 7.9 64位",
                        "MachineStatus": 9,
                        "MachineType": "CVM",
                        "MachineWanIp": "xx.xx.xx.xx",
                        "MemLoad": "36.52",
                        "MemSize": 4,
                        "Quuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                        "SecurityStatus": "RISK",
                        "Uuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                        "VulNum": 18
                    }
                ],
                "Region": "ap-guangzhou",
                "RegionName": "华南地区（广州）",
                "RiskCnt": 1,
                "SafetyCnt": 1,
                "TotalCount": 1,
                "UnAgentOfflineCnt": 1
            }
        ],
        "RequestId": "xxxxxxxx-1234-5678-9101-yyyyyyyyyy"
    }
}
```

