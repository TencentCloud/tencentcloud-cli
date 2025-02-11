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
                "ClientUin": 0,
                "TotalAmount": 0,
                "RemainAmount": 0
            }
        ],
        "RequestId": "9d8660fce37404d36e5710f13f0191fd"
    }
}
```

