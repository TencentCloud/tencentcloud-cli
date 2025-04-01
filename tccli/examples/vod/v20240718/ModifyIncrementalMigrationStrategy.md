**Example 1: 修改增量迁移策略名称**

修改增量迁移策略名称

Input: 

```
tccli vod ModifyIncrementalMigrationStrategy --cli-unfold-argument  \
    --SubAppId 123456789 \
    --BucketId bucketid2 \
    --StrategyId im-123-demoid \
    --StrategyName demo-modify
```

Output: 
```
{
    "Response": {
        "RequestId": "94a26124-reqid-demo-ad0f-e8458e187f02"
    }
}
```

**Example 2: 修改增量迁移策略内容**

修改增量迁移策略回源类型及 HTTP 回源配置信息

Input: 

```
tccli vod ModifyIncrementalMigrationStrategy --cli-unfold-argument  \
    --SubAppId 123456789 \
    --BucketId bucketid2 \
    --StrategyId im-123-demoid \
    --StrategyName  \
    --OriginType HTTP \
    --HttpOriginConfig.OriginInfo.EndpointInfo.Endpoint example2.com \
    --HttpOriginConfig.OriginParameter.HttpHeaderInfo.HeaderFollowMode IGNORE_ALL \
    --HttpOriginConfig.OriginParameter.HttpHeaderInfo.NewHttpHeaderSet.0.Key host \
    --HttpOriginConfig.OriginParameter.HttpHeaderInfo.NewHttpHeaderSet.0.Value demo2.com \
    --HttpOriginConfig.OriginParameter.Protocol FOLLOW \
    --HttpOriginConfig.OriginParameter.QueryStringFollowMode FOLLOW \
    --HttpOriginConfig.OriginParameter.HttpRedirectCode 302 \
    --HttpOriginConfig.OriginParameter.OriginRedirectionFollowMode IGNORE \
    --HttpOriginConfig.Mode SYNC \
    --HttpOriginConfig.OriginCondition.HttpStatusCode 404
```

Output: 
```
{
    "Response": {
        "RequestId": "300b29b9-demo-reqid-ade4-f84f176e60c3"
    }
}
```

