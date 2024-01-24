**Example 1: 错误示例**

错误示例

Input: 

```
tccli wedata JudgeTaskListenEvent --cli-unfold-argument  \
    --KeySet 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "内部服务错误，请稍后重试。"
        },
        "RequestId": "c15f9e68-1022-43d5-b197-60cdb32c7ecf"
    }
}
```

