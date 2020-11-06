**Example 1: 请求示例**



Input: 

```
tccli live DescribePlayErrorCodeSumInfoList --cli-unfold-argument  \
    --PlayDomains 5000.playdomain.com \
    --StartTime '2019-03-01 00:00:00' \
    --EndTime '2019-03-01 12:00:00'
```

Output: 
```
{
    "Response": {
        "ProIspInfoList": [
            {
                "CountryAreaName": "中国",
                "ProvinceName": "山东省",
                "IspName": "中国移动",
                "Code2xx": 11,
                "Code3xx": 12,
                "Code4xx": 10,
                "Code5xx": 19
            }
        ],
        "TotalCodeList": [
            {
                "Code": "200",
                "Num": 11
            },
            {
                "Code": "302",
                "Num": 12
            },
            {
                "Code": "403",
                "Num": 1000
            },
            {
                "Code": "500",
                "Num": 19
            }
        ],
        "TotalCodeAll": 100,
        "TotalCode2xx": 11,
        "TotalCode3xx": 12,
        "TotalCode4xx": 10,
        "TotalCode5xx": 29,
        "PageNum": 1,
        "PageSize": 10,
        "TotalPage": 10,
        "TotalNum": 100,
        "RequestId": "e6628973-db6a-48f1-9fcd-fe0b3ba54bc9"
    }
}
```

