**Example 1: 获取区域主机列表**

本接口 (DescribeMachines) 用于获取区域主机列表。

Input: 

```
tccli yunjing DescribeMachines --cli-unfold-argument  \
    --MachineType CVM \
    --MachineRegion ap-shanghai \
    --Filters.0.Name Keywords \
    --Filters.0.Values 10.0.1.1 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Machines": [
            {
                "MachineName": "ccs_cls-i4vyo8qa_node",
                "MachineIp": "172.16.0.4",
                "MachineWanIp": "193.112.57.245",
                "MachineOs": "ubuntu16.04.1 LTSx86_64",
                "MachineStatus": "OFFLINE",
                "Quuid": "fbd6ea2c-1894-47b0-bf3e-095c78138f76",
                "Uuid": "",
                "IsProVersion": false,
                "PayMode": "",
                "VulNum": 0,
                "Tag": [],
                "MalwareNum": 0,
                "BaseLineNum": 0,
                "CyberAttackNum": 0,
                "SecurityStatus": "SAFE"
            },
            {
                "MachineName": "piperpeng-mnet",
                "MachineIp": "10.0.0.8",
                "MachineWanIp": "129.204.223.122",
                "MachineOs": "centos7.5x86_64",
                "MachineStatus": "ONLINE",
                "Quuid": "d095145f-d417-49a7-8d83-da19320fd419",
                "Uuid": "ecc9dfd0-674b-11e9-950f-40f2e9f553a2",
                "IsProVersion": false,
                "PayMode": "",
                "VulNum": -1,
                "Tag": [
                    {
                        "Rid": 174,
                        "Name": "森"
                    }
                ],
                "MalwareNum": -1,
                "BaseLineNum": 0,
                "CyberAttackNum": 0,
                "SecurityStatus": "UNKNOWN"
            },
            {
                "MachineName": "jaryzhou-hp",
                "MachineIp": "10.104.18.25",
                "MachineWanIp": "139.199.79.160",
                "MachineOs": "centos7.2x86_64",
                "MachineStatus": "OFFLINE",
                "Quuid": "999108c2-e2a4-4ce7-b3ce-dd9c7af4c7ea",
                "Uuid": "a701fb5c-35ce-11ea-80ce-5cb90191ae78",
                "IsProVersion": false,
                "PayMode": "",
                "VulNum": -1,
                "Tag": [],
                "MalwareNum": 2,
                "BaseLineNum": 0,
                "CyberAttackNum": 0,
                "SecurityStatus": "UNKNOWN"
            },
            {
                "MachineName": "上汽私有云测试",
                "MachineIp": "172.16.16.15",
                "MachineWanIp": "193.112.181.15",
                "MachineOs": "centos6.8x86_64",
                "MachineStatus": "OFFLINE",
                "Quuid": "57375249-a16c-4c9f-b210-e8c1fb4e8806",
                "Uuid": "",
                "IsProVersion": false,
                "PayMode": "",
                "VulNum": 0,
                "Tag": [],
                "MalwareNum": 0,
                "BaseLineNum": 0,
                "CyberAttackNum": 0,
                "SecurityStatus": "SAFE"
            },
            {
                "MachineName": "漏洞yhvs编译机-linux",
                "MachineIp": "172.16.16.32",
                "MachineWanIp": "106.52.175.244",
                "MachineOs": "centos7.6.0_x64",
                "MachineStatus": "OFFLINE",
                "Quuid": "dbf3dcd4-179a-4bc6-86e4-15439f4cc898",
                "Uuid": "",
                "IsProVersion": false,
                "PayMode": "",
                "VulNum": 0,
                "Tag": [],
                "MalwareNum": 0,
                "BaseLineNum": 0,
                "CyberAttackNum": 0,
                "SecurityStatus": "SAFE"
            },
            {
                "MachineName": "漏洞yhvs编译机-win",
                "MachineIp": "172.16.16.48",
                "MachineWanIp": "106.52.166.61",
                "MachineOs": "Xserver V8.1_64",
                "MachineStatus": "OFFLINE",
                "Quuid": "1cbfd259-d992-4e3f-8188-02ad59b862cc",
                "Uuid": "",
                "IsProVersion": false,
                "PayMode": "",
                "VulNum": 0,
                "Tag": [],
                "MalwareNum": 0,
                "BaseLineNum": 0,
                "CyberAttackNum": 0,
                "SecurityStatus": "SAFE"
            },
            {
                "MachineName": "poc测试(129.204.1.205)",
                "MachineIp": "10.104.162.166",
                "MachineWanIp": "129.204.1.205",
                "MachineOs": "CentOS6.3-64bit",
                "MachineStatus": "ONLINE",
                "Quuid": "2967d5c5-730b-4b76-87a1-95565f218cd0",
                "Uuid": "9e9a4f9e-165e-11ea-8f91-5cb90191ae68",
                "IsProVersion": false,
                "PayMode": "",
                "VulNum": -1,
                "Tag": [],
                "MalwareNum": -1,
                "BaseLineNum": 0,
                "CyberAttackNum": 0,
                "SecurityStatus": "UNKNOWN"
            },
            {
                "MachineName": "poc测试(203.195.231.172)",
                "MachineIp": "10.104.135.28",
                "MachineWanIp": "203.195.231.172",
                "MachineOs": "debian9.0.0x86_64",
                "MachineStatus": "ONLINE",
                "Quuid": "d42129e4-54d3-41af-944c-ec5cfa0ce942",
                "Uuid": "c2972dd6-165e-11ea-95eb-40f2e9f5667a",
                "IsProVersion": false,
                "PayMode": "",
                "VulNum": -1,
                "Tag": [
                    {
                        "Rid": 285,
                        "Name": "&……#￥%@%36"
                    },
                    {
                        "Rid": 286,
                        "Name": "123"
                    },
                    {
                        "Rid": 283,
                        "Name": "helloworld"
                    },
                    {
                        "Rid": 284,
                        "Name": "森"
                    }
                ],
                "MalwareNum": 1,
                "BaseLineNum": 0,
                "CyberAttackNum": 0,
                "SecurityStatus": "UNKNOWN"
            },
            {
                "MachineName": "poc测试(129.204.37.89)",
                "MachineIp": "10.104.35.71",
                "MachineWanIp": "129.204.37.89",
                "MachineOs": "centos7.6.0_x64",
                "MachineStatus": "OFFLINE",
                "Quuid": "d7ab00a7-4318-4e6d-9280-0618c350e5eb",
                "Uuid": "b0ad0c08-1645-11ea-b872-40f2e9f5bb82",
                "IsProVersion": false,
                "PayMode": "",
                "VulNum": -1,
                "Tag": [],
                "MalwareNum": -1,
                "BaseLineNum": 0,
                "CyberAttackNum": 0,
                "SecurityStatus": "UNKNOWN"
            },
            {
                "MachineName": "poc测试(129.204.36.227)",
                "MachineIp": "10.104.14.165",
                "MachineWanIp": "129.204.36.227",
                "MachineOs": "ubuntu18.04.1x86_64",
                "MachineStatus": "OFFLINE",
                "Quuid": "b86925b4-cc36-420e-80d4-5094cb2f094b",
                "Uuid": "ed629672-165e-11ea-8bcf-40f2e9f3d932",
                "IsProVersion": false,
                "PayMode": "",
                "VulNum": -1,
                "Tag": [],
                "MalwareNum": 0,
                "BaseLineNum": 0,
                "CyberAttackNum": 0,
                "SecurityStatus": "UNKNOWN"
            }
        ],
        "TotalCount": 44,
        "RequestId": "c30f35cb-2f3e-94f5-59ae-316e0f32e660"
    }
}
```

