**Example 1: 查询批次列表**



Input: 

```
tccli trp DescribeCodeBatches --cli-unfold-argument  \
    --CorpId 10000
```

Output: 
```
{
    "Response": {
        "CodeBatches": [
            {
                "BatchId": "20121212000001",
                "CorpId": 10000,
                "BatchCode": "20121212000001",
                "CodeCnt": 10,
                "MerchantId": "eqdmnz7020bmtvi9",
                "ProductId": "tz6jpscwky41u23o9b",
                "BatchType": 0,
                "Remark": "备注",
                "MpTpl": "模板ID",
                "Status": 0,
                "CreateTime": "2021-12-01T06:48:45.000Z",
                "UpdateTime": "2021-12-01T06:48:45.000Z",
                "MerchantName": "商户名称",
                "ProductName": "商品名称",
                "Ext": {},
                "TplName": "模板名称",
                "Job": {
                    "JobId": 1000,
                    "Status": "init"
                },
                "ProductionDate": "2022-05-12",
                "ValidDate": "2022-11-12",
                "Attrs": []
            }
        ],
        "TotalCount": 1,
        "RequestId": "eaa3ccac-d2f5-4df0-a8b3-7b51324e9283"
    }
}
```

