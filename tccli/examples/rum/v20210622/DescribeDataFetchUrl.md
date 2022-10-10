**Example 1: 获取DescribeDataFetchUrl信息**



Input: 

```
tccli rum DescribeDataFetchUrl --cli-unfold-argument  \
    --ExtSecond 自定义2 \
    --Engine ie2 \
    --IsAbroad 1 \
    --Area 中国 \
    --NetType 2 \
    --CostType avg \
    --Level 1 \
    --Os apple \
    --Brand apple \
    --Isp 中国移动 \
    --VersionNum 版本 \
    --Platform 2 \
    --ExtThird 自定义3 \
    --ExtFirst 自定义1 \
    --StartTime 1625444040 \
    --Device 三星 \
    --From index.html \
    --EndTime 1625454840 \
    --Type pagepv \
    --ID 1 \
    --Browser ie
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

**Example 2: 333**



Input: 

```
tccli rum DescribeDataFetchUrl --cli-unfold-argument  \
    --EndTime 1625454840 \
    --Type condition \
    --ID 1 \
    --StartTime 1625444040
```

Output: 
```
{
    "Response": {
        "RequestId": "d8b037d7-08ae-401d-84cf-071e7a133c00",
        "Result": "{\"request_id\":\"d8b037d7-08ae-401d-84cf-071e7a133c00\",\"results\":[{\"statement_id\":0,\"total\":0},{\"statement_id\":1,\"total\":0}]}"
    }
}
```

**Example 3: 1**



Input: 

```
tccli rum DescribeDataFetchUrl --cli-unfold-argument  \
    --EndTime 1658390700 \
    --Type allcount \
    --ID 1 \
    --StartTime 1658304300
```

Output: 
```
{
    "Response": {
        "RequestId": "d446c290-7034-47d3-8d72-46e7a692f5ac",
        "Result": "{\"request_id\":\"d446c290-7034-47d3-8d72-46e7a692f5ac\",\"results\":[{\"statement_id\":0,\"total\":0},{\"statement_id\":1,\"total\":0}]}"
    }
}
```

