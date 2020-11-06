**Example 1: 获取实例列表**



Input: 

```
tccli ckafka DescribeInstances --cli-unfold-argument  \
    --InstanceId instance-will-s \
    --SearchWord tre \
    --Offset 0 \
    --Limit 10 \
    --Status 0 1 2
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "InstanceList": [
                {
                    "InstanceId": "instance-will-s",
                    "InstanceName": "treTest",
                    "IfCommunity": true,
                    "Status": 1
                }
            ]
        },
        "RequestId": "31740399-5d06-404b-a4b5-3652e21c8a1d"
    }
}
```

