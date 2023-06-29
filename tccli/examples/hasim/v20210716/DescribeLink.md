**Example 1: 查询云兔连接详细信息**

查询云兔连接详细信息

Input: 

```
tccli hasim DescribeLink --cli-unfold-argument  \
    --LinkID 1000001
```

Output: 
```
{
    "Response": {
        "Data": {
            "IsActiveLog": false,
            "TacticStatus": 0,
            "Status": 0,
            "ActiveTime": "xx",
            "Tags": [
                {
                    "Comment": "xx",
                    "Name": "xx",
                    "UpdatedAt": "xx",
                    "ID": 10002,
                    "CreatedAt": "xx"
                }
            ],
            "DataUse": 0,
            "SmsUse": 0,
            "Report": {
                "UploadTime": "xx",
                "DevModel": "xx",
                "Log": 0,
                "Ping": 36000,
                "Delay": 800,
                "DevType": "xx",
                "Version": "xx",
                "Tele": 1,
                "Tid": 100001,
                "Status": 0,
                "Lac": "xx",
                "Lat": "xx",
                "Rss": 0,
                "Imei": "xx",
                "Cell": "xx",
                "MonthFirstTime": "xx",
                "Iccid": "xx",
                "Lng": "xx"
            },
            "CardID": "xx",
            "TeleOperator": 0,
            "Cards": [
                {
                    "AccountTime": "xx",
                    "ActiveTime": "xx",
                    "Msisdn": "xx",
                    "LinkID": 0,
                    "TeleOperator": 2,
                    "ICCID": "xx",
                    "IMSI": "xx"
                }
            ],
            "TacticExpireTime": "xx",
            "ID": 39000000015,
            "TacticID": 0,
            "ExpireTime": "xx",
            "AudioUse": 0,
            "LinkedState": 1
        },
        "RequestId": "xx"
    }
}
```

