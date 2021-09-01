**Example 1: 请求示例**



Input: 

```
tccli redis DescribeInstanceMonitorTookDist --cli-unfold-argument  \
    --InstanceId crs-5a4py64p \
    --Date 2019-11-07 \
    --SpanType 4
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Ladder": -1,
                "Size": 0
            },
            {
                "Ladder": 5,
                "Size": 0
            },
            {
                "Ladder": 10,
                "Size": 0
            },
            {
                "Ladder": 1,
                "Size": 178942
            },
            {
                "Ladder": 50,
                "Size": 0
            },
            {
                "Ladder": 200,
                "Size": 0
            }
        ],
        "RequestId": "6f6441b4-884e-40b0-8503-5e5f5e6b6714"
    }
}
```

