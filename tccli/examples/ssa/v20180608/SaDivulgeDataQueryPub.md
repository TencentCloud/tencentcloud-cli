**Example 1: 查询【通用字段】【泄露监测数据列表】**



Input: 

```
tccli ssa SaDivulgeDataQueryPub --cli-unfold-argument  \
    --QueryKey 模糊查询目标字段 \
    --EventName 安全事件名称 \
    --DivulgeSoure 监控源 \
    --Asset 受影响资产 \
    --RuleName 主体集规则 Topic 名称 \
    --RuleId 主体集规则 Topic Id \
    --Level 风险等级 \
    --Status 安全事件状态 \
    --StartTime 起始时间 \
    --EndTime 结束时间 \
    --Offset 1 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "Data": {
            "Count": 1,
            "List": [
                {
                    "Status": "xx",
                    "EventTime": "xx",
                    "InsertTime": "xx",
                    "RuleWord": "xx",
                    "RuleId": "xx",
                    "ScanCount": "xx",
                    "RuleName": "xx",
                    "UpdateTime": "xx",
                    "Uin": "xx",
                    "EventName": "xx",
                    "Asset": "xx",
                    "DivulgeSoure": "xx",
                    "AppId": "xx",
                    "ScanUrl": "xx",
                    "Level": "xx",
                    "Id": "xx"
                }
            ]
        },
        "RequestId": "f86588f7-fb1f-4fdd-9c8b-c882f044eeb0"
    }
}
```

