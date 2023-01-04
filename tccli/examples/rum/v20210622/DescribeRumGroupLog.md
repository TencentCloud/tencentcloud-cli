**Example 1: 获取日志列表**



Input: 

```
tccli rum DescribeRumGroupLog --cli-unfold-argument  \
    --OrderBy "desc" \
    --StartTime "1" \
    --Limit 10 \
    --Query "xxx" \
    --EndTime "20" \
    --ID 10 \
    --Page 1 \
    --GroupField xx
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

**Example 2: 2312**



Input: 

```
tccli rum DescribeRumGroupLog --cli-unfold-argument  \
    --OrderBy asc \
    --ID 1 \
    --Limit 1 \
    --GroupField  \
    --StartTime 1 \
    --Query 1 \
    --EndTime 1 \
    --Page 1
```

Output: 
```
{
    "Response": {
        "RequestId": "81a43a52-d00f-462a-82da-89841117f4ca",
        "Result": ""
    }
}
```

