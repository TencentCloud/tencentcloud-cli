**Example 1: 请求示例**



Input: 

```
tccli redis DescribeInstanceMonitorTopNCmd --cli-unfold-argument  \
    --InstanceId crs-5a4py64p \
    --SpanType 4
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Cmd": "ping",
                "Count": 179562
            }
        ],
        "RequestId": "f5ce4f15-bf90-4958-95ca-97fa086ace28"
    }
}
```

