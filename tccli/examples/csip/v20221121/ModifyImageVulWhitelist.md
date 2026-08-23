**Example 1: 修改容器镜像漏洞白名单**



Input: 

```
tccli csip ModifyImageVulWhitelist --cli-unfold-argument  \
    --RuleId 1 \
    --MemberId mem-12e1se11 \
    --PocId tvd736 \
    --ImageIds 1 \
    --Scope 1 \
    --Status 1 \
    --Remark 漏洞白名单
```

Output: 
```
{
    "Response": {
        "RequestId": "3c3c0132-cfb2-4ceb-872a-90a7cc8110c2"
    }
}
```

