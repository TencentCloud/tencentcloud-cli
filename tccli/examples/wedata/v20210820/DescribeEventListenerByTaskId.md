**Example 1: 错误示例**

错误示例

Input: 

```
tccli wedata DescribeEventListenerByTaskId --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --Key 111
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "内部服务错误，请稍后重试。"
        },
        "RequestId": "17dcc5e2-bb4c-4534-9c64-fa88d4eba032"
    }
}
```

