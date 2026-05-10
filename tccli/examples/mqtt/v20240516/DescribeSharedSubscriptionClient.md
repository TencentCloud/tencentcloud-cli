**Example 1: 查询共享订阅组客户端**

查询共享订阅组客户端

Input: 

```
tccli mqtt DescribeSharedSubscriptionClient --cli-unfold-argument  \
    --InstanceId mqtt-zj944d74 \
    --SharedName mock-name \
    --TopicFilter mock-topic
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "ClientId": "mock-1",
                "Online": true,
                "SharedName": "mock-name",
                "TopicFilter": "mock-topic"
            },
            {
                "ClientId": "mock-2",
                "Online": false,
                "SharedName": "mock-name",
                "TopicFilter": "mock-topic"
            }
        ],
        "RequestId": "e1ff6dcf-d154-4bdc-acb9-22eaa384d07e",
        "TotalCount": 2
    }
}
```

