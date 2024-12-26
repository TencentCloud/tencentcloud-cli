**Example 1: GetClusterSummary**



Input: 

```
tccli tbaas GetClusterSummary --cli-unfold-argument  \
    --Module cluster_mng \
    --Operation cluster_summary \
    --ClusterId 251005746bc0f03q8u93j \
    --GroupId 12 \
    --GroupName liulanOrg
```

Output: 
```
{
    "Response": {
        "MyPeerCount": 1,
        "ClientCertCount": 1,
        "TotalChaincodeCount": 1,
        "TotalChannelCount": 1,
        "TlsCertCount": 1,
        "OrderCount": 1,
        "RecentChaincodeCount": 1,
        "PeerCertCount": 1,
        "MyChaincodeCount": 1,
        "RequestId": "aeae4ed4-a4ce-4ffd-9826-1aae7669bb7c",
        "TotalCertCount": 1,
        "MyGroupCount": 1,
        "MyChannelCount": 1,
        "TotalGroupCount": 1,
        "JoinChannelCount": 1,
        "TotalPeerCount": 1
    }
}
```

