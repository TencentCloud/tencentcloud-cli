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
                "Url": "https://anxin.qq.com/q99j9ovp5c6sok7l5g",
                "OpenId": "g3ST2ZYcreGP9jpqgKHOjuB1e0GrlI0t",
                "ScanTime": "2023-10-10 00:00:00",
                "Ip": "192.168.1.1",
                "Country": "中国",
                "Province": "广东",
                "City": "广州"
            }
        ],
        "RequestId": "eaa3ccac-d2f5-4df0-a8b3-7b51324e9283"
    }
}
```

