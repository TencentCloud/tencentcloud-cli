**Example 1: 修改用户防护规则，关闭具体的某条规则**



Input: 

```
tccli waf ModifyUserSignatureRuleV2 --cli-unfold-argument  \
    --Domain abc.test.com \
    --RuleID.0.Id 10000266 \
    --RuleID.0.Status 0
```

Output: 
```
{
    "Response": {
        "RequestId": "40bbd265-74de-4e3b-b4f8-6219222ab961"
    }
}
```

