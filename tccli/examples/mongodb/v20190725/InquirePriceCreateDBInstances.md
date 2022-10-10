**Example 1: 查询新购数据库实例价格**



Input: 

```
tccli mongodb InquirePriceCreateDBInstances --cli-unfold-argument  \
    --GoodsNum 2 \
    --Zone ap-guangzhou-4 \
    --Memory 4 \
    --Period 1 \
    --ClusterType REPLSET \
    --Volume 100 \
    --NodeNum 3 \
    --ReplicateSetNum 1 \
    --MachineCode HIO10G \
    --MongoVersion MONGO_36_WT
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

