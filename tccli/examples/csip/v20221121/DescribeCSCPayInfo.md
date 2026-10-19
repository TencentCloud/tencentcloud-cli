**Example 1: 查询配额用量**

显式传入 NeedQuotaUsed=true，返回各计费项配额总量与已使用量

Input: 

```
tccli csip DescribeCSCPayInfo --cli-unfold-argument  \
    --NeedQuotaUsed True
```

Output: 
```
{
    "Response": {
        "AppID": 260095525,
        "OrderStatus": 1,
        "PayMode": 1,
        "BeginTime": "2026-03-27 10:11:03",
        "EndTime": "2026-04-27 10:11:03",
        "AutoRenew": 1,
        "TimeSpan": 1,
        "TimeUnit": "m",
        "ResourceId": "csc-34d2fbec-2982-11f1-b5cc-525400e2504e",
        "TimeNow": "2026-04-02 11:47:41",
        "Uin": "700******039",
        "NickName": "700******039",
        "NewUser": 1,
        "QuotaList": [
            {
                "QuotaKey": "sv_soccloud_edition_ultimate_hp",
                "QuotaNum": 2,
                "QuotaUsed": 2,
                "QuotaGranted": 0
            },
            {
                "QuotaKey": "sv_soccloud_cspm_cspm",
                "QuotaNum": 100,
                "QuotaUsed": 145,
                "QuotaGranted": 12
            }
        ],
        "QuotaUsedError": "",
        "RequestId": "16a42165-319b-48b0-8a18-00ba52a07cf6"
    }
}
```

**Example 2: 正常请求**

无订单账号查询，订单相关字段返回零值

Input: 

```
tccli csip DescribeCSCPayInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "NewUser": 1,
        "RequestId": "16a42165-319b-48b0-8a18-00ba52a07cf6",
        "Uin": "700******039",
        "NickName": "700******039"
    }
}
```

