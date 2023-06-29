**Example 1: 查询集群**



Input: 

```
tccli tdcpg DescribeClusters --cli-unfold-argument  \
    --OrderBy CreateTime \
    --OrderByType DESC \
    --PageNumber 1 \
    --Filters.0.Values tdcpg-77iesdqa \
    --Filters.0.Name ClusterId \
    --Filters.0.ExactMatch True \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "ClusterSet": [
            {
                "AutoRenewFlag": 0,
                "ClusterId": "tdcpg-77iesdqa",
                "ClusterName": "tdcpg-77iesdqa",
                "CreateTime": "2021-12-08T19:50:55+08:00",
                "DBCharset": "UTF8",
                "DBMajorVersion": "10",
                "DBVersion": "10.17",
                "DBKernelVersion": "v10.17_r1.4",
                "EndpointSet": [
                    {
                        "ClusterId": "tdcpg-77iesdqa",
                        "EndpointId": "tdcpg-ep-6c6xs52r",
                        "EndpointName": "tdcpg-ep-6c6xs52r",
                        "EndpointType": "RW",
                        "PrivateIp": "10.0.64.20",
                        "PrivatePort": 5432,
                        "SubnetId": "subnet-5wnhtsmw",
                        "VpcId": "vpc-l0ee2prd",
                        "WanDomain": "",
                        "WanIp": "",
                        "WanPort": 0
                    },
                    {
                        "ClusterId": "tdcpg-77iesdqa",
                        "EndpointId": "tdcpg-ep-ffscxj6f",
                        "EndpointName": "tdcpg-ep-ffscxj6f",
                        "EndpointType": "RO",
                        "PrivateIp": "10.0.64.24",
                        "PrivatePort": 5432,
                        "SubnetId": "subnet-5wnhtsmw",
                        "VpcId": "vpc-l0ee2prd",
                        "WanDomain": "",
                        "WanIp": "",
                        "WanPort": 0
                    }
                ],
                "InstanceCount": 2,
                "PayMode": "PREPAID",
                "PayPeriodEndTime": "2022-01-08T19:50:54+08:00",
                "ProjectId": 0,
                "Region": "ap-guangzhou",
                "Status": "running",
                "StatusDesc": "运行中",
                "StorageLimit": 2048,
                "StorageUsed": 0.14,
                "Zone": "ap-guangzhou-3"
            }
        ],
        "RequestId": "c644d6ec-0743-4ba3-916a-e30c5a00ada1",
        "TotalCount": 1
    }
}
```

