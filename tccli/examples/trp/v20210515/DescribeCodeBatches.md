**Example 1: 查询批次列表**



Input: 

```
tccli trp DescribeCodeBatches --cli-unfold-argument  \
    --CorpId 1000
```

Output: 
```
{
    "Response": {
        "CodeBatches": [
            {
                "BatchId": "abc",
                "CorpId": 0,
                "BatchCode": "abc",
                "CodeCnt": 0,
                "MerchantId": "abc",
                "ProductId": "abc",
                "BatchType": 0,
                "Remark": "abc",
                "MpTpl": "abc",
                "Status": 0,
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "MerchantName": "abc",
                "ProductName": "abc",
                "Ext": {},
                "TplName": "abc",
                "Job": {
                    "JobId": 0,
                    "Status": "abc"
                },
                "ProductionDate": "abc",
                "ValidDate": "abc",
                "Attrs": []
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

