**Example 1: 获取日志列表**



Input: 

```
tccli rum DescribeRumStatsLogList --cli-unfold-argument  \
    --StartTime "1" \
    --Limit 10 \
    --Query "xxx" \
    --EndTime "20" \
    --ID 10
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

**Example 2: 1212**



Input: 

```
tccli rum DescribeRumStatsLogList --cli-unfold-argument  \
    --Query 1 \
    --EndTime 1 \
    --Limit 1 \
    --ID 1 \
    --StartTime 1
```

Output: 
```
{
    "Response": {
        "RequestId": "7987e9a1-cece-4468-b104-cd239f2f6cd6",
        "Result": ""
    }
}
```

