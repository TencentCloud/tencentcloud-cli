**Example 1: 查询物联网卡片列表**



Input: 

```
tccli ic DescribeCards --cli-unfold-argument  \
    --Limit 0 \
    --Sdkappid 1400168178 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "5facf6b3-9bd5-480b-98c9-51d7285cf064",
        "Data": {
            "Total": "10",
            "List": [
                {
                    "Iccid": "89860619000013360924",
                    "Msisdn": "861064606873883",
                    "Imsi": "460066520053790",
                    "Imei": "",
                    "Sdkappid": "1400168178",
                    "Teleoperator": 2,
                    "CardStatus": 1,
                    "NetworkStatus": 0,
                    "ActivitedTime": "0",
                    "Type": 1,
                    "ProductId": "LT-1-10M",
                    "PoolId": "",
                    "DataUsedInPeriod": 0,
                    "DataTotalInPeriod": 0,
                    "ProductExpiredTime": "0",
                    "Description": "",
                    "CreatedTime": "2019-01-04 17:41:42",
                    "ModifiedTime": "2019-01-04 18:30:44",
                    "PreorderCnt": 2,
                    "IsActivated": 1,
                    "OrderId": "20190104157897",
                    "AutoRenew": 0,
                    "Remark": "",
                    "AllowArrears": 0,
                    "NeedSms": 0,
                    "Provider": 1
                },
                {
                    "Iccid": "89860619000013360932",
                    "Msisdn": "861064606873884",
                    "Imsi": "460066520053791",
                    "Imei": "",
                    "Sdkappid": "1400168178",
                    "Teleoperator": 2,
                    "CardStatus": 1,
                    "NetworkStatus": 0,
                    "ActivitedTime": "0",
                    "Type": 1,
                    "ProductId": "LT-1-10M",
                    "PoolId": "",
                    "DataUsedInPeriod": 0,
                    "DataTotalInPeriod": 0,
                    "ProductExpiredTime": "0",
                    "Description": "",
                    "CreatedTime": "2019-01-04 17:41:42",
                    "ModifiedTime": "2019-01-04 18:30:44",
                    "PreorderCnt": 2,
                    "IsActivated": 1,
                    "OrderId": "20190104157897",
                    "AutoRenew": 0,
                    "Remark": "",
                    "AllowArrears": 0,
                    "NeedSms": 0,
                    "Provider": 1
                },
                {
                    "Iccid": "89860619000013360940",
                    "Msisdn": "861064606873885",
                    "Imsi": "460066520053792",
                    "Imei": "",
                    "Sdkappid": "1400168178",
                    "Teleoperator": 2,
                    "CardStatus": 1,
                    "NetworkStatus": 0,
                    "ActivitedTime": "0",
                    "Type": 1,
                    "ProductId": "LT-1-10M",
                    "PoolId": "",
                    "DataUsedInPeriod": 0,
                    "DataTotalInPeriod": 0,
                    "ProductExpiredTime": "0",
                    "Description": "",
                    "CreatedTime": "2019-01-04 17:41:42",
                    "ModifiedTime": "2019-01-04 18:30:44",
                    "PreorderCnt": 2,
                    "IsActivated": 1,
                    "OrderId": "20190104157897",
                    "AutoRenew": 0,
                    "Remark": "",
                    "AllowArrears": 0,
                    "NeedSms": 0,
                    "Provider": 1,
                    "OtherData": 123.1
                }
            ]
        }
    }
}
```

