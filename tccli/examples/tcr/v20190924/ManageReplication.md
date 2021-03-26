**Example 1: 管理实例同步规则**



Input: 

```
tccli tcr ManageReplication --cli-unfold-argument  \
    --SourceRegistryId tcr-xxx \
    --DestinationRegistryId tcr-yyy \
    --DestinationRegionId 9 \
    --Rule.Override true \
    --Rule.DestNamespace test \
    --Rule.Name test \
    --Rule.Filters.0.Type tag \
    --Rule.Filters.0.Value test
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

