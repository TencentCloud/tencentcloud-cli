**Example 1: Ip白名单列表**



Input: 

```
tccli captcha DescribeIpWhiteListInternational --cli-unfold-argument  \
    --Name haha \
    --PageIndex 1 \
    --PageSize 10 \
    --CaptchaAppid 179000009
```

Output: 
```
{
    "Response": {
        "RequestId": "c634b435-7bfe-4f04-b447-b995a2dd8adb",
        "Data": {
            "DataList": [
                {
                    "Id": 173,
                    "Name": "formdata",
                    "CaptchaAppid": 199999290,
                    "Ip": "93.26.59.11",
                    "Status": 0,
                    "CreatedTime": "2024-01-30T08:01:59+08:00",
                    "UpdatedTime": "2024-01-30T08:19:16+08:00",
                    "Comment": ""
                },
                {
                    "Id": 170,
                    "Name": "formdata",
                    "CaptchaAppid": 199999290,
                    "Ip": "127.0.0.1",
                    "Status": 0,
                    "CreatedTime": "2024-01-30T07:41:29+08:00",
                    "UpdatedTime": "2024-01-30T08:19:16+08:00",
                    "Comment": ""
                }
            ],
            "Total": 2,
            "PageIndex": 1
        },
        "CaptchaCode": 0,
        "CaptchaMsg": "success"
    }
}
```

