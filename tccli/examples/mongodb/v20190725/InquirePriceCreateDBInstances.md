**Example 1: 查询新购数据库实例价格**



Input: 

```
tccli mongodb InquirePriceCreateDBInstances --cli-unfold-argument  \
    --Zone ap-guangzhou-4 \
    --NodeNum 3 \
    --Memory 4 \
    --Volume 100 \
    --MongoVersion MONGO_36_WT \
    --MachineCode HIO10G \
    --GoodsNum 2 \
    --Period 1 \
    --ClusterType REPLSET \
    --ReplicateSetNum 1
```

Output: 
```
{
    "Response": {
        "Price": {
            "DiscountPrice": 1340,
            "OriginalPrice": 1340,
            "UnitPrice": 670
        },
        "RequestId": "fb8b4646-389d-44cc-ab8c-98c081cbdad3"
    }
}
```

