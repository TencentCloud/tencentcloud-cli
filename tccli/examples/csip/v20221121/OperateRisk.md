**Example 1: 风险操作**



Input: 

```
tccli csip OperateRisk --cli-unfold-argument  \
    --RiskRuleId tc_001 \
    --RiskIdList 1 2 3 \
    --OperationType Ignore
```

Output: 
```
{
    "Response": {
        "Message": "操作成功",
        "RequestId": "jhdjs-dsu8y81-js-dhs"
    }
}
```

