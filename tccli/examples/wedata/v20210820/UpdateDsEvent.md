**Example 1: 错误示例**

错误示例

Input: 

```
tccli wedata UpdateDsEvent --cli-unfold-argument  \
    --ProjectId 1470561602745229312 \
    --Name 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnauthorizedOperation",
            "Message": "未授权操作"
        },
        "RequestId": "177dfedd-79d5-44ef-9f53-de1a3cff17bf"
    }
}
```

