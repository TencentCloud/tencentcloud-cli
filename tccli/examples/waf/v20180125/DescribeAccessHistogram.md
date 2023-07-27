**Example 1: 访问日志柱状趋势图**



Input: 

```
tccli waf DescribeAccessHistogram --cli-unfold-argument  \
    --TopicId 1ae37c76-df99-4e2b-998c-20f39eba6226 \
    --From 1625395948532 \
    --To 1626000748532 \
    --Query 
```

Output: 
```
{
    "Response": {
        "Interval": 12096000,
        "TotalCount": 6221,
        "RequestId": "9b02bf9e-c89c-42c3-9ae1-685f968fa02d",
        "HistogramInfos": [
            {
                "BTime": 0,
                "Count": 0
            }
        ]
    }
}
```

