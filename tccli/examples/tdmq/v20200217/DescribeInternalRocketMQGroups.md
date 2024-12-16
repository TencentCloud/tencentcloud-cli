**Example 1: 查询消费组列表**

查询消费组列表

Input: 

```
tccli tdmq DescribeInternalRocketMQGroups --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Groups": [
            {
                "Name": "xx",
                "ConsumerNum": 1,
                "TPS": 1,
                "TotalAccumulative": 0,
                "ConsumptionMode": 0,
                "ReadEnabled": true,
                "RetryPartitionNum": 1,
                "CreateTime": 1,
                "UpdateTime": 1,
                "ClientProtocol": "xx",
                "Remark": "xx",
                "ConsumerType": "xx",
                "BroadcastEnabled": true,
                "GroupType": "xx",
                "RetryMaxTimes": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

