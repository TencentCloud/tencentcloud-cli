**Example 1: 删除用户自定义规则状态**



Input: 

```
tccli waf DeleteOwaspRuleStatus --cli-unfold-argument  \
    --Domain q.testwaf.com \
    --RuleIDs 1000000
```

Output: 
```
{
    "Response": {
        "RequestId": "08e8410d-6e80-4d1f-89ff-62669042369d"
    }
}
```

