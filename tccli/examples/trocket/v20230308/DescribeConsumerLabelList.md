**Example 1: 查询消费组标签列表成功**



Input: 

```
tccli trocket DescribeConsumerLabelList --cli-unfold-argument  \
    --InstanceId rmq-16je7x5e7o \
    --Group test_group
```

Output: 
```
{
    "Response": {
        "Labels": [
            {
                "Label": "gray_env",
                "State": "ACTIVE",
                "UpdatedAt": 1782700846330
            }
        ],
        "TotalCount": 1,
        "RequestId": "9d466284-9c30-4a9e-abde-7eca2b82e10a"
    }
}
```

