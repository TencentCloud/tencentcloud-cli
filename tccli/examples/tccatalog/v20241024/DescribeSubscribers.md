**Example 1: DescribeSubscribers示例**



Input: 

```
tccli tccatalog DescribeSubscribers --cli-unfold-argument  \
    --SubscriberId None \
    --SubscriberName None
```

Output: 
```
{
    "Response": {
        "RequestId": "96f5dedd-82b8-430b-92a2-0e23c89b4e64",
        "Subscribers": [
            {
                "AppId": "1300298608",
                "CreateTime": 1760952893625,
                "Description": "hello",
                "Filters": "[{\"Name\":\"AppId\",\"Values\":[\"113\"]},{\"Name\":\"Operation\",\"Values\":[\"CREATE_TABLE\"]}]",
                "Params": "[{\"Key\":\"url\",\"Value\":\"pulsar://localhost:6650\"},{\"Key\":\"topic\",\"Value\":\"wedata-113\"}]",
                "Region": "ap-guangzhou",
                "SinkType": "pulsar",
                "State": "off",
                "SubscriberId": "ea96648b-43ed-4625-b502-59e1c7e0ca70",
                "SubscriberName": "wedata-dfs-sdf",
                "Uin": "700001601851",
                "UpdateTime": 1760952893625
            }
        ]
    }
}
```

