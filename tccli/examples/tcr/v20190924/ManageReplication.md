**Example 1: 创建实例同步**



Input: 

```
tccli tcr ManageReplication --cli-unfold-argument  \
    --SourceRegistryId tcr-dg284imq \
    --DestinationRegistryId tcr-7o4xeay9 \
    --Rule.Name rule2 \
    --Rule.DestNamespace ns2 \
    --Rule.Override False \
    --Rule.Filters.0.Type name \
    --Rule.Filters.0.Value ns2/** \
    --Description gz-sync2bj \
    --DestinationRegionId 8
```

Output: 
```
{
    "Response": {
        "RequestId": "3114c283-39df-4966-a181-9e906a3bed2f"
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

