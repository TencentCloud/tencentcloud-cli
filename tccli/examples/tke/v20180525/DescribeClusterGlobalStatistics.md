**Example 1: 获取各地域集群数量统计**

获取各地域集群数量统计

Input: 

```
tccli tke DescribeClusterGlobalStatistics --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ClusterStatisticsSet": [
            {
                "Region": "ap-guangzhou",
                "TotalCount": 4,
                "Error": ""
            }
        ],
        "RequestId": "24564577-a642-4164-8752-4668d4ca8886"
    }
}
```

