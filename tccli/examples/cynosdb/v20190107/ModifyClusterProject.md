**Example 1: 修改集群项目ID**



Input: 

```
tccli cynosdb ModifyClusterProject --cli-unfold-argument  \
    --ClusterIdSet cynosdbpg-1xcycbu8 \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "117811",
        "AffectedClusterIdSet": [
            "cynosdbpg-1xcycbu8"
        ]
    }
}
```

