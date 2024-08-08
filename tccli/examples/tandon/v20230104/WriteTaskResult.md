**Example 1: 正常写回工具诊断结果**

正常写回工具诊断结果

Input: 

```
tccli tandon WriteTaskResult --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "123-yy"
    }
}
```

**Example 2: 非法的taskId**

非法的taskId

Input: 

```
tccli tandon WriteTaskResult --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter",
            "Message": "参数错误，taskId 不能为空"
        },
        "RequestId": ""
    }
}
```

