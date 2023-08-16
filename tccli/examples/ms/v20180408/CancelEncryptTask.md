**Example 1: 取消加固任务失败示例**

加固任务不存在

Input: 

```
tccli ms CancelEncryptTask --cli-unfold-argument  \
    --ResultId a002b9e7-e01
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound.ResultIdNotFound",
            "Message": "ResultId不存在。"
        },
        "RequestId": "9379a8bd-f165-44db-a346-a3199fab2ae3"
    }
}
```

