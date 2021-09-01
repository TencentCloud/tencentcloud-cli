**Example 1: GetClusterListForUser**



Input: 

```
tccli tbaas GetClusterListForUser --cli-unfold-argument  \
    --Module cluster_mng \
    --Operation cluster_list_for_user \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ClusterList": [
            {
                "ClusterId": "251005746bcku93u4ke0g",
                "ClusterName": "test",
                "GroupList": [
                    {
                        "GroupName": "qtaGZorg",
                        "GroupMSPId": "qtaGZorgMSP-bcku93u4ke0g"
                    }
                ]
            }
        ],
        "RequestId": "7c0c2650-a696-4427-bffc-67c2268d3eb0"
    }
}
```

