**Example 1: 发布新版本**

发布新版本

Input: 

```
tccli scf PublishVersion --cli-unfold-argument  \
    --FunctionName <FunctionName> \
    --Description <Description>
```

Output: 
```
{
    "Response": {
        "Namespace": "default",
        "Description": "dummytut",
        "CodeSize": 45686,
        "MemorySize": 256,
        "Handler": "scfredis.main_handler",
        "RequestId": "68c9669c-9e2c-47b0-9a01-e8406a41be59",
        "Timeout": 3,
        "Runtime": "Python2.7",
        "FunctionVersion": "4"
    }
}
```

