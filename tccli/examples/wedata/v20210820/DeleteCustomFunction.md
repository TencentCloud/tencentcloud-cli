**Example 1: 删除自定义函数**

删除自定义函数

Input: 

```
tccli wedata DeleteCustomFunction --cli-unfold-argument  \
    --ClusterIdentifier sdf \
    --FunctionId sdfsdf \
    --ProjectId sdfsdf \
    --FunctionName sdfsdf
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "系统内部异常：NumberFormatException: For input string: \"sdfsdf\""
        },
        "RequestId": "fde6b682-e482-44d9-b774-9d97b30446f5"
    }
}
```

