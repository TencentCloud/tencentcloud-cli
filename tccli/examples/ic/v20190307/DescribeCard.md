**Example 1: 查询物联网卡详情信息**



Input: 

```
tccli ic DescribeCard --cli-unfold-argument  \
    --Sdkappid 1200168178 \
    --Iccid 89860619000013360957
```

Output: 
```
{
    "Response": {
        "RequestId": "5facf6b3-9bd5-480b-98c9-51d7285cf064",
        "Data": {
            "Iccid": "89860619000013360957",
            "Msisdn": "861064606873886",
            "Imsi": "460066520053793",
            "Imei": "",
            "Sdkappid": "1200168178",
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
            "Provider": 0
        }
    }
}
```

