**Example 1: Updating alias configuration**



Input: 

```
tccli scf UpdateAlias --cli-unfold-argument  \
    --Name <AliasName>\
    --Namespace <Namespace>\
    --FunctionName <FunctionName>\
    --FunctionVersion <FunctionVersion>\
    --RoutingConfig.AdditionalVersionWeights.0.Version <OtherVersion>\
    --RoutingConfig.AdditionalVersionWeights.0.Weight <Weight>
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

