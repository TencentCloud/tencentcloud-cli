**Example 1: 集群信息列表**

查询集群列表，用于获取集群列表

Input: 

```
tccli tke DescribeEKSClusters --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Clusters": [
            {
                "ClusterId": "cls-xxxxxxx",
                "ClusterName": "集群AA",
                "K8SVersion": "1.10.5",
                "VpcId": "vpc-xxxxx",
                "SubnetIds": [
                    "subnet-xxxxx"
                ],
                "Status": "running",
                "CreatedTime": "2019-08-16T04:31:26Z"
            }
        ],
        "RequestId": "a1be36f0-1aa4-4af2-a289-da021bcef89f"
    }
}
```

