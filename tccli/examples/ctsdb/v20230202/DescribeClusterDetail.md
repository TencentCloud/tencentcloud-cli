**Example 1: 查询成功**



Input: 

```
tccli ctsdb DescribeClusterDetail --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Cluster": {
            "AccountID": "Tnog5Q==",
            "AppID": 251223625,
            "ClusterID": "ctsdbi-p39mhwnt",
            "Components": [
                {
                    "Cpu": 2,
                    "Disk": 0,
                    "ID": 332,
                    "InstanceID": "ctsdbi-p39mhwnt",
                    "Memory": 8,
                    "Name": "",
                    "Networks": [
                        {
                            "Port": 8086,
                            "SubnetId": "subnet-qdkd825s",
                            "VIP": "10.200.18.28",
                            "VpcId": "vpc-ncirw84v"
                        }
                    ],
                    "Replicas": 3,
                    "Shards": 1,
                    "State": 0,
                    "Type": "gateway"
                }
            ],
            "CreatedAt": "2025-12-23T03:26:51Z",
            "ExpiredAt": null,
            "IsolatedAt": null,
            "Name": "jacob-test",
            "Networks": [],
            "Region": "ap-beijing",
            "RenewFlag": 0,
            "Security": [],
            "ShutdownAt": null,
            "Status": 0,
            "Tags": [],
            "Type": 1,
            "UpdatedAt": "2025-12-23T03:30:29Z"
        },
        "RequestId": "41350874-99a8-41f5-a1ca-b254ba36ab09"
    }
}
```

