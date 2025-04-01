**Example 1: 创建增量迁移策略**

创建增量迁移策略

Input: 

```
tccli vod CreateIncrementalMigrationStrategy --cli-unfold-argument  \
    --SubAppId 1020304056 \
    --BucketId bucketid1 \
    --StrategyName strategy_name \
    --OriginType HTTP \
    --HttpOriginConfig.OriginInfo.EndpointInfo.Endpoint example.com:8080 \
    --HttpOriginConfig.OriginParameter.HttpHeaderInfo.HeaderFollowMode FOLLOW_ALL
```

Output: 
```
{
    "Response": {
        "RequestId": "83bb5dcc-reqid-demo-a891-9ceeed3bb173",
        "StrategyId": "im-123-demoid"
    }
}
```

