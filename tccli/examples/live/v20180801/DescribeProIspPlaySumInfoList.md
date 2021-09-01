**Example 1: 请求示例**



Input: 

```
tccli live DescribeProIspPlaySumInfoList --cli-unfold-argument  \
    --PlayDomains 5000.playdomain.com \
    --StartTime '2019-03-01 00:00:00' \
    --EndTime '2019-03-01 12:00:00' \
    --StatType Province
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "Name": "山东省",
                "TotalFlux": 50.0,
                "TotalRequest": 50,
                "AvgFluxPerSecond": 10.1
            }
        ],
        "TotalFlux": 100.0,
        "TotalRequest": 100,
        "AvgFluxPerSecond": 100,
        "PageSize": 10,
        "PageNum": 1,
        "TotalNum": 10,
        "TotalPage": 2,
        "StatType": "Province",
        "RequestId": "e6628973-db6a-48f1-9fcd-fe0b3ba54bc9"
    }
}
```

