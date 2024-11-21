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
        "TotalCount": 1,
        "ScanLogs": [
            {
                "LogId": 1,
                "Openid": "g3ST2ZYcreGP9jpqgKHOjuB1e0GrlI0t",
                "Nickname": "张三",
                "CreateTime": "2024-10-22T14:00:00Z",
                "Code": "https://anxin.qq.com/q99j9ovp5c6sok7l5g",
                "CorpId": 10000,
                "MerchantId": "pn30msjjxwga",
                "ProductId": "97zu51y30awe",
                "Ip": "192.168.1.1",
                "Country": "中国",
                "Province": "广东",
                "City": "深圳",
                "District": "南山区",
                "Unionid": "ue1Hd0ne2dzIy1oE",
                "First": 1,
                "BatchId": "20241022112952826",
                "Type": 1,
                "MerchantName": "商户名称",
                "ProductName": "产品名称",
                "ProductLogo": "",
                "Status": 1,
                "Verify": 1
            }
        ],
        "RequestId": "eaa3ccac-d2f5-4df0-a8b3-7b51324e9283"
    }
}
```

