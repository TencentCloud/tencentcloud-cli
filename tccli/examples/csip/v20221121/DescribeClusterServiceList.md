**Example 1: 调用示例**



Input: 

```
tccli csip DescribeClusterServiceList --cli-unfold-argument  \
    --ClusterAssetId 86693c5bf9e9fbdce993d557b1038fd8 \
    --MemberId mem-a6df317cb6a8c424 \
    --ClusterCaMD5 ddfda86**********************ddc \
    --PodUniqueID 10e4***********************71184
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AppID": 260083796,
                "AssetId": "e17e1498e7e929c33c4b1aa9201535a9",
                "CreateTime": "2026-02-24T21:24:02Z",
                "Name": "tke-eni-ipamd",
                "Namespace": "kube-system",
                "SelectorLabel": [
                    {
                        "TagKey": "k8s-app",
                        "TagValue": "tke-eni-ipamd"
                    }
                ]
            }
        ],
        "TotalCount": 8,
        "RequestId": "1c122180-cfe9-4bb4-be0a-de61eb030edb"
    }
}
```

