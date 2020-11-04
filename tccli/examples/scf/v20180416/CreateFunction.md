**Example 1: 创建函数**



Input: 

```
tccli scf CreateFunction --cli-unfold-argument  \
    --FunctionName <FunctionName>\
    --Handler <function.handler>\
    --Code.CosBucketName <CosBucketName>\
    --Code.CosObjectName <CosObjectName>
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

