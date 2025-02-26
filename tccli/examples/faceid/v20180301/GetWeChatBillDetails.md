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
                        "Name": "韦小宝",
                        "Seq": "e594dc57-9ee3-409b-a8e4-7b46945887c3",
                        "IdCard": "11204416541220243X",
                        "ErrorCode": "0",
                        "IsNeedCharge": true,
                        "ChargeType": "核身",
                        "ReqTime": "1638781186273",
                        "Sim": "100.00"
                    }
                ],
                "BizToken": "3DCE6611F1A-0F1E-455BD-BE13-34C05CEA7681",
                "RuleId": "96"
            }
        ],
        "HasNextPage": true,
        "RequestId": "fdce508f-0813-4229-8a2e-439b851ec99f"
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
                        "Name": "韦小宝",
                        "Seq": "e594dc357-9ee3-409b-a8e4-7b469458827c3",
                        "IdCard": "11204416541220243X",
                        "ErrorCode": "0",
                        "IsNeedCharge": true,
                        "ChargeType": "核身",
                        "ReqTime": "1638781186273",
                        "Sim": "100.00"
                    }
                ],
                "BizToken": "FFE6212B2-8DC2-4D03-BC1D-29C5054A221F9",
                "RuleId": "96"
            }
        ],
        "HasNextPage": false,
        "RequestId": "a87bb0ee-e95b-415be-b562-117944c4ceb1"
    }
}
```

**Example 3: 获取后续页面数据异常示例**

获取后续页面数据，输入不存在的RuleId。

Input: 

```
tccli faceid GetWeChatBillDetails --cli-unfold-argument  \
    --Date 2020-09-22 \
    --Cursor 1873 \
    --RuleId 23
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.RuleIdNotExist",
            "Message": "RuleId不存在，请到人脸核身控制台申请。"
        },
        "RequestId": "c5f6c7e4-2b4e-4a77-acc5-d111fffe8302"
    }
}
```

