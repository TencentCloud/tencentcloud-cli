**Example 1: 查询集群资源列表**



Input: 

```
tccli clb DescribeClusterResources --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "ClusterResourceSet": [
            {
                "ClusterName": "cluster-1",
                "ClusterId": "tgw-12345678",
                "Vip": "1.1.1.1",
                "LoadBalancerId": null,
                "Idle": true,
                "Isp": "BGP",
                "ClustersZone": {
                    "MasterZone": [
                        "ap-hongkong-1"
                    ],
                    "SlaveZone": [
                        "ap-hongkong-2"
                    ]
                }
            },
            {
                "ClusterName": "cluster-1",
                "ClusterId": "tgw-12345678",
                "Vip": "1.1.1.2",
                "LoadBalancerId": "lb-12345678",
                "Idle": false,
                "Isp": "BGP",
                "ClustersZone": {
                    "MasterZone": [
                        "ap-hongkong-1"
                    ],
                    "SlaveZone": [
                        "ap-hongkong-2"
                    ]
                }
            }
        ],
        "RequestId": "49e44bf9-1357-420b-87ba-3c827209af67"
    }
}
```

