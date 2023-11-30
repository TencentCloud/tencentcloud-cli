**Example 1: 创建一个别名**



Input: 

```
tccli scf CreateAlias --cli-unfold-argument  \
    --Name TestAlias \
    --Namespace default \
    --FunctionName TestFunction \
    --FunctionVersion $LATEST \
    --RoutingConfig.AdditionalVersionWeights.0.Version 1 \
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

