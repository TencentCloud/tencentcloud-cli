**Example 1: Sample request**



Input: 

```
tccli live CreateLiveSnapshotTemplate --cli-unfold-argument  \
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
        "TemplateId": 1000,
        "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

