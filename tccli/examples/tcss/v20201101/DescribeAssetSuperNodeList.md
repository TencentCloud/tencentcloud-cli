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
                "NodeID": "abc",
                "NodeName": "abc",
                "ClusterName": "abc",
                "ClusterID": "abc",
                "Status": "abc",
                "SubNetID": "abc",
                "SubNetName": "abc",
                "SubNetCidr": "abc",
                "ZoneID": "abc",
                "Zone": "abc",
                "CreateTime": "abc",
                "RelatePodCount": 1,
                "RelateContainerCount": 1,
                "AgentStatus": "abc",
                "NodeUniqueID": "abc",
                "ClusterAccessedStatus": "abc",
                "ChargeCoresCnt": 1,
                "DefendStatus": "abc"
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

