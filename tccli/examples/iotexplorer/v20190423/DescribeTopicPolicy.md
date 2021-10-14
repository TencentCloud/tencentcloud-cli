**Example 1: 查看Topic详情示例**



Input: 

```
tccli iotexplorer DescribeTopicPolicy --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --TopicName abc
```

Output: 
```
{
    "Response": {
        "TopicName": "abc",
        "Privilege": 2
    }
}
```

