**Example 1: 修改漏洞白名单配置**



Input: 

```
tccli csip ModifyVulWhitelistConfig --cli-unfold-argument  \
    --Id 8 \
    --Remark 备注 \
    --AssetRange 1 \
    --AssetList ins-khz78apa
```

Output: 
```
{
    "Response": {
        "RequestId": "965d7001-779c-4549-9d9c-ed3bcce4c402"
    }
}
```

