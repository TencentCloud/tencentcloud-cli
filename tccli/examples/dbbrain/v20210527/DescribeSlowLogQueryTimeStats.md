**Example 1: 获取慢日志分段耗时统计**



Input: 

```
tccli dbbrain DescribeSlowLogQueryTimeStats --cli-unfold-argument  \
    --InstanceId crs-k1gjspdk \
    --StartTime 2025-03-27 02:00:00 \
    --EndTime 2025-03-27 02:20:00 \
    --Product redis
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Count": 0,
                "Ratio": 0,
                "To": 0.001
            },
            {
                "Count": 0,
                "From": 0.001,
                "Ratio": 0,
                "To": 0.01
            },
            {
                "Count": 1,
                "From": 0.01,
                "Ratio": 100,
                "To": 0.1
            },
            {
                "Count": 0,
                "From": 0.1,
                "Ratio": 0,
                "To": 0.5
            },
            {
                "Count": 0,
                "From": 0.5,
                "Ratio": 0,
                "To": 1
            },
            {
                "Count": 0,
                "From": 1,
                "Ratio": 0,
                "To": 5
            },
            {
                "Count": 0,
                "From": 5,
                "Ratio": 0,
                "To": 10
            },
            {
                "Count": 0,
                "From": 10,
                "Ratio": 0,
                "To": 15
            },
            {
                "Count": 0,
                "From": 15,
                "Ratio": 0
            }
        ],
        "RequestId": "1ff0b4cf-f59a-440b-a47d-0f3e27eaa172",
        "TotalCount": 9
    }
}
```

