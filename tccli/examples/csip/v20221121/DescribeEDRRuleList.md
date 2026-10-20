**Example 1: edr策略列表**



Input: 

```
tccli csip DescribeEDRRuleList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AttackStageCounts": [
            {
                "AttackStage": "TA0002",
                "Count": 310
            }
        ],
        "DetectTypeCounts": [],
        "List": [
            {
                "Action": 2,
                "AppID": 260199983,
                "AttackStage": "TA0002",
                "CWPScope": 1,
                "ClusterIDs": [],
                "ConditionMatches": [],
                "Confidence": 1,
                "ContentType": "dns",
                "CreateTime": "2026-04-05 15:35:33",
                "Description": "腾讯云恶意域名库",
                "DetectMode": 0,
                "DetectType": 1,
                "ExcludeClusterIDs": [],
                "ExcludeImageIDs": [],
                "ExcludeInstanceIDs": [],
                "ExcludeQUUIDS": [],
                "ImageIDs": [],
                "ImageNamesRegex": "",
                "InstanceIDs": [],
                "Level": 1,
                "ModifyTime": "2026-08-11 22:38:07",
                "Name": "恶意请求",
                "QUUIDS": [],
                "RuleID": "sys_malicious_request",
                "RuleType": 0,
                "Status": 0,
                "SupportBlock": 1,
                "TCSSScope": 1,
                "TagItems": []
            }
        ],
        "TotalCount": 1545,
        "RequestId": "43758f26-985a-4f9f-abd5-8b6aa5dae30e"
    }
}
```

