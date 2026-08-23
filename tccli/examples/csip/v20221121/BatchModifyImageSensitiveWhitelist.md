**Example 1: 批量修改容器镜像敏感信息白名单**



Input: 

```
tccli csip BatchModifyImageSensitiveWhitelist --cli-unfold-argument  \
    --RuleId 89 \
    --MemberId mem-12e1se11 \
    --Status 1
```

Output: 
```
{
    "Response": {
        "RequestId": "0359f603-5888-4dd4-aa34-1e3e3433114d"
    }
}
```

