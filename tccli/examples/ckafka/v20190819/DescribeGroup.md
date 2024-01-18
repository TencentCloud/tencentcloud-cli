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
            "TotalCount": 0,
            "GroupList": [
                {
                    "Group": "abc",
                    "Protocol": "abc"
                }
            ],
            "GroupCountQuota": 1
        },
        "RequestId": "abc"
    }
}
```

