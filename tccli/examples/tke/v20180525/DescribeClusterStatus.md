**Example 1: 获取集群当前状态**



Input: 

```
tccli tke DescribeClusterStatus --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ClusterStatusSet": [
            {
                "ClusterClosingNodeNum": 0,
                "ClusterAuditEnabled": true,
                "ClusterDeletionProtection": true,
                "ClusterId": "xx",
                "ClusterBMonitor": true,
                "ClusterInitNodeNum": 0,
                "ClusterState": "xx",
                "ClusterClosedNodeNum": 0,
                "ClusterInstanceState": "xx",
                "ClusterRunningNodeNum": 0,
                "ClusterFailedNodeNum": 0
            }
        ],
        "RequestId": "a1be36f0-1aa4-4af2-a289-da021bcef89f"
    }
}
```

