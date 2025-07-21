**Example 1: 查询SIP通道内线路由策略列表信息**



Input: 

```
tccli ccc DescribeSipTrunkRouteList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "22590cbf-da98-4e81-a7bd-659140900268",
        "TotalCount": 1,
        "SipTrunkRouteList": [
            {
                "Id": 1,
                "Uin": "xxxxx",
                "AppId": 111111,
                "SdkAppId": 1400000000,
                "Direction": "out",
                "Regex": "^1\\d{5}$",
                "Prefix": "1",
                "Length": 6,
                "State": 1
            }
        ]
    }
}
```

