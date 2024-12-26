**Example 1: ModifyLiveSnapshotTemplate**

更新截图鉴黄模板配置。

Input: 

```
tccli live ModifyLiveSnapshotTemplate --cli-unfold-argument  \
    --TemplateId 0 \
    --TemplateName mytemplate \
    --Description 模板 \
    --SnapshotInterval 0 \
    --Width 0 \
    --Height 0 \
    --PornFlag 0 \
    --CosAppId 0 \
    --CosBucket sfjjsidexample \
    --CosRegion ap-beijing \
    --CosPrefix live \
    --CosFileName myfilename
```

Output: 
```
{
    "Response": {
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e"
    }
}
```

