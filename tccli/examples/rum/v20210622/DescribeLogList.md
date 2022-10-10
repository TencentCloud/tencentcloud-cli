**Example 1: 获取日志列表**



Input: 

```
tccli rum DescribeLogList --cli-unfold-argument  \
    --Sort "desc" \
    --StartTime "1" \
    --ActionType "searchlog" \
    --Limit 10 \
    --Context "xxx" \
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

