**Example 1: 运营中心-设备录像存储统计**



Input: 

```
tccli iotvideoindustry DescribeMonitorDataByDate --cli-unfold-argument  \
    --StartTime 1624201800 \
    --EndTime 1624204810
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Time": 1624204800,
                "Value": {
                    "ExpectTimeLen": 1424325,
                    "RecordTimeLen": 1324546,
                    "FileSize": 12532636
                }
            },
            {
                "Time": 1624204800,
                "Value": {
                    "ExpectTimeLen": 424325,
                    "RecordTimeLen": 124546,
                    "FileSize": 2532636
                }
            }
        ],
        "RequestId": "1d7a62c9-db36-4a5f-9209-2e420883e28f"
    }
}
```

