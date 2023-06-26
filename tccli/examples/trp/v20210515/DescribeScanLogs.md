**Example 1: 查询扫描记录**

查询扫描明细，查询参数 Code, Openid 至少需要一个

Input: 

```
tccli trp DescribeScanLogs --cli-unfold-argument  \
    --Code https://anxin.m.qq.com/qr/eqdmnz70000243813742005003
```

Output: 
```
{
    "Response": {
        "Products": [],
        "ScanLogs": [
            {
                "LogId": 2,
                "Openid": "abc",
                "Nickname": "demo",
                "CreateTime": "2021-12-06T07:13:35.000Z",
                "Code": "https://anxin.m.qq.com/qr/eqdmnz70000243813742005003",
                "CorpId": 10000,
                "MerchantId": "",
                "ProductId": "",
                "Ip": "127.0.0.1",
                "Country": "",
                "Province": "广东",
                "City": "广州",
                "District": ""
            }
        ],
        "TotalCount": 1,
        "RequestId": "ee4f0117-953f-4a5b-9a3f-6a1831ac3c0a"
    }
}
```

