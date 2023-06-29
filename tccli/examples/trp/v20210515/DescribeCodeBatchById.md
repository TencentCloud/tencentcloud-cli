**Example 1: 查询批次信息**



Input: 

```
tccli trp DescribeCodeBatchById --cli-unfold-argument  \
    --BatchId xfetmgoiky2nms6nk8
```

Output: 
```
{
    "Response": {
        "CodeBatch": {
            "MpTpl": "xx",
            "Status": 0,
            "Remark": "xx",
            "MerchantName": "xx",
            "CorpId": 0,
            "UpdateTime": "xx",
            "ProductName": "xx",
            "BatchId": "xx",
            "Ext": {},
            "BatchCode": "xx",
            "CodeCnt": 0,
            "BatchType": 0,
            "CreateTime": "xx",
            "MerchantId": "xx",
            "ProductId": "xx"
        },
        "RequestId": "xx"
    }
}
```

