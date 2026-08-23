**Example 1: 创建容器镜像漏洞白名单**



Input: 

```
tccli csip CreateImageVulWhitelist --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --PocId tvd736 \
    --ImageIds 1 \
    --Scope 1 \
    --Status 1 \
    --Remark tvd白名单
```

Output: 
```
{
    "Response": {
        "RequestId": "21b05fc7-5807-4786-89c4-8b292e1c5d81"
    }
}
```

