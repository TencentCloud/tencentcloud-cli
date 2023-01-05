**Example 1: 查询聊天记录示例**

获取指定服务记录的文本消息记录。

Input: 

```
tccli ccc DescribeChatMessages --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --SessionId d6253538-7c28-477b-998a-919059801899
```

Output: 
```
{
    "Response": {
        "RequestId": "48edd236-7ef1-45af-9e12-fc376ba355bf",
        "TotalCount": 0,
        "Messages": []
    }
}
```

