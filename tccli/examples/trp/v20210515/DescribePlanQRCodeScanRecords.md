**Example 1: 查询安心计划二维码扫码记录**



Input: 

```
tccli trp DescribePlanQRCodeScanRecords --cli-unfold-argument  \
    --StartTime 2023-10-10 00:00:00 \
    --EndTime 2023-10-10 23:59:59 \
    --PageNo 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Ret": 0,
        "Total": 1,
        "Data": [
            {
                "Url": "xxx",
                "OpenId": "",
                "ScanTime": "2023-10-10 00:00:00",
                "Ip": "",
                "Country": "",
                "Province": "",
                "City": ""
            }
        ],
        "RequestId": "abc"
    }
}
```

