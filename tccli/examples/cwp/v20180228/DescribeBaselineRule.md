**Example 1: 查询基线检测项信息**

根据基线id与条件查询基线检测项信息

Input: 

```
tccli cwp DescribeBaselineRule --cli-unfold-argument  \
    --BaselineId 100441 \
    --Level 1 \
    --Status 0 \
    --Quuid "8c8a-69e3ab73aa8a" \
    --Uuid "asdasd123-124sfas" \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "TotalCount": 21,
        "ShowRuleRemark": true,
        "BaselineRuleList": [
            {
                "RuleName": "安全检测项目1",
                "Description": "安全检测项目1描述",
                "FixMessage": "重新启动服务",
                "Level": 1,
                "Status": 0,
                "RuleId": 1,
                "LastScanAt": "2020-09-16 ：00:00:00",
                "EventId": 1,
                "Uuid": "Uuid"
            }
        ]
    }
}
```

