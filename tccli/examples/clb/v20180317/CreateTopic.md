**Example 1: 创建主题。**

创建主题。

Input: 

```
tccli clb CreateTopic --cli-unfold-argument  \
    --PartitionCount 3 \
    --TopicName clb-topic
```

Output: 
```
{
    "Response": {
        "TopicId": "b046ae5f-00cf-4e90-880c-215e5ae7b6xy",
        "RequestId": "dccf2ce3-0277-465a-9c60-260cfb141d65"
    }
}
```

