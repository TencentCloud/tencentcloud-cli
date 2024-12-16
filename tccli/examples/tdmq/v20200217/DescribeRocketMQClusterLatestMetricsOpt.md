**Example 1: test**



Input: 

```
tccli tdmq DescribeRocketMQClusterLatestMetricsOpt --cli-unfold-argument  \
    --ClusterName tdmq_txy_gz_01 \
    --MetricsName topic_count
```

Output: 
```
{
    "Response": {
        "RequestId": "2d61a7c9-aab7-4132-83ed-f38b750fca95",
        "Metrics": 23100.0
    }
}
```

