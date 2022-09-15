**Example 1: 请求示例**



Input: 

```
tccli live ModifyLiveSnapshotTemplate --cli-unfold-argument  \
    --CosRegion beijing \
    --Description testDesc \
    --SnapshotInterval 10 \
    --PornFlag 0 \
    --CosBucket bucket \
    --TemplateName testName \
    --Height 250 \
    --CosAppId 123 \
    --Width 250 \
    --TemplateId 1000
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

