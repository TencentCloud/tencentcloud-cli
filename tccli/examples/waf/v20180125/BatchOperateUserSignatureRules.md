**Example 1: 批量操作tiga子规则**



Input: 

```
tccli waf BatchOperateUserSignatureRules --cli-unfold-argument  \
    --Domain test.waf.com \
    --Status 1 \
    --RuleIds 10000006 10000009 10000011 10000030 \
    --Reason 0 \
    --SelectedAll True \
    --Filters.0.ExactMatch True \
    --Filters.0.Name MainClassID \
    --Filters.0.Values 010000000
```

Output: 
```
{
    "Response": {
        "CommonRsp": {
            "Code": 0,
            "Msg": "Success"
        },
        "RequestId": "546b2091-1a59-4bd9-818d-47ab565102d9"
    }
}
```

