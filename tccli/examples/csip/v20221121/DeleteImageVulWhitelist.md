**Example 1: 删除容器镜像漏洞白名单**



Input: 

```
tccli csip DeleteImageVulWhitelist --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --RuleId 2
```

Output: 
```
{
    "Response": {
        "RequestId": "09d549a9-7e54-4141-bb80-8ce9e5ec13ef"
    }
}
```

