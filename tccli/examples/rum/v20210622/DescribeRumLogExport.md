**Example 1: 获取日志列表**



Input: 

```
tccli rum DescribeRumLogExport --cli-unfold-argument  \
    --Name xx \
    --Fields xx \
    --StartTime xx \
    --Query xx \
    --EndTime xx \
    --ID 0
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
tccli rum DescribeRumLogExport --cli-unfold-argument  \
    --Query id:1 \
    --EndTime 1 \
    --Name  \
    --StartTime 1665994920000 \
    --ID 1
```

Output: 
```
{
    "Response": {
        "RequestId": "763188d1-9f99-45e8-8bbf-bcdffa8f58f0",
        "Result": ""
    }
}
```

