**Example 1: 明细号查询明细单正常示例**

明细号查询明细单正常示例

Input: 

```
tccli cpdp QueryTransferDetail --cli-unfold-argument  \
    --MerchantId 1589516661 \
    --BatchId 1030001016801203285292020080400005400005 \
    --DetailId 1040001016801203285292020080400005010006
```

Output: 
```
{
    "Response": {
        "MerchantId": "1589160661",
        "MerchantBatchNo": "6695160909762424836",
        "BatchId": "1030001016801203285292020080400005400005",
        "MerchantAppId": "wx1844094c6p71d8a2",
        "MerchantDetailNo": "6695165909980028644",
        "DetailId": "1040001016801203285292020080400005010006",
        "DetailStatus": "SUCCESS",
        "TransferAmount": 36,
        "TransferRemark": "测试910",
        "FailReason": null,
        "OpenId": "oMliQ0XhIzf32t2D2K9SnvTtxCIs",
        "UserName": "张三",
        "InitiateTime": "2020-08-01T11:36:44+08:00",
        "UpdateTime": "2020-08-01T11:36:44+08:00",
        "RequestId": "c386d591-307d-460d-8235-c2a9e1c8de19"
    }
}
```

