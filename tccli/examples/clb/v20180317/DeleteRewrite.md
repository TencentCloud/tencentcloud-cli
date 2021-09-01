**Example 1: 批量删除多对重定向关系**



Input: 

```
tccli clb DeleteRewrite --cli-unfold-argument  \
    --LoadBalancerId lb-r6nx1iby \
    --SourceListenerId lbl-cy6akv52 \
    --TargetListenerId lbl-g14o899k \
    --RewriteInfos.0.SourceLocationId loc-2jkimjn0 \
    --RewriteInfos.0.TargetLocationId loc-bmsddozm \
    --RewriteInfos.1.SourceLocationId loc-eu15yo84 \
    --RewriteInfos.1.TargetLocationId loc-bmsddozm
```

Output: 
```
{
    "Response": {
        "RequestId": "4fcf51ca-fde7-4064-beff-cc46dd151f73"
    }
}
```

