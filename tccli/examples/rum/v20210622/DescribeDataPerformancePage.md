**Example 1: 22**



Input: 

```
tccli rum DescribeDataPerformancePage --cli-unfold-argument  \
    --EndTime 1658390700 \
    --Type allcount \
    --ID 1 \
    --StartTime 1658304300
```

Output: 
```
{
    "Response": {
        "RequestId": "ddec0dc8-3268-4571-9ac0-566ae7537495",
        "Result": "{\"request_id\":\"ddec0dc8-3268-4571-9ac0-566ae7537495\",\"results\":[{\"statement_id\":0,\"total\":0},{\"statement_id\":1,\"total\":0},{\"statement_id\":2,\"total\":0},{\"statement_id\":3,\"total\":0}]}"
    }
}
```

**Example 2: 获取PerformancePage信息**



Input: 

```
tccli rum DescribeDataPerformancePage --cli-unfold-argument  \
    --ExtSecond 自定义2 \
    --Engine ie2 \
    --IsAbroad 1 \
    --Area 中国 \
    --NetType 2 \
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

