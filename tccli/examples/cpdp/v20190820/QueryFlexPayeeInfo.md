**Example 1: 查询收款用户**



Input: 

```
tccli cpdp QueryFlexPayeeInfo --cli-unfold-argument  \
    --PayeeId 字符串 \
    --OutUserId 字符串
```

Output: 
```
{
    "Response": {
        "ErrCode": "COMMON.RECORD_NOT_EXIST",
        "ErrMessage": "记录不存在:收款用户不存在",
        "Result": null,
        "RequestId": "37691590-4912-4697-bf7b-e8ce6ac34465"
    }
}
```

