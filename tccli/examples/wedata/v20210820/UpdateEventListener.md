**Example 1: 错误示例**

错误示例

Input: 

```
tccli wedata UpdateEventListener --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --Key 1 \
    --Type 1 \
    --EventName 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "内部服务错误，请稍后重试。"
        },
        "RequestId": "f59094b7-0d99-4baf-9215-db8c3c371230"
    }
}
```

