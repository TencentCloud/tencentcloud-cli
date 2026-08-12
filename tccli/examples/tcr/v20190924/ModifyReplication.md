**Example 1: 修改实例同步**



Input: 

```
tccli tcr ModifyReplication --cli-unfold-argument  \
    --SourceRegistryId tcr-f3ouwtzl \
    --RuleName rule1 \
    --Rule.DestNamespace nginx \
    --Rule.Override True \
    --Rule.Deletion False \
    --Rule.Filters.0.Type tag \
    --Rule.Filters.0.Value v1 \
    --Rule.Enabled False
```

Output: 
```
{
    "Response": {
        "RequestId": "709ebe2a-0a47-4fb4-a559-6a3cd329bd0e"
    }
}
```

