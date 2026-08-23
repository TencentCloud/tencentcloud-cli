**Example 1: 批量修改镜像木马白名单**



Input: 

```
tccli csip BatchModifyImageVirusWhitelist --cli-unfold-argument  \
    --RuleId 7 \
    --MemberId mem-12e1se11 \
    --Status 1
```

Output: 
```
{
    "Response": {
        "RequestId": "c95b245d-bd76-45a0-b846-59fb568b6ac5"
    }
}
```

