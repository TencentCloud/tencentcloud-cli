**Example 1: 更新云函数代码**



Input: 

```
tccli tcb UpdateFunctionCode --cli-unfold-argument  \
    --FunctionName scfweb2 \
    --EnvId ************************ \
    --Handler  \
    --Namespace  \
    --InstallDependency TRUE \
    --Publish  \
    --Code.ZipFile  \
    --CodeSource 
```

Output: 
```
{
    "Response": {
        "RequestId": "2a1b1e20-f32c-4285-b3b9-a94c493fa3d1"
    }
}
```

