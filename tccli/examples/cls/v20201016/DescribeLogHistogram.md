**Example 1: 获取直方图信息**



Input: 

```
tccli cls DescribeLogHistogram --cli-unfold-argument  \
    --TopicId 682d0718-07bb-4ec0-9fda-f1e9a2767e0b \
    --From 1608794855000 \
    --To 1608794855000 \
    --Query select *from a \
    --Interval 10
```

Output: 
```
{
    "Response": {
        "Interval": 10,
        "TotalCount": 15,
        "HistogramInfos": [
            {
                "Count": 5,
                "BTime": 1619331870
            },
            {
                "Count": 10,
                "BTime": 1619332410
            }
        ],
        "RequestId": "b276cb6e-4687-11eb-b378-0242ac130002"
    }
}
```

