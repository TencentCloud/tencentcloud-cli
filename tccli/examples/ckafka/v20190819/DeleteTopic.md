**Example 1: 删除主题**



Input: 

```
tccli ckafka DeleteTopic --cli-unfold-argument  \
    --InstanceId ckafka \
    --TopicName topicname
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReturnCode": "0",
            "ReturnMessage": "ok[apply success]",
            "Data": null
        },
        "RequestId": "bf88d4c8-06f5-4643-be86-5ffc179dc325"
    }
}
```

