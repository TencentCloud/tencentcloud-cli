**Example 1: 查询标签详情成功**



Input: 

```
tccli trocket DescribeConsumerLabel --cli-unfold-argument  \
    --InstanceId rmq-16je7x5e7o \
    --Group test_group \
    --Label gray_env
```

Output: 
```
{
    "Response": {
        "Label": {
            "Label": "gray_env",
            "State": "DELETING",
            "UpdatedAt": 1782717266193
        },
        "RequestId": "928cf954-b233-4582-b2af-135686c5b3e9"
    }
}
```

