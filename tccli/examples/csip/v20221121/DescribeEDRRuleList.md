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
                "Count": 218
            }
        ],
        "DetectTypeCounts": [
            {
                "Count": 688,
                "DetectType": 0
            }
        ],
        "List": [
            {
                "Action": 0,
                "AttackStage": "TA0009",
                "CWPScope": 1,
                "Confidence": 1,
                "ContentType": "cmdline",
                "CreateTime": "2026-03-02T15:11:09+08:00",
                "Description": "检测yapi应用中使用cat、head、tail、tac、less、more、vi、vim、nano、getent、vipw、vigr等命令查看/etc/passwd、/etc/shadow等/etc敏感文件或authorized_keys、bash_history等用户认证文件的行为",
                "DetectMode": 0,
                "DetectType": 0,
                "ExcludeImageIDs": [],
                "ExcludeQUUIDS": [],
                "ImageIDs": [],
                "ImageNamesRegex": "",
                "Level": 2,
                "ModifyTime": "2026-03-02T15:11:09+08:00",
                "Name": "yapi应用查看敏感文件",
                "QUUIDS": [],
                "RuleID": "383",
                "RuleType": 0,
                "Status": 0,
                "SupportBlock": 0,
                "TCSSScope": 1
            }
        ],
        "TotalCount": 688,
        "RequestId": "de366fc1-5524-4d68-a1fa-ab3ecebb6c02"
    }
}
```

