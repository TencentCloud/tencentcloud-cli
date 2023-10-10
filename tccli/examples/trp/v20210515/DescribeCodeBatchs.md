**Example 1: 查询批次列表**



Input: 

```
tccli trp DescribeCodeBatchs --cli-unfold-argument  \
    --MerchantId eqdmnz7020bmtvi9 \
    --ProductId  \
    --Keyword 20121212000001 \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "CodeBatchs": [
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

