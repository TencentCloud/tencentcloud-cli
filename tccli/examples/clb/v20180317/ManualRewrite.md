**Example 1: 手动添加一条重定向关系**



Input: 

```
tccli clb ManualRewrite --cli-unfold-argument  \
    --LoadBalancerId lb-r6nx1iby \
    --SourceListenerId lbl-cy6akv52 \
    --TargetListenerId lbl-cy6ak123 \
    --RewriteInfos.0.SourceLocationId loc-2jkimjn0 \
    --RewriteInfos.0.TargetLocationId loc-eu15yo84
```

Output: 
```
{
    "Response": {
        "RequestId": "fc0ed756-c311-41c8-a22d-64f88a346951"
    }
}
```

