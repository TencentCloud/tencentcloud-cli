**Example 1: 设置自动续费**



Input: 

```
tccli igtm ModifyPackageAutoRenew --cli-unfold-argument  \
    --ResourceId task-muqyohplgqld \
    --AutoRenew 1
```

Output: 
```
{
    "Response": {
        "RequestId": "e7f146a6-53b7-4647-80fe-cfc3df35e3ef",
        "ResourceIds": [
            "task-muqyohplgqld"
        ]
    }
}
```

