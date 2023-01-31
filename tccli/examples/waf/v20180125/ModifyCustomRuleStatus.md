**Example 1: 切换自定义规则的开关**

切换自定义规则的开关

Input: 

```
tccli waf ModifyCustomRuleStatus --cli-unfold-argument  \
    --Domain "test.qlcoud.com" \
    --RuleId 12 \
    --Status 0
```

Output: 
```
{
    "Response": {
        "RequestId": "1c30f037-a684-4d5b-b0a8-0bc0acc668d1",
        "Success": {
            "Message": "Success",
            "Code": "Success"
        }
    }
}
```

