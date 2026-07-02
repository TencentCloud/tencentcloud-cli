**Example 1: edr告警列表**



Input: 

```
tccli csip DescribeEdrAlertList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --Order DESC \
    --By LatestDetectTime
```

Output: 
```
{
    "Response": {
        "AlertCategoryCounts": [
            {
                "AlertCategory": "VIRUS_TROJAN",
                "Count": 245
            }
        ],
        "AttackStageCounts": [
            {
                "AttackStage": "",
                "Count": 3182
            }
        ],
        "List": [
            {
                "AlertCategory": "VIRUS_TROJAN",
                "AlertId": "3d4463f3f4a7bdee02520b0f83a11c6a",
                "AlertSource": "HOST",
                "AlertSubType": "MALWARE_PROCESS",
                "AppId": 260146618,
                "AttackStage": "",
                "ClusterId": "",
                "ContainerId": "",
                "ContentType": "",
                "DetectMode": "PRECISE",
                "EventCount": 2,
                "FirstDetectTime": "2026-05-30 17:28:21",
                "Id": 1000000000008822,
                "ImageId": "",
                "InstanceId": "ins-f1vbqysn",
                "InstanceName": "VM-11-16-tencentos",
                "IsProVersion": 1,
                "LatestDetectTime": "2026-06-03 17:14:29",
                "Level": "CRITICAL",
                "PrivateIp": "172.20.11.16",
                "PublicIp": "129.28.108.211",
                "Quuid": "8ceae791-925f-4a77-be58-22e9f7ead617",
                "RuleId": "mp_15003",
                "RuleName": "",
                "RuleType": 0,
                "Status": "PENDING"
            }
        ],
        "TotalCount": 3496,
        "RequestId": "dd11c00c-d7b4-48ec-8a7b-00e7bcdc909c"
    }
}
```

