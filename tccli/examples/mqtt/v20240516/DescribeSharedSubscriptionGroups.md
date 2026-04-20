**Example 1: 查询共享订阅组列表**

查询共享订阅组列表

Input: 

```
tccli mqtt DescribeSharedSubscriptionGroups --cli-unfold-argument  \
    --InstanceId mqtt-zj944d74
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "CreateTime": 1749468454000,
                "ExpiryInterval": 10,
                "InstanceId": "mqtt-zj944d74",
                "LbStrategy": 1,
                "Remark": "helklo2",
                "SharedName": "test-aa",
                "UpdateTime": 1749798776000
            },
            {
                "CreateTime": 1749398400000,
                "ExpiryInterval": 10,
                "InstanceId": "mqtt-zj944d74",
                "LbStrategy": 1,
                "Remark": null,
                "SharedName": "test-bb",
                "UpdateTime": 1749398400000
            },
            {
                "CreateTime": 1749475014000,
                "ExpiryInterval": 10,
                "InstanceId": "mqtt-zj944d74",
                "LbStrategy": 1,
                "Remark": null,
                "SharedName": "test-cc",
                "UpdateTime": 1749475016000
            },
            {
                "CreateTime": 1749475039000,
                "ExpiryInterval": 15,
                "InstanceId": "mqtt-zj944d74",
                "LbStrategy": 1,
                "Remark": null,
                "SharedName": "test-dd",
                "UpdateTime": 1749475041000
            },
            {
                "CreateTime": 1749798707000,
                "ExpiryInterval": 10,
                "InstanceId": "mqtt-zj944d74",
                "LbStrategy": 1,
                "Remark": "hello",
                "SharedName": "test-ee",
                "UpdateTime": 1749798707000
            }
        ],
        "RequestId": "f320bebc-c033-4cc5-ab39-72c477e98b24",
        "TotalCount": 5
    }
}
```

