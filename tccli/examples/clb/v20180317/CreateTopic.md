**Example 1: Creating a topic**



Input: 

```
tccli clb CreateTopic --cli-unfold-argument  \
    --TopicName clb-topic\
    --PartitionCount 3
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

