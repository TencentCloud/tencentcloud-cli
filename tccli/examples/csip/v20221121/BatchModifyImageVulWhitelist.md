**Example 1: 批量修改容器镜像漏洞白名单**



Input: 

```
tccli csip BatchModifyImageVulWhitelist --cli-unfold-argument  \
    --RuleId 120 \
    --MemberId mem-12e1se11 \
    --Status 1
```

Output: 
```
{
    "Response": {
        "RequestId": "696d0201-24ce-4785-88a1-613c078eb32f"
    }
}
```

