**Example 1: 查询云兔连接列表**

查询云兔连接列表

Input: 

```
tccli hasim DescribeLinks --cli-unfold-argument  \
    --LinkID 1000101 \
    --ICCID 8279***72 \
    --IMEI 874****123 \
    --Status 1 \
    --TeleOperator 1 \
    --TagID 100101 \
    --TacticID 100101 \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Total": 0,
            "List": [
                {
                    "ID": 0,
                    "Status": 0,
                    "ActiveTime": "0001-01-01T00:00:00Z",
                    "ExpireTime": "0001-01-01T00:00:00Z",
                    "DataUse": 0,
                    "AudioUse": 0,
                    "SmsUse": 0,
                    "LinkedState": 0,
                    "TacticID": 0,
                    "TacticStatus": 0,
                    "TacticExpireTime": "abc",
                    "IsActiveLog": true,
                    "TeleOperator": 0,
                    "Report": {
                        "Imei": "89860919730018794506",
                        "Lng": "",
                        "Lat": "37.29",
                        "Lac": "749069031",
                        "Cell": "1031",
                        "Iccid": "89860919730018751670",
                        "Rss": -10,
                        "Tele": 1,
                        "Tid": 100001,
                        "Ping": 36000,
                        "Delay": 800,
                        "Log": 0,
                        "DevType": "TestDevice",
                        "DevModel": "TD-10037",
                        "Version": "v1.0.1",
                        "UploadTime": "2021-07-16T11:19:26+08:00",
                        "Status": 0,
                        "MonthFirstTime": "2021-07-16T11:19:26+08:00"
                    }
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

