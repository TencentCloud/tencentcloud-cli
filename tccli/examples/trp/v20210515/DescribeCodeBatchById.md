**Example 1: 查询批次信息**



Input: 

```
tccli trp DescribeCodeBatchById --cli-unfold-argument  \
    --BatchId 20121212000001xx
```

Output: 
```
{
    "Response": {
        "CodeBatch": {
            "BatchId": "20121212000001xx",
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
        },
        "RequestId": "eaa3ccac-d2f5-4df0-a8b3-7b51324e9283"
    }
}
```

