**Example 1: 获取某个实例下的主题列表**



Input: 

```
tccli ckafka DescribeTopic --cli-unfold-argument  \
    --InstanceId ckafka-xxooa0
```

Output: 
```
{
    "Response": {
        "Result": {
            "TopicList": [
                {
                    "TopicId": "inter-topic-8sj6wxwi",
                    "TopicName": "test1",
                    "Note": ""
                },
                {
                    "TopicId": "inter-topic-844bkmry",
                    "TopicName": "test10",
                    "Note": ""
                }
            ],
            "TotalCount": 12
        },
        "RequestId": "8d7551b2-651e-4f47-80bc-13a478fda732"
    }
}
```

