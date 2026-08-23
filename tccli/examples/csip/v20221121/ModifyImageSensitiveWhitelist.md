**Example 1: 修改容器镜像敏感信息白名单**



Input: 

```
tccli csip ModifyImageSensitiveWhitelist --cli-unfold-argument  \
    --RuleId 1 \
    --MemberId mem-12e1se11 \
    --Behavior 2 \
    --ImageIds 1 \
    --Scope 0 \
    --Status 0 \
    --Remark 敏感信息白名单
```

Output: 
```
{
    "Response": {
        "RequestId": "a4cea968-49df-4ec5-b417-6462c2733129"
    }
}
```

