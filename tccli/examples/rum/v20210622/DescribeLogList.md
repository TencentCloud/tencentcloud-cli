**Example 1: 获取日志列表**



Input: 

```
tccli rum DescribeLogList --cli-unfold-argument  \
    --StartTime "1" \
    --EndTime "20" \
    --Query "xxx" \
    --Limit 10 \
    --Context "xxx" \
    --Sort "desc" \
    --ActionType "searchlog" \
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

