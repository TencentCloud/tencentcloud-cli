**Example 1: DescribeAssetSuperNodeList**

查询超级节点列表

Input: 

```
tccli tcss DescribeAssetSuperNodeList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "NodeID": "dc56fda9-58c8-4c4f-9e8c-b7296836c1fe",
                "NodeName": "web-node1",
                "ClusterName": "web-cluster",
                "ClusterID": "cls-sdfsdf",
                "Status": "Running",
                "SubNetID": "subnet-sdfsd",
                "SubNetName": "web-node1",
                "SubNetCidr": "10.0.1.0/24",
                "ZoneID": "ap-guangzhou-6",
                "Zone": "ap-guangzhou",
                "CreateTime": "2024-10-30 10:40:41",
                "RelatePodCount": 1,
                "RelateContainerCount": 1,
                "AgentStatus": "UNINSTALL",
                "NodeUniqueID": "392f05bd-bf86-4911-8cf9-b8c2afd445cd4",
                "ClusterAccessedStatus": "AccessedDefended",
                "ChargeCoresCnt": 1,
                "DefendStatus": "Defended"
            }
        ],
        "TotalCount": 1,
        "RequestId": "c826b9fa-68b5-4603-bf25-a5eb9b65c768"
    }
}
```

