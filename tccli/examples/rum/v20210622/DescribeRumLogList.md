**Example 1: 获取日志列表**



Input: 

```
tccli rum DescribeRumLogList --cli-unfold-argument  \
    --OrderBy "desc" \
    --StartTime "1" \
    --Limit 10 \
    --Query "xxx" \
    --EndTime "20" \
    --ID 10 \
    --Page 1
```

Output: 
```
{
    "Response": {
        "Result": "xxxx",
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

**Example 2: 1**



Input: 

```
tccli rum DescribeRumLogList --cli-unfold-argument  \
    --OrderBy asc \
    --ID 1 \
    --Limit 1 \
    --StartTime 1665994920000 \
    --Query id:1 \
    --EndTime 1 \
    --Page 1
```

Output: 
```
{
    "Response": {
        "RequestId": "72ef03a0-01a8-443e-908a-8573fbeaafcd",
        "Result": ""
    }
}
```

