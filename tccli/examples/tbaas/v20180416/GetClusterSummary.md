**Example 1: GetClusterSummary**



Input: 

```
tccli tbaas GetClusterSummary --cli-unfold-argument  \
    --Module cluster_mng \
    --Operation cluster_summary \
    --ClusterId 251005746bc0f03q8u93j \
    --GroupId 0 \
    --GroupName liulanOrg
```

Output: 
```
{
    "Response": {
        "ClientCertCount": 2,
        "JoinChannelCount": 1,
        "MyChaincodeCount": 1,
        "MyChannelCount": 1,
        "MyGroupCount": 1,
        "MyPeerCount": 2,
        "PeerCertCount": 2,
        "RecentChaincodeCount": 1,
        "RequestId": "8646a1d8-bae3-4b41-8732-06b8c004eaa5",
        "TlsCertCount": 4,
        "TotalCertCount": 8,
        "TotalChaincodeCount": 1,
        "TotalChannelCount": 1,
        "TotalGroupCount": 1,
        "TotalPeerCount": 2
    }
}
```

