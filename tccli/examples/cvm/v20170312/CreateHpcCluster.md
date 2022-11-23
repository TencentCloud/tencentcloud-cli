**Example 1: 创建高性能计算集群**

创建高性能计算集群。

Input: 

```
tccli cvm CreateHpcCluster --cli-unfold-argument  \
    --Name test_cluster \
    --Remark 'my cluster' \
    --Zone ap-guangzhou-3
```

Output: 
```
{
    "Response": {
        "HpcClusterSet": [
            {
                "HpcClusterId": "hpc-0eixl8xv",
                "Name": "test_cluster",
                "Remark": "my cluster",
                "Zone": "ap-guangzhou-3",
                "InstanceIds": [],
                "CvmQuotaTotal": 50,
                "CurrentNum": 0,
                "CreateTime": "2020-06-02T07:36:04Z"
            }
        ],
        "RequestId": "5834f1a5-cd9c-449d-acba-df1803a8583e"
    }
}
```

