**Example 1: 样例**

样例

Input: 

```
tccli trocket DescribeMQTTClient --cli-unfold-argument  \
    --InstanceId mqtt-2vnk55xv \
    --ClientId sub_client2
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "CleanSession": true,
        "ClientAddress": "11.176.16.153:23354",
        "ClientId": "sub_client2",
        "ConnectTime": 1711444795304,
        "ConnectionStatus": "CONNECTED",
        "CreateTime": 1711443908331,
        "DisconnectTime": 0,
        "Inbound": {
            "Bytes": 40,
            "Items": [
                {
                    "Count": 1,
                    "MessageType": "SUBACK",
                    "Qos": 0
                },
                {
                    "Count": 1,
                    "MessageType": "CONNACK",
                    "Qos": 0
                },
                {
                    "Count": 14,
                    "MessageType": "PINGRESP",
                    "Qos": 0
                }
            ]
        },
        "Keepalive": 60,
        "MQTTClientSubscriptions": [
            {
                "Qos": 1,
                "TopicFilter": "home/sun/+/"
            },
            {
                "Qos": 1,
                "TopicFilter": "home/temp/+/"
            },
            {
                "Qos": 0,
                "TopicFilter": "home/humidity/+/"
            },
            {
                "Qos": 2,
                "TopicFilter": "home/person/+/"
            }
        ],
        "OutBound": {
            "Bytes": 134,
            "Items": [
                {
                    "Count": 1,
                    "MessageType": "CONNECT",
                    "Qos": 0
                },
                {
                    "Count": 1,
                    "MessageType": "SUBSCRIBE",
                    "Qos": 1
                },
                {
                    "Count": 14,
                    "MessageType": "PINGREQ",
                    "Qos": 0
                }
            ]
        },
        "ProtocolVersion": 4,
        "RequestId": "b59aa63c-6cc6-418a-92c7-c205cb30d4cd"
    }
}
```

