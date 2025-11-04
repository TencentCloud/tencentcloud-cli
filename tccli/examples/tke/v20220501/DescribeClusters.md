**Example 1: 查询集群列表**

查询集群列表

Input: 

```
tccli tke DescribeClusters --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Clusters": [
            {
                "ClusterDescription": "",
                "ClusterId": "cls-padxxv08",
                "ClusterLevel": "L5",
                "ClusterName": "勿删 feeli-1.16.7-1",
                "ClusterStatus": "Running",
                "ClusterType": "EDGE_CLUSTER",
                "ClusterVersion": "1.16.7",
                "CreatedTime": "2022-11-09T17:12:15Z",
                "TagSpecification": []
            }
        ],
        "Errors": [],
        "RequestId": "55777e90-1af7-4108-abd5-fca0638a7bb6",
        "TotalCount": 1
    }
}
```

