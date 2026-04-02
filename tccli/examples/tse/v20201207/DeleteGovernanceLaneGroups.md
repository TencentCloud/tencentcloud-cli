**Example 1: 删除泳道组**



Input: 

```
tccli tse DeleteGovernanceLaneGroups --cli-unfold-argument  \
    --InstanceId ins-17dhh123 \
    --LaneGroups.0.Name sct \
    --LaneGroups.0.ID db33e953bfd7467abe34f40f23ca1ada
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "db33e953bfd7467abe34f40f23ca1ada"
    }
}
```

