**Example 1: 错误示例**

错误示例

Input: 

```
tccli wedata DeleteEventListenerByTaskId --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --Key 11
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "内部服务错误，请稍后重试。"
        },
        "RequestId": "31c85a45-499d-4b23-af9d-43dbb1faa50d"
    }
}
```

