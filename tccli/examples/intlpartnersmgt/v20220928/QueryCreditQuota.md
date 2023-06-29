**Example 1: 查询子客信用**

计费查询子客信用

Input: 

```
tccli intlpartnersmgt QueryCreditQuota --cli-unfold-argument  \
    --ClientUin 123 \
    --ComponentName qcost
```

Output: 
```
{
    "Response": {
        "TotalCredit": 100,
        "RemainingCredit": 100,
        "RemainingVoucher": 0,
        "Force": 0,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

