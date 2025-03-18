**Example 1: 示例**

示例

Input: 

```
tccli mqtt DescribeClientList --cli-unfold-argument  \
    --InstanceId mqtt-2vnk55xv \
    --ClientId sub \
    --Number 10
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Clients": [
            {
                "ClientAddress": "11.176.16.153:63066",
                "ClientId": "sub_client1",
                "ConnectTime": 1710314923557,
                "ConnectionStatus": "CONNECTED",
                "CreateTime": 1710314923554,
                "DisconnectTime": 0,
                "Keepalive": 60,
                "MQTTClientSubscriptions": [
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
                "ProtocolVersion": 4
            },
            {
                "ClientAddress": "11.176.16.153:62048",
                "ClientId": "sub_client2",
                "ConnectTime": 1710314912143,
                "ConnectionStatus": "CONNECTED",
                "CreateTime": 1710314912140,
                "DisconnectTime": 0,
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
                "ProtocolVersion": 4
            }
        ],
        "RequestId": "9f81924f-41e8-4f24-aaf2-61da7da9c713"
    }
}
```

