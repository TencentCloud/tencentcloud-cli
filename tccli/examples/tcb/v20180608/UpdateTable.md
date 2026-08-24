**Example 1: 给集合 testxishu 增加稀疏索引**



Input: 

```
tccli tcb UpdateTable --cli-unfold-argument  \
    --TableName testxishu \
    --CreateIndexes.0.IndexName xishu2 \
    --CreateIndexes.0.MgoKeySchema.MgoIndexKeys.0.Name age \
    --CreateIndexes.0.MgoKeySchema.MgoIndexKeys.0.Direction 1 \
    --CreateIndexes.0.MgoKeySchema.MgoIsUnique True \
    --CreateIndexes.0.MgoKeySchema.MgoIsSparse False \
    --CreateIndexes.0.MgoKeySchema.PartialFilterExpression {"age":{"$gt":18}} \
    --EnvId mike-qiye-mongo2-d4eiui5538d249d
```

Output: 
```
{
    "Response": {
        "RequestId": "e942c859-c64a-4753-983d-1a1747a45e5f"
    }
}
```

**Example 2: 给集合 demo_items 增加索引**



Input: 

```
tccli tcb UpdateTable --cli-unfold-argument  \
    --TableName demo_items \
    --CreateIndexes.0.IndexName xishu2 \
    --CreateIndexes.0.MgoKeySchema.MgoIndexKeys.0.Name age \
    --CreateIndexes.0.MgoKeySchema.MgoIndexKeys.0.Direction 1 \
    --CreateIndexes.0.MgoKeySchema.MgoIsUnique False \
    --EnvId mike-qiye-mongo2-d4eiui5538d249d
```

Output: 
```
{
    "Response": {
        "RequestId": "f5a74bae-6743-4079-8114-137582a94c18"
    }
}
```

