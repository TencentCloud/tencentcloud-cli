**Example 1: 获取DescribeDataStaticUrl信息**



Input: 

```
tccli rum DescribeDataStaticUrl --cli-unfold-argument  \
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
        "RequestId": "19f7743c-8a5d-4c41-ad6a-742a145b685d",
        "Result": "{\"request_id\":\"19f7743c-8a5d-4c41-ad6a-742a145b685d\",\"results\":[{\"statement_id\":0,\"total\":0,\"offset\":\"\"}]}"
    }
}
```

