**Example 1: 获取第一页数据**

获取第一页数据时，Cursor值传0。当HasNextPage的值为true时，继续调用接口。

Input: 

```
tccli faceid GetWeChatBillDetails --cli-unfold-argument  \
    --Date 2020-09-22 \
    --Cursor 0 \
    --RuleId 2
```

Output: 
```
{
    "Response": {
        "NextCursor": 1873,
        "WeChatBillDetails": [
            {
                "ChargeCount": 1,
                "ChargeDetails": [
                    {
                        "ErrorMessage": "成功",
                        "Name": "**钱",
                        "Seq": "xxxxx-xxxxx-xxxxx-xxxxx",
                        "Idcard": "4************8",
                        "ErrorCode": 0,
                        "IsNeedCharge": true,
                        "ChargeType": "核身",
                        "ReqTime": "1638781186273",
                        "Sim": "100.00"
                    }
                ],
                "BizToken": "xxxxxxxx-xxxxxx-xxxxxx",
                "RuleId": "96"
            }
        ],
        "HasNextPage": true,
        "RequestId": "xxxxxx-xxxxxx-xxxxxxx"
    }
}
```

**Example 2: 获取后续页面数据**

获取后续页面数据时，将上一页返回的NextCursor值作为入参传入。当HasNextPage的值为false的时候，即可停止调用接口。

Input: 

```
tccli faceid GetWeChatBillDetails --cli-unfold-argument  \
    --Date 2020-09-22 \
    --Cursor 1873 \
    --RuleId 2
```

Output: 
```
{
    "Response": {
        "NextCursor": 28888,
        "WeChatBillDetails": [
            {
                "ChargeCount": 1,
                "ChargeDetails": [
                    {
                        "ErrorMessage": "成功",
                        "Name": "**钱",
                        "Seq": "xxxxx-xxxxx-xxxxx-xxxxx",
                        "Idcard": "4************8",
                        "ErrorCode": 0,
                        "IsNeedCharge": true,
                        "ChargeType": "核身",
                        "ReqTime": "1638781186273",
                        "Sim": "100.00"
                    }
                ],
                "BizToken": "xxxxxxxx-xxxxxx-xxxxxx",
                "RuleId": "96"
            }
        ],
        "HasNextPage": false,
        "RequestId": "xxxxxx-xxxxxx-xxxxxxx"
    }
}
```

