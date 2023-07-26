**Example 1: 请求示例**

创建 直播截图&鉴黄 模板。

Input: 

```
tccli live CreateLiveSnapshotTemplate --cli-unfold-argument  \
    --CosRegion beijing \
    --Description testDesc \
    --SnapshotInterval 10 \
    --PornFlag 0 \
    --CosBucket bucket \
    --TemplateName testName \
    --Height 250 \
    --CosAppId 123 \
    --Width 250
```

Output: 
```
{
    "Response": {
        "TemplateId": 1000,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

