**Example 1: 请求示例**



Input: 

```
tccli live ModifyLiveSnapshotTemplate --cli-unfold-argument  \
    --TemplateId 1000 \
    --TemplateName testName \
    --Description testDesc \
    --SnapshotInterval 10 \
    --Width 250 \
    --Height 250 \
    --PornFlag 0 \
    --CosAppId 123 \
    --CosBucket bucket \
    --CosRegion beijing
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

