**Example 1: 自定义风险规则**



Input: 

```
tccli csip OperateRiskRulePolicy --cli-unfold-argument  \
    --OperateType disable \
    --RuleIDs tc_101 \
    --CheckAll False
```

Output: 
```
{
    "Response": {
        "Message": "操作成功",
        "RequestId": "8bb5f28c-4054-40a6-bff1-8f58703adda8"
    }
}
```

