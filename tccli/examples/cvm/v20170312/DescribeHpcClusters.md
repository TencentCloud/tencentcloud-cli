**Example 1: 查询高性能集群信息**

查询高性能集群信息

Input: 

```
tccli cvm DescribeHpcClusters --cli-unfold-argument  \
    --Zone ap-guangzhou-3 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "HpcClusterSet": [
            {
                "HpcClusterId": "hpc-dc4gcarp",
                "Name": "test_33311",
                "Remark": "remark 1",
                "CvmQuotaTotal": 50,
                "Zone": "ap-guangzhou-3",
                "CurrentNum": 0,
                "InstanceIds": [],
                "CreateTime": "2020-06-02T07:55:05Z"
            },
            {
                "HpcClusterId": "hpc-p64fdfa9",
                "Name": "test_333333",
                "Remark": "remark 2",
                "CvmQuotaTotal": 50,
                "Zone": "ap-guangzhou-3",
                "CurrentNum": 0,
                "InstanceIds": [],
                "CreateTime": "2020-06-02T07:51:58Z"
            }
        ],
        "TotalCount": 2,
        "RequestId": "5834f1a5-cd9c-449d-acba-df1803a8583e"
    }
}
```

