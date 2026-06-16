**Example 1: 查询 DB Custom 集群详情**



Input: 

```
tccli dbdc DescribeDBCustomClusterDetail --cli-unfold-argument  \
    --ClusterId dbcc-jnfqi1b9
```

Output: 
```
{
    "Response": {
        "ApiServerNetwork": {
            "SubnetId": "subnet-clk8il4i",
            "VpcId": "vpc-evvog2gd"
        },
        "ClusterDescription": "该集群用于测试集群购买流程",
        "ClusterId": "dbcc-jnfqi1b9",
        "ClusterLevel": "L5",
        "ClusterName": "测试 DB Custom 集群",
        "ClusterNodeNum": 1,
        "ClusterStatus": "Running",
        "ClusterVersion": "1.34.1",
        "ContainerNetwork": {
            "SubnetIds": [
                "subnet-clk8il4i"
            ],
            "VpcId": "vpc-evvog2gd"
        },
        "CreatedTime": "2026-06-01T15:08:04Z",
        "Region": "ap-shanghai",
        "Tags": [
            {
                "Key": "测试集群TagKey",
                "Value": "测试集群TagValue"
            }
        ],
        "RequestId": "969a02eb-0755-4162-a7ba-a6947a3d5628"
    }
}
```

