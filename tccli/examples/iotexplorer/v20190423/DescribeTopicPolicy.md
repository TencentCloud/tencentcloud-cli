**Example 1: 查看Topic详情示例**



Input: 

```
tccli iotexplorer DescribeTopicPolicy --cli-unfold-argument  \
    --ProductId ' 4ON538D9AX' \
    --TopicName $thing/up/raw/4ON538D9AX/dev
```

Output: 
```
{
    "Response": {
        "ProductId": "4ON538D9AX",
        "TopicName": "$thing/up/raw/4ON538D9AX/dev",
        "Privilege": 2,
        "RequestId": "4rt6-7yhn"
    }
}
```

