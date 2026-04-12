**Example 1: 拉取趋势数据**



Input: 

```
tccli rum DescribeIssuesStatisticsTrend --cli-unfold-argument  \
    --ProductId 0dc5283a55 \
    --IssueType 5 \
    --TimeWindow 1 \
    --MetricType 160 \
    --RequestHeader BEGIN{"X-ProductId": "0dc5283a55","X-Tc-Username": "cdx_test"}END
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Data": "{\"base_rsp\":{\"code\":0,\"msg\":\"success\"},\"trends\":[]}",
        "Message": "",
        "RequestId": "74caed67-3121-4708-b255-ca2a010b043d"
    }
}
```

**Example 2: trend信息**



Input: 

```
tccli rum DescribeIssuesStatisticsTrend --cli-unfold-argument  \
    --ProductId 78e6fc7aa0 \
    --ParamToken 5eb862f90d9381a27425afd8955b36a3 \
    --IssueType 70 \
    --TimeWindow 5 \
    --TotalSize False \
    --MetricType 104 \
    --RequestHeader BEGIN{"X-ProductId":"78e6fc7aa0","X-Tc-Username":"v_wxyawang@700001793941"}END \
    --TrendStat 5
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Data": "{\"base_rsp\":{\"code\":0,\"msg\":\"success\"},\"trends\":[{\"time\":\"1759075200\",\"value\":0},{\"time\":\"1759680000\",\"value\":0},{\"time\":\"1760284800\",\"value\":0},{\"time\":\"1760889600\",\"value\":0},{\"time\":\"1761494400\",\"value\":0},{\"time\":\"1762099200\",\"value\":0},{\"time\":\"1762704000\",\"value\":0},{\"time\":\"1763308800\",\"value\":0},{\"time\":\"1763913600\",\"value\":1234411},{\"time\":\"1764518400\",\"value\":182835},{\"time\":\"1765123200\",\"value\":300},{\"time\":\"1765728000\",\"value\":300},{\"time\":\"1766332800\",\"value\":182835}]}",
        "Message": "",
        "RequestId": "4ed0399a-1eec-4cfd-b3a7-b08beeff91d4"
    }
}
```

