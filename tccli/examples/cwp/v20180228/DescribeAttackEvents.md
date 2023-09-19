**Example 1: 网络攻击检测列表**

网络攻击检测列表

Input: 

```
tccli cwp DescribeAttackEvents --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Count": 6,
                "DstPort": 8080,
                "Id": 3,
                "Location": "",
                "MachineExtraInfo": {
                    "HostName": "",
                    "InstanceID": "ins-0cvonrya",
                    "NetworkName": "",
                    "NetworkType": 0,
                    "PrivateIP": "10.0.0.5",
                    "WanIP": "106.52.29.133"
                },
                "MergeTime": "2023-05-23T19:21:46+08:00",
                "PayVersion": 2,
                "Quuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
                "SrcIP": "127.0.0.1",
                "Status": 0,
                "Type": 0,
                "Uuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
                "VulDefenceStatus": 0,
                "VulId": 101824,
                "VulName": "Apache log4j2 远程代码执行漏洞 (CVE-2021-44228)",
                "VulSupportDefense": 1
            },
            {
                "Count": 5,
                "DstPort": 8080,
                "Id": 2,
                "Location": "局域网",
                "MachineExtraInfo": {
                    "HostName": "",
                    "InstanceID": "ins-0cvonrya",
                    "NetworkName": "",
                    "NetworkType": 0,
                    "PrivateIP": "10.0.0.5",
                    "WanIP": "106.52.29.133"
                },
                "MergeTime": "2023-05-23T14:43:28+08:00",
                "PayVersion": 2,
                "Quuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
                "SrcIP": "10.0.0.14",
                "Status": 0,
                "Type": 0,
                "Uuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
                "VulDefenceStatus": 0,
                "VulId": 101824,
                "VulName": "Apache log4j2 远程代码执行漏洞 (CVE-2021-44228)",
                "VulSupportDefense": 1
            },
            {
                "Count": 5,
                "DstPort": 8080,
                "Id": 1,
                "Location": "局域网",
                "MachineExtraInfo": {
                    "HostName": "",
                    "InstanceID": "ins-0cvonrya",
                    "NetworkName": "",
                    "NetworkType": 0,
                    "PrivateIP": "10.0.0.5",
                    "WanIP": "106.52.29.133"
                },
                "MergeTime": "2023-05-23T14:37:51+08:00",
                "PayVersion": 2,
                "Quuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
                "SrcIP": "10.0.0.5",
                "Status": 0,
                "Type": 0,
                "Uuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
                "VulDefenceStatus": 0,
                "VulId": 101824,
                "VulName": "Apache log4j2 远程代码执行漏洞 (CVE-2021-44228)",
                "VulSupportDefense": 1
            }
        ],
        "RequestId": "dcdbc4d6-54c1-45d5-ab8e-4a7c9275c168",
        "TotalCount": 3
    }
}
```

