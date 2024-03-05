**Example 1: 查询集群列表**



Input: 

```
tccli clb DescribeExclusiveClusters --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ClusterSet": [
            {
                "ClustersVersion": "",
                "ClusterId": "tgw-12345678",
                "ClusterName": "tgw_cluster",
                "ClusterType": "TGW",
                "ClusterTag": null,
                "Zone": "ap-guangzhou-1",
                "Network": "Public",
                "Isp": "CMCC",
                "MaxConn": 12,
                "MaxInFlow": 0,
                "MaxInPkg": 0,
                "MaxOutFlow": 0,
                "MaxOutPkg": 0,
                "MaxNewConn": 0,
                "HTTPMaxNewConn": 0,
                "HTTPSMaxNewConn": 0,
                "HTTPQps": 0,
                "HTTPSQps": 0,
                "ClustersZone": {
                    "MasterZone": [
                        "ap-hongkong-1"
                    ],
                    "SlaveZone": [
                        "ap-hongkong-2"
                    ]
                },
                "ResourceCount": 30,
                "IdleResourceCount": 26,
                "LoadBalanceDirectorCount": 4,
                "DisasterRecoveryType": "DISASTER-RECOVERY",
                "Egress": "abc",
                "IPVersion": "abc"
            }
        ],
        "RequestId": "49e44bf9-1357-420b-87ba-3c827209af67"
    }
}
```

