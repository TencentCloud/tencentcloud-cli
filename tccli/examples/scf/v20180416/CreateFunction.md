**Example 1: 创建函数**

创建函数

Input: 

```
tccli scf CreateFunction --cli-unfold-argument  \
    --Code.CosBucketName <CosBucketName> \
    --Code.CosObjectName <CosObjectName> \
    --Handler <function.handler> \
    --FunctionName <FunctionName>
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

