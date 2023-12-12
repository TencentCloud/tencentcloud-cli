**Example 1: 根据客户uin查询代金券列表**



Input: 

```
tccli intlpartnersmgt QueryVoucherListByUin --cli-unfold-argument  \
    --ClientUins 1 \
    --Status abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ClientUin": 0,
                "TotalCount": 0,
                "Data": [
                    {
                        "VoucherId": "abc",
                        "VoucherStatus": "abc",
                        "TotalAmount": 0,
                        "RemainAmount": 0
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

