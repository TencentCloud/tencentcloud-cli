**Example 1: 结算中心-查询payee用户信息**



Input: 

```
tccli cpdp ModifyFlexPayeeAccountRightStatus --cli-unfold-argument  \
    --AccountRightType 字符串 \
    --PayeeId 字符串 \
    --AccountRightStatus 字符串
```

Output: 
```
{
    "Response": {
        "ErrCode": "1",
        "ErrMessage": "fail",
        "Result": null,
        "RequestId": "8fd1c191-a3da-4759-bc4a-13587bd8a89f"
    }
}
```

