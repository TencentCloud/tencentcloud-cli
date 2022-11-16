**Example 1: CreateDidService**

创建Did服务

Input: 

```
tccli tdid CreateDidService --cli-unfold-argument  \
    --AgencyName xx \
    --AppName xx \
    --ConsortiumName xx \
    --ClusterId xx \
    --GroupName xx \
    --ConsortiumId 617 \
    --GroupId 6
```

Output: 
```
{
    "Response": {
        "Task": {
            "Id": 37,
            "AppId": 251005746,
            "ClusterId": "bcos-fmtkyt8xne",
            "GroupId": 6,
            "ServiceId": 0,
            "Status": 0,
            "ErrorCode": "",
            "ErrorMsg": "",
            "CreateTime": "2021-07-23 13:52:50",
            "UpdateTime": "2021-07-23 13:52:50"
        },
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425"
    }
}
```

