**Example 1: 创建消费组灰度标签成功**



Input: 

```
tccli trocket CreateConsumerLabel --cli-unfold-argument  \
    --InstanceId rmq-16je7x5e7o \
    --Label gray_env \
    --Group test_group
```

Output: 
```
{
    "Response": {
        "Group": "test_group",
        "InstanceId": "rmq-16je7x5e7o",
        "Label": "gray_env",
        "RequestId": "4f97b0a7-a11e-4428-878c-ffb54ee79f60"
    }
}
```

