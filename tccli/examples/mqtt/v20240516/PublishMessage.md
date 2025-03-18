**Example 1: 发布消息到主题**



Input: 

```
tccli mqtt PublishMessage --cli-unfold-argument  \
    --InstanceId mqtt-xxx \
    --TargetTopic test/a/b \
    --Payload Hello MQTT! \
    --Encoding plain \
    --Qos 1 \
    --Retain False
```

Output: 
```
{
    "Response": {
        "RequestId": "416510a6-f614-487d-bbca-e7fdbf72fc29"
    }
}
```

