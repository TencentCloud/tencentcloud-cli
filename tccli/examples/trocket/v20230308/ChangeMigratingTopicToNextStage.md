**Example 1: 修改迁移主题进入下一个迁移阶段**



Input: 

```
tccli trocket ChangeMigratingTopicToNextStage --cli-unfold-argument  \
    --TaskId 02f6c31a-9707-4244-8dd3-35ad868ef92a \
    --TopicNameList TopicTest
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Results": [
            {
                "TopicName": "TopicTest",
                "Success": true,
                "Namespace": ""
            }
        ],
        "RequestId": "02f6c31a-9707-4244-8dd3-35ad868ef92a"
    }
}
```

