**Example 1: 创建索引**



Input: 

```
tccli tcb UpdateTable --cli-unfold-argument  \
    --TableName adise \
    --Tag tnt-jas2zvl90 \
    --CreateIndexes.0.IndexName test-index \
    --CreateIndexes.0.MgoKeySchema.MgoIndexKeys.0.Name adise \
    --CreateIndexes.0.MgoKeySchema.MgoIndexKeys.0.Direction 1 \
    --CreateIndexes.0.MgoKeySchema.MgoIsUnique false
```

Output: 
```
{
    "Response": {
        "RequestId": "C563943B-3BEA-FE92-29FE-591EAEB7871F"
    }
}
```

**Example 2: 删除索引**



Input: 

```
tccli tcb UpdateTable --cli-unfold-argument  \
    --TableName adise \
    --Tag tnt-jas2zvl90 \
    --DropIndexes.0.IndexName testIndex
```

Output: 
```
{
    "Response": {
        "RequestId": "C563943B-3BEA-FE92-29FE-591EAEB7871F"
    }
}
```

**Example 3: 创建索引-使用MongoDB连接器**



Input: 

```
tccli tcb UpdateTable --cli-unfold-argument  \
    --TableName test2 \
    --CreateIndexes.0.IndexName adise \
    --CreateIndexes.0.MgoKeySchema.MgoIndexKeys.0.Name adise \
    --CreateIndexes.0.MgoKeySchema.MgoIndexKeys.0.Direction 1 \
    --EnvId lowcode-1g1ac0pjd4eca700 \
    --MongoConnector.InstanceId luke_test2 \
    --MongoConnector.DatabaseName adise
```

Output: 
```
{
    "Response": {
        "RequestId": "5811a2a8-a892-4600-a7dc-96bf1c4b28ab"
    }
}
```

