**Example 1: xc**



Input: 

```
tccli rum DescribeRumLogExports --cli-unfold-argument  \
    --PageNum 1 \
    --ID 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "RequestId": "641faf00-efc4-46b5-b3ce-03383133dc08",
        "Result": ""
    }
}
```

**Example 2: 获取日志列表**



Input: 

```
tccli rum DescribeRumLogExports --cli-unfold-argument  \
    --PageSize 10 \
    --ID 10 \
    --PageNum 1
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

