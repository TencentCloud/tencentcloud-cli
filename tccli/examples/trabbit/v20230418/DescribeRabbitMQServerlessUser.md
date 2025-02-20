**Example 1: 成功**



Input: 

```
tccli trabbit DescribeRabbitMQServerlessUser --cli-unfold-argument  \
    --InstanceId amqp-44w9928j
```

Output: 
```
{
    "Response": {
        "RequestId": "12bedf1e-5377-46e1-ae05-07225440b16f",
        "TotalCount": 1,
        "RabbitMQUserList": [
            {
                "InstanceId": "ramqp-cpssyrct",
                "User": "testUser",
                "Password": "",
                "Description": "",
                "Tags": [],
                "CreateTime": "2024-10-21 15:52:45:000",
                "ModifyTime": "2024-10-21 15:52:45:000",
                "Type": "default",
                "MaxConnections": null,
                "MaxChannels": null
            }
        ]
    }
}
```

