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
        "TotalCount": 0,
        "CodeBatchs": [
            {
                "MpTpl": "xx",
                "Status": 0,
                "Remark": "xx",
                "MerchantName": "xx",
                "CorpId": 0,
                "UpdateTime": "xx",
                "ProductName": "xx",
                "BatchId": "xx",
                "Ext": 0,
                "BatchCode": "xx",
                "CodeCnt": 0,
                "BatchType": 0,
                "CreateTime": "xx",
                "MerchantId": "xx",
                "ProductId": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

