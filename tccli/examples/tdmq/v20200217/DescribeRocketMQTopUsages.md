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
                    {
                        "Name": "tenant",
                        "Value": "rocketmq-vvqb9emabapx"
                    },
                    {
                        "Name": "namespace",
                        "Value": "test_ns"
                    },
                    {
                        "Name": "topic",
                        "Value": "test_topic"
                    }
                ]
            },
            {
                "Dimensions": [
                    {
                        "Name": "tenant",
                        "Value": "rocketmq-vvqb9emabapx"
                    },
                    {
                        "Name": "namespace",
                        "Value": "test_ns"
                    },
                    {
                        "Name": "topic",
                        "Value": "test_topic2"
                    }
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

