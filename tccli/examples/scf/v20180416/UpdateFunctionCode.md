**Example 1: 更新函数代码**



Input: 

```
tccli scf UpdateFunctionCode --cli-unfold-argument  \
    --FunctionName test\
    --Handler index.main\
    --CosBucketName <CosBucketName>\
    --CosObjectName <CosObjectName>
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

