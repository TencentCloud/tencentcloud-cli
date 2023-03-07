**Example 1: 创建自定义规则**

创建自定义规则

Input: 

```
tccli cwp ModifyBaselineRule --cli-unfold-argument  \
    --Data.Items.0.ItemId 1000 \
    --Data.Items.0.ItemName Redis 基线合规检测 \
    --Data.RuleDesc test111 \
    --Data.RuleName test111
```

Output: 
```
{
    "Response": {
        "RequestId": "0358f7f9-d07c-4db8-96ba-eed1bcbd947d"
    }
}
```

