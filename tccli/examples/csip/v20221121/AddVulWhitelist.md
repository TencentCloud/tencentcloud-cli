**Example 1: 添加漏洞白名单**



Input: 

```
tccli csip AddVulWhitelist --cli-unfold-argument  \
    --VulId 5566 \
    --KbId 10 \
    --MemberId mem-tencent-6f5795752f66e429 \
    --Remark 备注1 \
    --AssetList ins-m****iks
```

Output: 
```
{
    "Response": {
        "RequestId": "ad8a5084-ce24-42c7-b582-ebac463687db"
    }
}
```

