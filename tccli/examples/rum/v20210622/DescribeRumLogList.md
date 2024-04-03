**Example 1: 123**



Input: 

```
tccli rum DescribeRumLogList --cli-unfold-argument  \
    --OrderBy asc \
    --ID 4 \
    --Limit 1 \
    --StartTime 1676390400000 \
    --Query id:4 \
    --EndTime 1676476799000 \
    --Page 1
```

Output: 
```
{
    "Response": {
        "RequestId": "a6bafa2f-3f6a-4f1a-b9a3-d1d848d34168",
        "Result": ""
    }
}
```

**Example 2: 获取日志列表**

获取日志列表

Input: 

```
tccli rum DescribeRumLogList --cli-unfold-argument  \
    --OrderBy desc \
    --ID 120000 \
    --Limit 100 \
    --StartTime 1665994920000 \
    --Query id:120000 \
    --EndTime 1673417492913 \
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

