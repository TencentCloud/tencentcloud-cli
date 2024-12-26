**Example 1: 更新Api分组**



Input: 

```
tccli tsf UpdateApiGroup --cli-unfold-argument  \
    --GroupId grp-notmqbpe \
    --GroupName grp_app \
    --Description This is desc \
    --AuthType none \
    --GroupContext /grp_app \
    --NamespaceNameKey TSF-NamespaceName \
    --ServiceNameKey TSF-ServiceName \
    --NamespaceNameKeyPosition path \
    --ServiceNameKeyPosition path
```

Output: 
```
{
    "Response": {
        "RequestId": "9bcb4936-f3e5-4fdc-acd8-71fd041429e8",
        "Result": true
    }
}
```

