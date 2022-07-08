**Example 1: 计算中心-查询提现单列表**



Input: 

```
tccli cpdp QueryFlexPaymentOrderList --cli-unfold-argument  \
    --PageNumber.Count 10 \
    --PageNumber.Index 1 \
    --EndTime 2022-05-12 00:00:00 \
    --PayeeId 90609c1035c348db88b752a69194b1ea \
    --StartTime 2022-05-06 00:00:00
```

Output: 
```
{
    "Response": {
        "ErrCode": "0",
        "ErrMessage": "success",
        "Result": {
            "List": [],
            "Count": 0
        },
        "RequestId": "38d7b2b1-4c14-4a04-81d4-889267bad6db"
    }
}
```

**Example 2: 查询订单列表**



Input: 

```
tccli cpdp QueryFlexPaymentOrderList --cli-unfold-argument  \
    --Environment 字符串 \
    --EndTime 2022-05-12 00:00:00 \
    --PageNumber.Count 1 \
    --PageNumber.Index 1 \
    --StartTime 2022-05-06 00:00:00
```

Output: 
```
{
    "Response": {
        "ErrCode": "SUCCESS",
        "ErrMessage": "成功",
        "Result": {
            "List": [],
            "Count": 0
        },
        "RequestId": "2dc80fdc-530f-4573-bcdb-4a69a82f945b"
    }
}
```

