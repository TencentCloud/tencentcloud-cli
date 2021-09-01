**Example 1: 查询活码列表**



Input: 

```
tccli wav QueryChannelCodeList --cli-unfold-argument  \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "NextCursor": "iKJ7ml3ltna2Hs+BMN02l6F6RoJbCkeHgCBKcY0Qe+s=",
        "PageData": [
            {
                "Friends": 0,
                "QrCodeUrl": "https://wework.qpic.cn/wwpic/182442_klur6CpKTWe-bVG_1623808245/0",
                "SourceName": "公域车迅达",
                "MsgId": 1404979725786083311,
                "Source": "1001",
                "Remark": "",
                "Name": "erwef",
                "Type": 1,
                "UseUserOpenIdList": [
                    "ShiHao"
                ],
                "AppId": "LXC",
                "UseUserIdList": [
                    1372482008858415111
                ],
                "TagList": [],
                "ConfigId": "f25675c3b271f41f28274c1c7e729f16",
                "Id": 1404979727371530211,
                "SkipVerify": 0,
                "RecStatus": 0
            }
        ],
        "RequestId": "801fbb9d-00ad-4990-b0c9-fdb3e4e48073"
    }
}
```

