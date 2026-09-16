**Example 1: 创建公网实例**



Input: 

```
tccli edgezone CreatePublicNetworkInstance --cli-unfold-argument  \
    --ZoneId ap-guangzhou-7 \
    --NetworkInstanceName e2e-real-static-pub \
    --Line CT \
    --RouteMode static
```

Output: 
```
{
    "Response": {
        "NetworkInstanceId": "epn-efcc33f1",
        "RequestId": "2fecac51-e082-4e03-86cf-548369a3f8f2"
    }
}
```

