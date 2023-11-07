**Example 1: 校验数据加工函数语法**

校验数据加工函数的语法

Input: 

```
tccli cls CheckFunction --cli-unfold-argument  \
    --EtlContent fields_set() \
    --DstResources.0.TopicId x56493046-XXXX-4194-81f6-c2e75569b031 \
    --DstResources.0.Alias example \
    --FuncType 1
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "ErrorMsg": "",
        "RequestId": "x56493046-XXXX-4194-81f6-c2e75569b031"
    }
}
```

