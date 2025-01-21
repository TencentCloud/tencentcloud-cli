**Example 1: 1**

1

Input: 

```
tccli rum DescribeDataPvUrlStatistics --cli-unfold-argument  \
    --StartTime 1697078966 \
    --Type ckuv \
    --EndTime 1697093366 \
    --ID 120000
```

Output: 
```
{
    "Response": {
        "RequestId": "4f93b7fc-1857-4f4d-b3ac-eb63719a8bc5",
        "Result": "{\"request_id\":\"4f93b7fc-1857-4f4d-b3ac-eb63719a8bc5\",\"results\":[{\"statement_id\":0,\"total\":0,\"offset\":\"\"}]}"
    }
}
```

**Example 2: 测试**

测试

Input: 

```
tccli rum DescribeDataPvUrlStatistics --cli-unfold-argument  \
    --StartTime 1683270000 \
    --Type ckuv \
    --EndTime 1683356400 \
    --ID 120000
```

Output: 
```
{
    "Response": {
        "RequestId": "85acc203-d239-4e47-bc04-195cb09e9e83",
        "Result": "{\"request_id\":\"85acc203-d239-4e47-bc04-195cb09e9e83\",\"results\":[{\"statement_id\":0,\"total\":0,\"offset\":\"\"}]}"
    }
}
```

**Example 3: 获取DescribeDataPvUrlStatistics信息**



Input: 

```
tccli rum DescribeDataPvUrlStatistics --cli-unfold-argument  \
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
    --From index.html
```

Output: 
```
{
    "Response": {
        "Result": "{\"request_id\":\"65a8fec7-2b39-4b11-893f-3715279d235f\",\"results\":[{\"statement_id\":0,\"total\":0,\"offset\":\"\"}]}",
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

