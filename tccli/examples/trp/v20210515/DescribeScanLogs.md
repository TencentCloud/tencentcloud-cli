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
        "Products": [
            {
                "LogId": 0,
                "Openid": "abc",
                "Nickname": "abc",
                "CreateTime": "abc",
                "Code": "abc",
                "CorpId": 0,
                "MerchantId": "abc",
                "ProductId": "abc",
                "Ip": "abc",
                "Country": "abc",
                "Province": "abc",
                "City": "abc",
                "District": "abc",
                "Unionid": "abc",
                "First": 0,
                "BatchId": "abc",
                "Type": 0,
                "MerchantName": "abc",
                "ProductName": "abc",
                "ProductLogo": "abc",
                "Status": 0,
                "Verify": 0
            }
        ],
        "TotalCount": 0,
        "ScanLogs": [
            {
                "LogId": 0,
                "Openid": "abc",
                "Nickname": "abc",
                "CreateTime": "abc",
                "Code": "abc",
                "CorpId": 0,
                "MerchantId": "abc",
                "ProductId": "abc",
                "Ip": "abc",
                "Country": "abc",
                "Province": "abc",
                "City": "abc",
                "District": "abc",
                "Unionid": "abc",
                "First": 0,
                "BatchId": "abc",
                "Type": 0,
                "MerchantName": "abc",
                "ProductName": "abc",
                "ProductLogo": "abc",
                "Status": 0,
                "Verify": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

