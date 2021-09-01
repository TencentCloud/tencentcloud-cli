**Example 1: 发起批量转账正确返回示例**

发起批量转账，参数完全正确的情况

Input: 

```
tccli cpdp CreateTransferBatch --cli-unfold-argument  \
    --MerchantId 129284394 \
    --MerchantAppId wxf636efh567hg4356 \
    --MerchantBatchNo plfk2020042013 \
    --BatchName 2019年1月深圳分部报销单 \
    --BatchRemark 转账说明 \
    --TotalAmount 50000 \
    --TotalNum 1 \
    --TransferDetails.0.MerchantDetailNo x23zy545Bd5436 \
    --TransferDetails.0.TransferAmount 50000 \
    --TransferDetails.0.TransferRemark 2020年4月报销 \
    --TransferDetails.0.OpenId o-MYE42l80oelYMDE34nYD456Xoy \
    --TransferDetails.0.UserName 张三
```

Output: 
```
{
    "Response": {
        "MerchantBatchNo": "6695169909762424836",
        "BatchId": "1030001016801203285292020080100005190005",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

**Example 2: 发起批量转账错误返回示例**

发起批量转账，参数错误的情况

Input: 

```
tccli cpdp CreateTransferBatch --cli-unfold-argument  \
    --MerchantId 129284394 \
    --MerchantAppId wxf636efh567hg4356 \
    --MerchantBatchNo plfk2020042013 \
    --BatchName 2019年1月深圳分部报销单 \
    --BatchRemark 转账说明 \
    --TotalAmount 50000 \
    --TotalNum 1 \
    --TransferDetails.0.MerchantDetailNo x23zy545Bd5436 \
    --TransferDetails.0.TransferAmount 20000 \
    --TransferDetails.0.TransferRemark 2020年4月报销 \
    --TransferDetails.0.OpenId o-MYE42l80oelYMDE34nYD456Xoy \
    --TransferDetails.0.UserName 张三
```

Output: 
```
{
    "Response": {
        "RequestId": "41f4cac5-8a76-47ea-ae6e-913855f0df5c"
    }
}
```

