**Example 1: 为资源绑定标签**

为资源绑定标签

Input: 

```
tccli tag TagResources --cli-unfold-argument  \
    --ResourceList qcs::cvm:ap-beijing:uin/10000055****:instance/ins-**** qcs::cvm:ap-shanghai:uin/10000055****:volme/volme-**** \
    --Tags.0.TagKey 11 \
    --Tags.0.TagValue 11 \
    --Tags.1.TagKey 22 \
    --Tags.1.TagValue 22
```

Output: 
```
{
    "Response": {
        "FailedResources": [],
        "RequestId": "a4c9f540-b04e-47c4-a267-4a398b70d2f5"
    }
}
```

