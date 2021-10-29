**Example 1: 调用成功示例**



Input: 

```
tccli tiia DescribeImages --cli-unfold-argument  \
    --EntityId test3 \
    --GroupId work
```

Output: 
```
{
    "Response": {
        "EntityId": "test3",
        "GroupId": "work",
        "ImageInfos": [
            {
                "CustomContent": "custom",
                "EntityId": "test3",
                "PicName": "4000",
                "Score": 0,
                "Tags": "{\"value\": 20}"
            },
            {
                "CustomContent": "custom",
                "EntityId": "test3",
                "PicName": "4001",
                "Score": 0,
                "Tags": "{\"value\": 20}"
            },
            {
                "CustomContent": "custom",
                "EntityId": "test3",
                "PicName": "4002",
                "Score": 0,
                "Tags": "{\"value\": 20}"
            }
        ],
        "RequestId": "65996842-8bb5-430f-bb40-460b3c73db76"
    }
}
```

