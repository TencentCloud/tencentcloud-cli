**Example 1: 调用示例**



Input: 

```
tccli csip DescribeClusterPodList --cli-unfold-argument  \
    --ClusterAssetId 86693c5bf9e9fbdce993d557b1038fd8 \
    --MemberId mem-a6df317cb6a8c424 \
    --ClusterCaMD5 4e***************************778
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AppID": 260083796,
                "AssetId": "a08a96938d70342df1a8f0c115277a07",
                "CreateTime": "2026-03-06T02:56:46Z",
                "DefendCoresCount": 100,
                "Namespace": "tcss",
                "NodeId": "",
                "NodeType": "",
                "PodIPs": [
                    "172.16.0.76"
                ],
                "PodName": "tcss-asset-66c6b4cc44-4v8vl",
                "PodUid": "d9ba13f7-e52b-4b91-8620-f4dfeeb7e9d7",
                "RunStatus": "Running",
                "WorkloadName": "tcss-asset-66c6b4cc44",
                "WorkloadType": "ReplicaSet"
            }
        ],
        "TotalCount": 10,
        "RequestId": "2a4ebe3e-bdb7-44cb-8ed4-45aa048db2ec"
    }
}
```

