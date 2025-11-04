**Example 1: 正常获取connection列表**



Input: 

```
tccli trabbit DescribeRabbitMQServerlessConnection --cli-unfold-argument  \
    --InstanceId amqp-slbswcjhay \
    --VirtualHost /
```

Output: 
```
{
    "Response": {
        "Connections": [
            {
                "Channels": 10,
                "ConnectionName": "11.141.232.162:2594 -> 21.63.172.58:5672",
                "Heartbeat": 60,
                "IncomingBytes": 5,
                "MaxChannel": 1024,
                "OutgoingBytes": 766.65,
                "PeerHost": "11.141.232.162",
                "Protocol": "AMQP 0-9-1",
                "SSL": false,
                "State": "running",
                "User": "ledou"
            },
            {
                "Channels": 1,
                "ConnectionName": "11.151.193.8:35695 -> 21.63.172.58:5672",
                "Heartbeat": 60,
                "IncomingBytes": 9.92,
                "MaxChannel": 1024,
                "OutgoingBytes": 763.8,
                "PeerHost": "11.151.193.8",
                "Protocol": "AMQP 0-9-1",
                "SSL": false,
                "State": "running",
                "User": "ledou"
            }
        ],
        "RequestId": "8ea767cf-5895-4eda-985b-cf739d9074b5",
        "TotalCount": 2
    }
}
```

