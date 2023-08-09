**Example 1: 请求示例**

省份和运营商 [映射表](/document/api/267/34019)。

Input: 

```
tccli live DescribeProvinceIspPlayInfoList --cli-unfold-argument  \
    --StatType Bandwidth \
    --EndTime 2019-02-02T00:00:00+08:00 \
    --StartTime 2019-02-01T00:00:00+08:00 \
    --PlayDomains 5000.playdomain.com \
    --Granularity 1
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "Time": "2019-02-01T00:00:00+08:00",
                "Value": 500.0
            }
        ],
        "StatType": "Bandwidth",
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

