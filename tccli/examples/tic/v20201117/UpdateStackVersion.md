**Example 1: 更新资源栈的某个版本**



Input: 

```
tccli tic UpdateStackVersion --cli-unfold-argument  \
    --VersionId ver-d6bxn583 \
    --VersionName new api v2.0 \
    --Description api v2.0 backend infra template \
    --TemplateUrl https://hello-xxxx.cos.ap-guangzhou.myqcloud.com/main.tf.zip
```

Output: 
```
{
    "Response": {
        "RequestId": "8ef5ccb0-4207-468b-bb07-a03e6a772caf"
    }
}
```

