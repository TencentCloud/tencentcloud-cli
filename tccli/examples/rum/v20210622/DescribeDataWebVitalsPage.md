**Example 1: 获取WebVitalsPage信息**



Input: 

```
tccli rum DescribeDataWebVitalsPage --cli-unfold-argument  \
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
        "RequestId": "2fe018e0-9e76-46cb-9ddb-cfbd6835ff19",
        "Result": "{\"request_id\":\"2fe018e0-9e76-46cb-9ddb-cfbd6835ff19\",\"results\":[{\"statement_id\":0,\"series\":[{\"name\":\"webvitals_page_statistics\",\"columns\":[\"time\",\"LCP\",\"FID\",\"CLS\",\"FCP\"],\"values\":[[0,null,null,null,null]]}],\"total\":1,\"offset\":\"\"}]}"
    }
}
```

