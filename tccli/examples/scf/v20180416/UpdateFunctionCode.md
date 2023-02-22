**Example 1: 更新函数代码**



Input: 

```
tccli scf UpdateFunctionCode --cli-unfold-argument  \
    --CosObjectName <CosObjectName> \
    --Handler index.main \
    --CosBucketName <CosBucketName> \
    --FunctionName test
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

