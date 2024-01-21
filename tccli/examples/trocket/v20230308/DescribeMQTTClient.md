**Example 1: 标准请求**

标准请求

Input: 

```
tccli trocket DescribeMQTTClient --cli-unfold-argument  \
    --InstanceId mqtt-25m2jz9j \
    --ClientId recv01
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "ClientAddress": "/11.176.16.157:43440",
        "ClientId": "recv01",
        "ConnectTime": 1703581008199,
        "ConnectionStatus": "CONNECTED",
        "CreateTime": 1703581008198,
        "DisconnectTime": 0,
        "Keepalive": 60,
        "MQTTClientSubscriptions": [
            {
                "Qos": 1,
                "TopicFilter": "mqtt-25m2jz9j%111/r1/"
            },
            {
                "Qos": 1,
                "TopicFilter": "mqtt-25m2jz9j%111/r/+/"
            },
            {
                "Qos": 2,
                "TopicFilter": "mqtt-25m2jz9j%111/r2/"
            }
        ],
        "ProtocolVersion": 4,
        "RequestId": "b0f34768-130d-4a15-89d3-d3ca1976b4b7"
    }
}
```

**Example 2: 示例**

示例

Input: 

```
tccli trocket DescribeMQTTClient --cli-unfold-argument  \
    --InstanceId mqtt-47ka4rdr \
    --ClientId subscribe_client
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "ClientAddress": "11.176.16.153:37360",
        "ClientId": "subscribe_client",
        "ConnectTime": 1705632841108,
        "ConnectionStatus": "CONNECTED",
        "CreateTime": 1705632841106,
        "DisconnectTime": 0,
        "Keepalive": 60,
        "MQTTClientSubscriptions": [
            {
                "Qos": 0,
                "TopicFilter": "mqtt-47ka4rdr%topic24"
            }
        ],
        "ProtocolVersion": 4,
        "RequestId": "4ec9c58c-e6ac-4149-9673-b8f0d526a6aa"
    }
}
```

