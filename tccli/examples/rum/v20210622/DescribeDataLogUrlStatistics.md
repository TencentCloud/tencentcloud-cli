**Example 1: 获取LogUrlStatistics信息**



Input: 

```
tccli rum DescribeDataLogUrlStatistics --cli-unfold-argument  \
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
        "Result": "{\"request_id\":\"4d50a7e7-cb3a-47af-a4ff-f545bfd54880\",\"results\":[{\"statement_id\":1,\"series\":[{\"name\":\"log_url_statistics\",\"columns\":[\"time\",\"allCount\"],\"values\":[],\"total\":1,\"offset\":\"\"},{\"statement_id\":2,\"total\":0,\"offset\":\"\"}]}",
        "RequestId": "4d50a7e7-cb3a-47af-a4ff-f545bfd54880"
    }
}
```

