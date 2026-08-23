**Example 1: 创建镜像木马白名单**



Input: 

```
tccli csip CreateImageVirusWhitelist --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Md5List B8C*******************9559EBB996 \
    --Scope 1 \
    --ImageIds 1 \
    --Remark 木马白名单 \
    --VirusId 1 \
    --Name 木马白名单0629
```

Output: 
```
{
    "Response": {
        "RequestId": "e86e6fbc-461c-4334-b44e-eb09e9f6a752"
    }
}
```

