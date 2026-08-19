**Example 1: 查询集群节点列表**



Input: 

```
tccli csip DescribeClusterNodeList --cli-unfold-argument  \
    --MemberId mem-tencent-6f5795752f66e429 \
    --ClusterCaMD5 83d4abefaac754bfaf66cc6342421eb9
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AppID": 260083796,
                "AssetId": "",
                "ClientStatus": "OFFLINE",
                "CoresCount": 2000,
                "InstanceId": "ins-ngi794so",
                "InternalIP": "172.16.1.38",
                "NodeId": "ins-ngi794so",
                "NodeName": "as-tke-np-c63zg3iq",
                "NodeType": "WORKER",
                "PublicIP": "",
                "RunStatus": "Error",
                "Tags": [],
                "UniqueID": "de115e930d4f8c31a4c8a0a45b1bf88b"
            }
        ],
        "TotalCount": 7,
        "RequestId": "88da4e12-da90-4493-b540-3b22575bb806"
    }
}
```

