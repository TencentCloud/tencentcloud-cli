**Example 1: 查询联通性检测主机列表**



Input: 

```
tccli csip DescribeCheckConnectivityHostList --cli-unfold-argument  \
    --MemberId mem-12e1se11
```

Output: 
```
{
    "Response": {
        "HostList": [
            {
                "ClusterId": "cls-law7jgc6",
                "ClusterName": "openclaw-Test",
                "DockerFileSystemDriver": "overlay",
                "DockerVersion": "v1.6.9-tke.8",
                "HostId": "d2fc28e6-6513-4989-8614-9f84ce628da2",
                "HostIp": "172.16.0.199",
                "HostName": "cls-law7jgc6_np-3qr9l30o-gf957",
                "HostRegion": "ap-guangzhou",
                "HostRegionId": 1,
                "InstanceId": "eks-8z0pj6qn",
                "IsContainerd": true,
                "MachineType": "EKS-NATIVE",
                "Project": {
                    "ProjectId": 0,
                    "ProjectName": "0"
                },
                "PublicIp": "",
                "Status": "ONLINE",
                "Tags": [],
                "Uuid": "d2fc28e6-6513-4989-8614-9f84ce628da2"
            }
        ],
        "TotalCount": 18,
        "RequestId": "ad69f33f-cdde-42de-947a-26c3f7a214e5"
    }
}
```

