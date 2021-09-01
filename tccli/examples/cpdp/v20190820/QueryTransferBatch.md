**Example 1: 批量转账批次查询正常返回**

批量转账批次查询正常返回

Input: 

```
tccli cpdp QueryTransferBatch --cli-unfold-argument  \
    --MerchantId 1589516681 \
    --MerchantBatchNo 6695169909762424846 \
    --NeedQueryDetail true \
    --Offset 20 \
    --Limit 100 \
    --DetailStatus SUCCESS
```

Output: 
```
{
    "Response": {
        "MerchantId": "1589516681",
        "MerchantBatchNo": "6695169909762424846",
        "BatchId": "1030001016801203285292020073100004980005",
        "MerchantAppId": "wx1844094c6d71d8a2",
        "BatchStatus": "FINISHED",
        "BatchType": "API",
        "BatchName": "brainbian test批次",
        "BatchRemark": "remark",
        "CloseReason": null,
        "TotalAmount": 66,
        "TotalNum": 1,
        "CreateTime": "2020-07-31T16:45:05+08:00",
        "UpdateTime": "2020-07-31T16:45:07+08:00",
        "SuccessAmount": 66,
        "SuccessNum": 1,
        "FailAmount": 0,
        "FailNum": 0,
        "RequestId": "555"
    }
}
```

