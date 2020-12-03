**Example 1: 给资源栈新增一个模版版本**



Input: 

```
tccli tic CreateStackVersion --cli-unfold-argument  \
    --StackId stk-hz5vn3te \
    --VersionName new api v1.0 \
    --Description awesome description \
    --TemplateUrl https://hello-xxxxx.cos.ap-guangzhou.myqcloud.com/main.tf.zip
```

Output: 
```
{
    "Response": {
        "VersionId": "ver-mf7en58f",
        "RequestId": "8ef5ccb0-4207-468b-bb07-a03e6a772caf"
    }
}
```

