**Example 1: 枚举消费分组**



Input: 

```
tccli ckafka DescribeGroup --cli-unfold-argument  \
    --InstanceId xxxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "GroupList": [
                {
                    "Group": "qcloud_tocos",
                    "Protocol": "consumer"
                }
            ]
        },
        "RequestId": "c931f394-7d72-4ad4-8d70-5a225708c762"
    }
}
```

