**Example 1: 创建实例同步**



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

**Example 2: 创建跨主账号实例同步**

用于创建跨主账号的实例同步

Input: 

```
tccli tcr ManageReplication --cli-unfold-argument  \
    --SourceRegistryId tcr-3498 \
    --DestinationRegistryId tcr-98676 \
    --DestinationRegionId 9 \
    --Rule.Override true \
    --Rule.DestNamespace test \
    --Rule.Name test \
    --Rule.Filters.0.Type tag \
    --Rule.Filters.0.Value test \
    --PeerReplicationOption.EnablePeerReplication true \
    --PeerReplicationOption.PeerRegistryUin 113498 \
    --PeerReplicationOption.PeerRegistryToken xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

