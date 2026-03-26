**Example 1: 创建函数**



Input: 

```
tccli tcb CreateFunction --cli-unfold-argument  \
    --FunctionName my-func \
    --EnvId env-zyxjgkd \
    --Handler index.main \
    --MemorySize 0 \
    --Timeout 0 \
    --UseGpu false \
    --InstallDependency true \
    --Stamp Tcb \
    --Role TCB_QcsRole \
    --Description my function \
    --Runtime nodejs16 \
    --ClsTopicId topic-xx \
    --ClsLogsetId logset-yy \
    --Code.ZipFile zip-code-here \
    --PrivateConfig.Language nodejs
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

