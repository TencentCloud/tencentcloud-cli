**Example 1: 删除增量迁移策略**

删除增量迁移策略

Input: 

```
tccli vod DeleteIncrementalMigrationStrategy --cli-unfold-argument  \
    --SubAppId 1020304056 \
    --BucketId bucketid2 \
    --StrategyId im-123-demoid
```

Output: 
```
{
    "Response": {
        "RequestId": "397d92f2-demo-reqid-bfbd-c2f7e3569c9d"
    }
}
```

