**Example 1: 新增主题**



Input: 

```
tccli tdmq CreateTopic --cli-unfold-argument  \
    --EnvironmentId felixsshi-ns \
    --TopicName tp-3 \
    --Partitions 2 \
    --ClusterId pulsar-n58wv32op7j2 \
    --PulsarTopicType 3 \
    --DelayMessagePolicy timingwheelPolicy
```

Output: 
```
{
    "Response": {
        "EnvironmentId": "felixsshi-ns",
        "Partitions": 2,
        "Remark": "",
        "TopicName": "tp-3",
        "TopicType": 2,
        "RequestId": "5e554337-cfb5-486c-97a6-1fefcd531e71"
    }
}
```

