**Example 1: 根据客户uin查询代金券额度**



Input: 

```
tccli intlpartnersmgt QueryVoucherAmountByUin --cli-unfold-argument  \
    --ClientUins 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "TotalAmount": 0.0,
                "ClientUin": 0,
                "RemainAmount": 0.0
            }
        ],
        "RequestId": "xx"
    }
}
```

