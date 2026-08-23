**Example 1: 创建容器镜像敏感信息白名单**



Input: 

```
tccli csip CreateImageSensitiveWhitelist --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Behavior 1 \
    --ImageIds 1 \
    --Scope 0 \
    --Status 0 \
    --Remark 敏感信息白名单
```

Output: 
```
{
    "Response": {
        "RequestId": "09dda0d0-697e-484b-b33d-8b141d148f6f"
    }
}
```

