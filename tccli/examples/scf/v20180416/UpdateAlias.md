**Example 1: 更新别名的配置**



Input: 

```
tccli scf UpdateAlias --cli-unfold-argument  \
    --Name abcAlias \
    --Namespace default \
    --FunctionName abc \
    --FunctionVersion 1 \
    --RoutingConfig.AdditionalVersionWeights.0.Version 2 \
    --RoutingConfig.AdditionalVersionWeights.0.Weight 0.5
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

