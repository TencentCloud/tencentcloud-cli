**Example 1: 查询 DB Cluster 集群列表**

按标签筛选

Input: 

```
tccli dbdc DescribeDBCustomClusters --cli-unfold-argument  \
    --Tags.0.Key DBCustomCluster \
    --Tags.0.Value PRE-CLUSTER \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "ClusterSet": [
            {
                "ClusterDescription": "",
                "ClusterId": "dbcc-nmtmsew8",
                "ClusterLevel": "L500",
                "ClusterName": "DBCustomPRE",
                "ClusterNodeNum": 0,
                "ClusterStatus": "Running",
                "ClusterVersion": "1.32.2",
                "CreatedTime": "2026-06-06T11:05:40Z",
                "Region": "ap-shanghai",
                "Tags": [
                    {
                        "Key": "DBCustomCluster",
                        "Value": "PRE-CLUSTER"
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "b5156a5a-122f-4d42-8322-06237ee54131"
    }
}
```

