**Example 1: 查询指定统计项详情**



Input: 

```
tccli iotvideoindustry DescribeStatisticDetails --cli-unfold-argument  \
    --StartDate 2020-12-09 \
    --EndDate 2020-12-14 \
    --StatisticField StorageUsage
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Date": "2020-12-06 00:00:00",
                "Sum": 3.0
            }
        ],
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8"
    }
}
```

