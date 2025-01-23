**Example 1: 获取DescribeDataCustomUrl信息**



Input: 

```
tccli rum DescribeDataCustomUrl --cli-unfold-argument  \
    --ID 1 \
    --StartTime 1625444040 \
    --EndTime 1625454840 \
    --Type pagepv \
    --Level 1 \
    --Isp 中国移动 \
    --Area 中国 \
    --NetType 2 \
    --Platform 2 \
    --Device 三星 \
    --VersionNum 版本 \
    --ExtFirst 自定义1 \
    --ExtSecond 自定义2 \
    --ExtThird 自定义3 \
    --IsAbroad 1 \
    --Browser ie \
    --Os apple \
    --Engine ie2 \
    --Brand apple \
    --From index.html \
    --CostType avg
```

Output: 
```
{
    "Response": {
        "RequestId": "44202a67-c864-4d29-82f4-bfd483327e60",
        "Result": "{\"request_id\":\"44202a67-c864-4d29-82f4-bfd483327e60\",\"results\":[{\"statement_id\":0,\"total\":0,\"offset\":\"\"},{\"statement_id\":1,\"total\":0,\"offset\":\"\"}]}"
    }
}
```

