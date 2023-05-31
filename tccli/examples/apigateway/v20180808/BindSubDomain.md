**Example 1: 绑定自定义域名**

绑定自定义域名

Input: 

```
tccli apigateway BindSubDomain --cli-unfold-argument  \
    --ServiceId service-1w9ekbwo \
    --NetType OUTER \
    --SubDomain xxx.com \
    --NetSubDomain service-1w9ekbwo-1259027407.gz.apigw.tencentcs.com \
    --IsDefaultMapping TRUE \
    --PathMappingSet.0.Environment release \
    --PathMappingSet.0.Path / \
    --Protocol http \
    --IsForcedHttps TRUE
```

Output: 
```
{
    "Response": {
        "RequestId": "6e00553a-8158-4f70-ad43-e1b046af1502"
    }
}
```

