**Example 1: 调用失败示例**



Input: 

```
tccli tiia DeleteImages --cli-unfold-argument  \
    --GroupId  \
    --EntityId 1 \
    --PicName test
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter.InvalidParameter",
            "Message": "参数不合法。"
        },
        "RequestId": "cac925c7-c939-4eb6-8db5-d642f7385c30"
    }
}
```

**Example 2: 调用成功示例**



Input: 

```
tccli tiia DeleteImages --cli-unfold-argument  \
    --GroupId 123 \
    --EntityId 1 \
    --PicName test
```

Output: 
```
{
    "Response": {
        "RequestId": "cac925c7-c939-4eb6-8db5-d642f7385c30"
    }
}
```

