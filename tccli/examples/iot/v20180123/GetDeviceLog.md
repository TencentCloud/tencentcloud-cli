**Example 1: 获取设备日志**

获取设备日志

Input: 

```
tccli iot GetDeviceLog --cli-unfold-argument  \
    --ProductId iot-4e0wsxpi \
    --DeviceNames dev0 dev5 \
    --StartTime '2018-03-30 00:00:00' \
    --EndTime '2018-03-30 23:00:00' \
    --Size 5 \
    --Type comm
```

Output: 
```
{
    "Response": {
        "RequestId": "4a82f1ad-1072-4378-ad6e-b29dd417bf6c",
        "DeviceLog": [
            {
                "Id": "uuid0020",
                "Msg": "{\"data\":\"this is msg body\"}",
                "Code": "err-code",
                "Timestamp": 1521792750222,
                "DeviceName": "dev-name",
                "Method": "method"
            },
            {
                "Id": "uuid00215",
                "Msg": "{\"data\":\"this is msg body\"}",
                "Code": "err-code",
                "Timestamp": 1521792750222,
                "DeviceName": "dev-name",
                "Method": "method"
            },
            {
                "Id": "uuid00232",
                "Msg": "{\"data\":\"this is msg body\"}",
                "Code": "err-code",
                "Timestamp": 1521792750222,
                "DeviceName": "dev-name",
                "Method": "method"
            },
            {
                "Id": "uuid00233",
                "Msg": "{\"data\":\"this is msg body\"}",
                "Code": "err-code",
                "Timestamp": 1521792750222,
                "DeviceName": "dev-name",
                "Method": "method"
            },
            {
                "Id": "uuid00238",
                "Msg": "{\"data\":\"this is msg body\"}",
                "Code": "err-code",
                "Timestamp": 1521792750222,
                "DeviceName": "dev-name",
                "Method": "method"
            }
        ],
        "ScrollId": "DnF1ZXJ5VGhlbkZldGNoCgAAAAAAAAL-FmM2eDR6OUQ2Ukh1Nnh2R0ZvclJCb0EAAAAAAAAC_xZjNng0ejlENlJIdTZ4dkdGb3JSQm9BAAAAAAAAAwAWYzZ4NHo5RDZSSHU2eHZHRm9yUkJvQQAAAAAAAAMCFmM2eDR6OUQ2Ukh1Nnh2R0ZvclJCb0EAAAAAAAADARZjNng0ejlENlJIdTZ4dkdGb3JSQm9BAAAAAAAAAwQWYzZ4NHo5RDZSSHU2eHZHRm9yUkJvQQAAAAAAAAMDFmM2eDR6OUQ2Ukh1Nnh2R0ZvclJCb0EAAAAAAAADBRZjNng0ejlENlJIdTZ4dkdGb3JSQm9BAAAAAAAAAwYWYzZ4NHo5RDZSSHU2eHZHRm9yUkJvQQAAAAAAAAMHFmM2eDR6OUQ2Ukh1Nnh2R0ZvclJCb0E=",
        "ScrollTimeout": 60
    }
}
```

