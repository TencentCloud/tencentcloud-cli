**Example 1: 获取Topic列表示例**



Input: 

```
tccli iotexplorer ListTopicPolicy --cli-unfold-argument  \
    --ProductId ABCDE12345
```

Output: 
```
{
    "Response": {
        "Topics": [
            {
                "TopicName": "abc",
                "Privilege": 1
            }
        ],
        "RequestId": "be69a7a3-7315-40a7-9532-3316e4a3e97e"
    }
}
```

