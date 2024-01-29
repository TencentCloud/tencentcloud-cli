**Example 1: 错误示例**

错误示例

Input: 

```
tccli wedata DescribeEventListenerTask --cli-unfold-argument  \
    --ProjectId 1 \
    --EventName 1 \
    --PageNumber 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnauthorizedOperation",
            "Message": "未授权操作"
        },
        "RequestId": "b2abb65c-fb76-41d9-9167-871768935f1c"
    }
}
```

