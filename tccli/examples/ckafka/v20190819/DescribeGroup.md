**Example 1: 枚举消费分组**



Input: 

```
tccli ckafka DescribeGroup --cli-unfold-argument  \
    --InstanceId ckafka-pkwxedpq
```

Output: 
```
{
    "Response": {
        "RequestId": "5936dc43-9496-44fa-977b-25f3048352be",
        "Result": {
            "GroupCountQuota": 200,
            "GroupList": [
                {
                    "Group": "test-group",
                    "Protocol": "consumer"
                }
            ],
            "TotalCount": 1
        }
    }
}
```

