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
        "NextCursor": "xxx",
        "RequestId": "8e368d08-faa7-4cb3-ab55-1eb820b2a915",
        "PageData": [
            {
                "Friends": 0,
                "QrCodeUrl": "xxx",
                "SourceName": "xxx",
                "MsgId": 0,
                "Source": "xxx",
                "Remark": "xxx",
                "Name": "xxx",
                "Type": 0,
                "UseUserOpenIdList": [
                    "jonsen"
                ],
                "AppId": "xxx",
                "UseUserIdList": [
                    1234556778899
                ],
                "TagList": [
                    {
                        "GroupName": "xxx",
                        "BizGroupId": "11111111111111111",
                        "Type": 1,
                        "TagName": "xxx",
                        "BizTagIdStr": "xxx",
                        "TagId": "xxx",
                        "BizTagId": "xxx"
                    }
                ],
                "ConfigId": "xxx",
                "Id": 11111111111111111111111,
                "SkipVerify": 0,
                "RecStatus": 0
            }
        ]
    }
}
```

