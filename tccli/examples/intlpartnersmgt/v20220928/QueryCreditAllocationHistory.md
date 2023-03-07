**Example 1: 查询客户信用分配历史信息**



Input: 

```
tccli intlpartnersmgt QueryCreditAllocationHistory --cli-unfold-argument  \
    --ClientUin 1 \
    --Page 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "RequestId": "2b7c676e-bb4b-449d-89e6-4866132036c6",
        "History": [
            {
                "Operator": "PartnerTest Limited",
                "Credit": 0.1,
                "AllocatedTime": "2022-07-28 15:04:08",
                "AllocatedCredit": 1000.1
            }
        ]
    }
}
```

