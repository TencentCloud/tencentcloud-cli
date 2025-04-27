**Example 1: 查询二级经销商信息**



Input: 

```
tccli intlpartnersmgt QuerySubAgentsDetailV2 --cli-unfold-argument  \
    --Page 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Data": [
            {
                "SubAgentUin": 100001,
                "Name": "fdfd",
                "Remark": "dd",
                "CountOfCustomers": 0,
                "BindTime": "",
                "Credit": 0,
                "RemainingCredit": 0,
                "Voucher": 0,
                "RemainingVoucher": 0,
                "Email": "a@qq.com",
                "Mobile": "151xxx"
            }
        ],
        "RequestId": "abchs-****-****3n2m4m5b"
    }
}
```

