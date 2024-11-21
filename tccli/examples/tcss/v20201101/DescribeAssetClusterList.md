**Example 1: 查询集群列表**



Input: 

```
tccli tcss DescribeAssetClusterList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "BindRuleName": "piper",
                "ClusterID": "cls-abhq0j4o",
                "ClusterName": "bx_test_tmp",
                "ClusterType": "INDEPENDENT_CLUSTER",
                "ClusterVersion": "",
                "CpuLimit": 0,
                "MemLimit": 0,
                "Status": "CSR_RUNNING"
            }
        ],
        "RequestId": "bb39b643-b0e1-4c79-b006-7d62083227a8",
        "TotalCount": 15
    }
}
```

