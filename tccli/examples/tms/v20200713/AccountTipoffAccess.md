**Example 1: 账号举报**

举报存在诈骗、违规、违法等行为的账号

Input: 

```
tccli tms AccountTipoffAccess --cli-unfold-argument  \
    --ReportedAccount 123456789 \
    --ReportedAccountType 2 \
    --SenderAccount 987654321 \
    --SenderAccountType 2 \
    --SenderIP 127.0.0.1 \
    --EvilType 1 \
    --EvilContent 王者代练，入会需交费，+q：123456789
```

Output: 
```
{
    "Response": {
        "RequestId": "9d31ec33",
        "Data": {
            "ResultCode": 0,
            "ResultMsg": "success"
        }
    }
}
```

