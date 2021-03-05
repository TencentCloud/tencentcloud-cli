**Example 1: 获取用户绑定的专享集群列表**



Input: 

```
tccli tdmq DescribeBindClusters --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ClusterSet": [
            {
                "ClusterName": "xxx"
            }
        ],
        "RequestId": "32a34a4c-58a8-445f-80ff-7152399b18f7"
    }
}
```

