**Example 1: 转发规则生效的开关，默认为开**



Input: 

```
tccli monitor ModifyDispenseExternalRuleStatus --cli-unfold-argument  \
    --RuleIdList 8388611 \
    --Status 0
```

Output: 
```
{
    "Response": {
        "RequestId": "12c2b6cb-6432-4e7e-b774-255917b7f0ed"
    }
}
```

