**Example 1: 请求示例**



Input: 

```
tccli redis DescribeInstanceMonitorHotKey --cli-unfold-argument  \
    --InstanceId crs-r34wkc1d \
    --SpanType 4
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Key": "haha",
                "Type": "string",
                "Count": 123
            }
        ],
        "RequestId": "20d64b80-cbac-49a0-8771-42e326db5c45"
    }
}
```

