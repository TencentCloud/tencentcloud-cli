**Example 1: 获取当前用户的过滤策略列表**



Input: 

```
tccli csip DescribeDspmAuditFilterStrategy --cli-unfold-argument  \
    --MemberId mem-1223 \
    --Filter.Limit 10 \
    --Filter.Offset 0 \
    --Filter.Order desc \
    --Filter.By ModifyTime
```

Output: 
```
{
    "Response": {
        "StrategySet": [
            {
                "AppId": 260085118,
                "AuditFilterStrategyId": 14,
                "CreateTime": "2026-07-17T06:57:52+08:00",
                "Description": "用于过滤无效的查询日志操作",
                "IsEnabled": 0,
                "ModifyTime": "2026-08-04T08:54:13+08:00",
                "Name": "过滤规则-去除查询操作",
                "Remark": "用于过滤无效的查询日志操作",
                "Rule": "{\"Fields\":[{\"Key\":\"DbName\",\"Operator\":\"include\",\"Value\":\"select\"}]}"
            }
        ],
        "TotalCount": 2,
        "RequestId": "3db2d4da-9b8c-42ca-8537-e0987161d3ca"
    }
}
```

