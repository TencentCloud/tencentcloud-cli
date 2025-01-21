**Example 1: 获取DescribeDataStaticProject信息**



Input: 

```
tccli rum DescribeDataStaticProject --cli-unfold-argument  \
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
        "Result": "{\"results\":[{\"statement_id\":0,\"series\":[{\"name\":\"static_project_statistics\",\"columns\":[\"time\",\"allCount\",\"successRate\",\"avgDuration\",\"connectTime\",\"domainLookupTime\"],\"values\":[[1737246360,null,null,null,null,null],[1737246420,null,null,null,null,null],[1737246480,null,null,null,null,null],[1737246540,null,null,null,null,null]}],\"total\":1,\"offset\":\"\"}]}",
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

