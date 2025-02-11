**Example 1: 根据客户uin查询代金券列表**



Input: 

```
tccli intlpartnersmgt QueryVoucherListByUin --cli-unfold-argument  \
    --ClientUins 800000190982 \
    --Status Used
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
                        "VoucherId": "TVSYNGAEJTSZX9EWXJ1DK9",
                        "VoucherStatus": "Used",
                        "TotalAmount": 0,
                        "RemainAmount": 0
                    }
                ]
            }
        ],
        "RequestId": "9d8660fce37404d36e5710f13f0191fd"
    }
}
```

