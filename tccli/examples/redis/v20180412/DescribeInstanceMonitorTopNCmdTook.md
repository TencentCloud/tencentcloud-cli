**Example 1: 请求示例**



Input: 

```
tccli redis DescribeInstanceMonitorTopNCmdTook --cli-unfold-argument  \
    --InstanceId crs-r34wkc1d \
    --SpanType 4
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Cmd": "ping",
                "Took": 4688000
            }
        ],
        "RequestId": "95308f10-19d9-4313-bedf-cb65a846826f"
    }
}
```

