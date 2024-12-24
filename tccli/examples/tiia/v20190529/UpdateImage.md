**Example 1: 更新图片接口调用失败示例**



Input: 

```
tccli tiia UpdateImage --cli-unfold-argument  \
    --GroupId my_group \
    --EntityId entity_297 \
    --PicName my_pic
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter.InvalidParameter",
            "Message": "参数不合法。"
        },
        "RequestId": "cac925c7-c939-4eb6-8db5-d64123385c30"
    }
}
```

**Example 2: 更新图片接口调用成功示例**



Input: 

```
tccli tiia UpdateImage --cli-unfold-argument  \
    --GroupId group_972 \
    --EntityId entity_297 \
    --PicName my_pic
```

Output: 
```
{
    "Response": {
        "RequestId": "cac925c7-c939-4e26-8db5-d642f7385c30"
    }
}
```

