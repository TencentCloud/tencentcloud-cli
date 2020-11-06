**Example 1: 请求示例**



Input: 

```
tccli live DescribeTopClientIpSumInfoList --cli-unfold-argument  \
    --StartTime '2019-03-01 00:00:00' \
    --EndTime '2019-03-01 04:00:00' \
    --PageSize 2 \
    --PageNum 2 \
    --OrderParam TotalFlux
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

