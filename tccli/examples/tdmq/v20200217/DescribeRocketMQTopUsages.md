**Example 1: 获取 Group 堆积数量排序**



Input: 

```
tccli tdmq DescribeRocketMQTopUsages --cli-unfold-argument  \
    --ClusterId rocketmq-abc \
    --MetricName consumeLag \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Dimensions": [
            {
                "Dimensions": [
                    {},
                    {},
                    {}
                ]
            },
            {
                "Dimensions": [
                    {},
                    {},
                    {}
                ]
            }
        ],
        "RequestId": "f0288e86-ee7d-4a73-a788-81ca6680b06c",
        "Values": [
            309,
            0
        ]
    }
}
```

