**Example 1: 示例**

示例

Input: 

```
tccli trocket DescribeMQTTMessage --cli-unfold-argument  \
    --InstanceId mqtt-47ka4rdr \
    --Topic topic24 \
    --MsgId 0B8D67F0002D6ACBCFC0557BCEBA0001
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Body": "Hello MQTT111111",
        "MessageId": "0B8D67F0002D6ACBCFC0557BCEBA0001",
        "ProduceTime": "2024-01-17 14:22:57",
        "ProducerAddr": "11.176.16.153:51134",
        "Properties": [
            {
                "Key": "TRACE_ON",
                "Value": "true"
            },
            {
                "Key": "originMqttTopic",
                "Value": "mqtt-47ka4rdr%topic24/1"
            },
            {
                "Key": "INNER_MULTI_DISPATCH",
                "Value": "%LMQ%mqtt-47ka4rdr%topic24%1%"
            },
            {
                "Key": "IS_EMPTY_MSG",
                "Value": "false"
            },
            {
                "Key": "INNER_MULTI_QUEUE_OFFSET",
                "Value": "0"
            },
            {
                "Key": "retryTimes",
                "Value": "0"
            },
            {
                "Key": "extData",
                "Value": "{\"qosLevel\":\"1\"}"
            },
            {
                "Key": "MSG_REGION",
                "Value": "cd"
            },
            {
                "Key": "qosLevel",
                "Value": "1"
            },
            {
                "Key": "UNIQ_KEY",
                "Value": "0B8D67F0002D6ACBCFC0557BCEBA0001"
            },
            {
                "Key": "CLUSTER",
                "Value": "rmqbk-mqtt"
            },
            {
                "Key": "TAGS",
                "Value": "MQTT_COMMON"
            },
            {
                "Key": "__CLIENT_HOST",
                "Value": "11.176.16.153:51134"
            }
        ],
        "RequestId": "e658afc8-e2c0-463e-bf90-3103d881d59f",
        "ShowTopicName": "topic24"
    }
}
```

