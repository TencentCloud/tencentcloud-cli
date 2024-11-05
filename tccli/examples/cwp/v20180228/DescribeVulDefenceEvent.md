**Example 1: 获取漏洞防御事件列表**



Input: 

```
tccli cwp DescribeVulDefenceEvent --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "356fec3f-0a9e-47c1-bbd0-c47d1496d0ae",
        "TotalCount": 1,
        "List": [
            {
                "Id": 13844,
                "Uuid": "acdd5474-6360-4fd4-bfc7-843162cb8116",
                "Quuid": "acdd5474-6360-4fd4-bfc7-843162cb8116",
                "Alias": "v_llzlu微隔离测试(millionlan)",
                "PrivateIp": "10.0.1.233",
                "PublicIp": "43.138.142.208",
                "UpgradeType": 1,
                "VulId": 14004,
                "VulName": "ISC BIND 资源管理错误漏洞(CVE-2014-8500)",
                "CveId": "CVE-2014-8500",
                "FixType": 1,
                "EventType": 2,
                "SourceIp": "na",
                "City": "beijing",
                "SourcePort": [],
                "CreateTime": "2024-11-03 00:40:12",
                "MergeTime": "2024-11-03 15:45:16",
                "Count": 74,
                "Status": 1,
                "MachineExtraInfo": {
                    "WanIP": "43.138.142.208",
                    "PrivateIP": "10.0.1.233",
                    "NetworkType": 1,
                    "NetworkName": "vpc-mbgoxtov",
                    "InstanceID": "ins-j7vumfb6",
                    "HostName": "v_llzlu微隔离测试(millionlan)"
                }
            }
        ]
    }
}
```

