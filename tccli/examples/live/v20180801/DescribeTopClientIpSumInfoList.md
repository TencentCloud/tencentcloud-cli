**Example 1: 请求示例**



Input: 

```
tccli live DescribeTopClientIpSumInfoList --cli-unfold-argument  \
    --OrderParam TotalFlux \
    --EndTime 2019-03-01T04:00:00+08:00 \
    --PageNum 2 \
    --PageSize 2 \
    --StartTime 2019-03-01T00:00:00+08:00
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "ClientIp": "119.44.7.168",
                "CountryArea": "中国",
                "Province": "湖南省",
                "TotalFailedRequest": 4,
                "TotalFlux": 13321.099,
                "TotalRequest": 740
            },
            {
                "ClientIp": "119.44.7.175",
                "CountryArea": "中国",
                "Province": "湖南省",
                "TotalFailedRequest": 3,
                "TotalFlux": 12566.334,
                "TotalRequest": 2318
            }
        ],
        "OrderParam": "TotalFlux",
        "PageNum": 2,
        "PageSize": 2,
        "RequestId": "k54e3deb-f318-4147-8a68-3c959642f9ec",
        "TotalNum": 1000,
        "TotalPage": 500
    }
}
```

