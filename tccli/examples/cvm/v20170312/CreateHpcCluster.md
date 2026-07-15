**Example 1: 创建高性能计算集群**

创建高性能计算集群。

Input: 

```
tccli cvm CreateHpcCluster --cli-unfold-argument  \
    --Zone ap-guangzhou-3 \
    --Name MyHpcCluster \
    --Remark my cluster \
    --TagSpecification.0.ResourceType hpc \
    --TagSpecification.0.Tags.0.Key tag_key \
    --TagSpecification.0.Tags.0.Value tag_value
```

Output: 
```
{
    "Response": {
        "HpcClusterSet": [
            {
                "HpcClusterId": "hpc-0eixl8xv",
                "Name": "MyHpcCluster",
                "Remark": "my cluster",
                "HpcClusterType": "STANDARD",
                "HpcClusterBusinessId": "cluster-ax457mhr",
                "HpcClusterNetMode": 30,
                "Zone": "ap-guangzhou-3",
                "InstanceIds": [],
                "CvmQuotaTotal": 50,
                "CurrentNum": 0,
                "CreateTime": "2020-06-02T07:36:04Z",
                "Tags": [
                    {
                        "Key": "tag_key",
                        "Value": "tag_value"
                    }
                ]
            }
        ],
        "RequestId": "5834f1a5-cd9c-449d-acba-df1803a8583e"
    }
}
```

