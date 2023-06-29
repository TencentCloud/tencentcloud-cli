**Example 1: 根据客户uin查询代金券列表**



Input: 

```
tccli intlpartnersmgt QueryVoucherListByUin --cli-unfold-argument  \
    --Status xx \
    --ClientUins 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TotalCount": 0,
                "ClientUin": 0,
                "Data": [
                    {
                        "VoucherId": "xx",
                        "TotalAmount": 0.0,
                        "RemainAmount": 0.0,
                        "VoucherStatus": "xx"
                    }
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

