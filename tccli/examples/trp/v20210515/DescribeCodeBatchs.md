**Example 1: 查询批次列表**



Input: 

```
tccli trp DescribeCodeBatchs --cli-unfold-argument  \
    --MerchantId pn30msjjxwga \
    --ProductId  \
    --Keyword  \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "CodeBatchs": [
            {
                "BatchId": "20241022112952826",
                "CorpId": 10000,
                "BatchCode": "20241022112952826",
                "CodeCnt": 250,
                "MerchantId": "pn30msjjxwga",
                "ProductId": "97zu51y30awe",
                "BatchType": 1,
                "Remark": "优质产品批次",
                "MpTpl": "base",
                "Status": 1,
                "CreateTime": "2023-10-01T11:30:50.321Z",
                "UpdateTime": "2023-10-05T15:50:45.212Z",
                "MerchantName": "优品商贸",
                "ProductName": "高档家用电器",
                "Ext": {},
                "TplName": "默认",
                "Job": {
                    "JobId": 7520,
                    "Status": "完成"
                },
                "ProductionDate": "2023-09-30T00:00:00.000Z",
                "ValidDate": "2023-12-31T00:00:00.000Z",
                "Attrs": []
            }
        ],
        "TotalCount": 1,
        "RequestId": "f01dbe8b-09ad-4d75-bbde-30cf67c1f4b7"
    }
}
```

