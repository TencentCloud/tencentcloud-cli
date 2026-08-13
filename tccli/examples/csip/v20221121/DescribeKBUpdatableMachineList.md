**Example 1: 查询可更新补丁主机列表**



Input: 

```
tccli csip DescribeKBUpdatableMachineList --cli-unfold-argument  \
    --KBIds 20001 20002 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "KBId": 20001,
                "InstanceId": "ins-e5f6g7h8",
                "MachineName": "win-server-01",
                "MachineIp": "10.0.1.50",
                "PublicIp": "203.0.113.20",
                "OsName": "Windows Server 2019",
                "MachineStatus": "ONLINE",
                "SupportAutoFix": 1,
                "FixStatus": 0,
                "LatestFixTime": "",
                "NotFixableReason": "",
                "TagItems": [],
                "AppId": 1251234567,
                "PayVersion": "ULTIMATE"
            }
        ],
        "TotalCount": 1,
        "FixableCount": 1,
        "NotFixableCount": 0,
        "KBSummary": [
            {
                "KBId": 20001,
                "KBName": "Windows 10 Version 22H2 累计更新",
                "KBNo": "KB5377343",
                "RelatedVulCount": 3,
                "AffectedCount": 1,
                "NeedReboot": true,
                "KBPreCondition": ""
            }
        ],
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

