**Example 1: 查询客户参与增量激励考核信息**



Input: 

```
tccli partners DescribeClientJoinIncreaseList --cli-unfold-argument  \
    --ClientUins 700000000000
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ClientUin": "700000000000",
                "IncreaseGoal": "1000000.00",
                "IncreaseUseAssociateDate": "2025-01-03 14:35:31",
                "IsJoinIncrease": "Y",
                "TLevel": "T0",
                "TotalBaseAmt": "800000.00"
            }
        ],
        "RequestId": "7e4387ac-7373-417a-87fa-b8de96fd9b7b"
    }
}
```

