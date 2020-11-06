**Example 1: 查看站点列表**

查看已经添加的站点信息

Input: 

```
tccli cws DescribeSites --cli-unfold-argument  \
    --Filters.0.Name Name \
    --Filters.0.Values QQ 微信 \
    --Filters.1.Name Url \
    --Filters.1.Values http%3A%2F%2Fdemo.aisec.cn
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "Sites": [
            {
                "Appid": 1251001047,
                "CreatedAt": "2018-03-19T16:33:45+08:00",
                "Id": 4,
                "LastScanCancelTime": "",
                "LastScanExtsCount": "",
                "LastScanFinishTime": "2018-03-19T17:38:56+08:00",
                "LastScanPageCount": 0,
                "LastScanScannerType": "",
                "LastScanStartTime": "2018-03-22T00:00:00+08:00",
                "LastScanTaskId": 0,
                "LastScanVulsNum": 10,
                "LastScanNoticeNum": 1,
                "LastScanVulsHighNum": 0,
                "LastScanVulsLowNum": 0,
                "LastScanVulsMiddleNum": 0,
                "LastScanVulsNoticeNum": 0,
                "MonitorId": 0,
                "MonitorStatus": 0,
                "Name": "Spqs6w6el",
                "ScanStatus": 0,
                "Progress": 0,
                "UpdatedAt": "2018-03-19T17:38:56+08:00",
                "Url": "http://demo.aisec.cn/demo/aisec/",
                "VerifyStatus": 0,
                "LoginCheckKw": "",
                "LoginCheckUrl": "",
                "LoginCookie": "",
                "LoginCookieValid": 0,
                "NeedLogin": 0,
                "ScanDisallow": "",
                "UserAgent": ""
            }
        ],
        "TotalCount": 1
    }
}
```

