**Example 1: 获取漏洞防御事件列表**



Input: 

```
tccli cwp DescribeVulDefenceEvent --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Id": 10001,
                "Uuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
                "Quuid": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
                "Alias": "harborV2_yancyw",
                "PrivateIp": "1.1.1.1",
                "PublicIp": "1.1.1.1",
                "UpgradeType": 1,
                "VulId": 101824,
                "VulName": "Apache log4j2 远程代码执行漏洞 (CVE-2021-44228)",
                "CveId": "CVE-2021-44228",
                "FixType": 0,
                "EventType": 2,
                "SourceIp": "",
                "City": "",
                "SourcePort": [],
                "CreateTime": "2024-10-23 11:41:10",
                "MergeTime": "2024-10-23 11:43:52",
                "Count": 20,
                "Status": 1,
                "MachineExtraInfo": {
                    "WanIP": "1.1.1.1",
                    "PrivateIP": "1.1.1.1",
                    "NetworkType": 1,
                    "NetworkName": "vpc-12332112",
                    "InstanceID": "ins-12332112",
                    "HostName": "机器名称"
                }
            }
        ],
        "RequestId": "be6f6eec-0825-4e67-ab9a-c8568bbf736c"
    }
}
```

