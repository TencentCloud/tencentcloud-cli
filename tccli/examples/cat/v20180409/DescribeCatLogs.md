**Example 1: 查询拨测流水 示例**



Input: 

```
tccli cat DescribeCatLogs --cli-unfold-argument  \
    --Offset 0 \
    --Limit 2 \
    --TaskId 226791
```

Output: 
```
{
    "Response": {
        "TotalCount": 126,
        "CatLogs": [
            {
                "Time": "2019-12-12 00:02:01",
                "CatTypeName": "http",
                "TaskId": 260409,
                "ClientIp": "180.163.9.66",
                "City": "hz",
                "CityName": "杭州",
                "Isp": "ctc",
                "IspName": "电信",
                "ServerIp": "106.54.177.242",
                "DomainName": "tb.xryen.com",
                "ParseTime": 3,
                "ConnectTime": 2988,
                "SendTime": 0,
                "WaitTime": 0,
                "ReceiveTime": 0,
                "TotalTime": 2991,
                "ResultType": 1,
                "ResultCode": 10009,
                "ReqPkgSize": 151,
                "RspPkgSize": 0,
                "RespMsg": "Connect Error",
                "ReqMsg": "GET tb.xryen.com/do.php HTTP/1.1\r\nUser-Agent: curl\r\nCookie: \r\nAuthorization: Basic : Og==\r\n\r\n"
            },
            {
                "Time": "2019-12-12 00:01:57",
                "CatTypeName": "http",
                "TaskId": 260409,
                "ClientIp": "125.39.253.111",
                "City": "tj",
                "CityName": "天津",
                "Isp": "cuc",
                "IspName": "联通",
                "ServerIp": "106.54.177.242",
                "DomainName": "tb.xryen.com",
                "ParseTime": 3,
                "ConnectTime": 8976,
                "SendTime": 0,
                "WaitTime": 0,
                "ReceiveTime": 0,
                "TotalTime": 8979,
                "ResultType": 1,
                "ResultCode": 10009,
                "ReqPkgSize": 151,
                "RspPkgSize": 0,
                "RespMsg": "Connect Error",
                "ReqMsg": "GET tb.xryen.com/do.php HTTP/1.1\r\nUser-Agent: curl\r\nCookie: \r\nAuthorization: Basic : Og==\r\n\r\n"
            }
        ],
        "RequestId": "ed82e699-d3c4-408d-b12c-21b0b9aaea5c"
    }
}
```

