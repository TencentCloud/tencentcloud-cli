**Example 1: 请求示例**



Input: 

```
tccli live DescribeVisitTopSumInfoList --cli-unfold-argument  \
    --StartTime '2019-03-01 00:00:00' \
    --EndTime '2019-03-01 04:00:00' \
    --PageSize 2 \
    --PageNum 2 \
    --TopIndex StreamId \
    --OrderParam TotalFlux
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "AvgFluxPerSecond": 4.773,
                "Name": "CSZFMPP360",
                "TotalRequest": 36590,
                "TotalFlux": 69023.772
            },
            {
                "AvgFluxPerSecond": 4.634,
                "Name": "CSNXMPP360",
                "TotalRequest": 88629,
                "TotalFlux": 67009.417
            }
        ],
        "OrderParam": "TotalFlux",
        "PageNum": 2,
        "PageSize": 2,
        "RequestId": "k54e3deb-f318-4147-8a68-3c959642f9ec",
        "TopIndex": "StreamId",
        "TotalNum": 1000,
        "TotalPage": 500
    }
}
```

