**Example 1: 修改迁移主题进入下一个迁移阶段**



Input: 

```
tccli trocket ChangeMigratingTopicToNextStage --cli-unfold-argument  \
    --TaskId abc \
    --TopicNameList TopicTest
```

Output: 
```
{
    "Response": {
        "Results": [
            {
                "TopicName": "TopicTest",
                "Success": true,
                "Namespace": ""
            }
        ],
        "RequestId": "abc"
    }
}
```

