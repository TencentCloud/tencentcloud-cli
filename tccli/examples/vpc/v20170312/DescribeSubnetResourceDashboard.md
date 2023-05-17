**Example 1: 查看Subnet资源信息**

查看Subnet资源信息

Input: 

```
tccli vpc DescribeSubnetResourceDashboard --cli-unfold-argument  \
    --SubnetIds subnet-12345678
```

Output: 
```
{
    "Response": {
        "ResourceStatisticsSet": [
            {
                "VpcId": "vpc-12345678",
                "SubnetId": "subnet-12345678",
                "Ip": 14,
                "ResourceStatisticsItemSet": [
                    {
                        "ResourceType": "NetworkDetect",
                        "ResourceName": "NetworkDetect",
                        "ResourceCount": 1
                    },
                    {
                        "ResourceType": "LoadBanlancer",
                        "ResourceName": "LoadBanlancer",
                        "ResourceCount": 2
                    },
                    {
                        "ResourceType": "MySQL",
                        "ResourceName": "MySQL",
                        "ResourceCount": 1
                    },
                    {
                        "ResourceType": "Memcached",
                        "ResourceName": "Memcached",
                        "ResourceCount": 1
                    },
                    {
                        "ResourceType": "CTSDB",
                        "ResourceName": "CTSDB",
                        "ResourceCount": 0
                    },
                    {
                        "ResourceType": "TDSQL",
                        "ResourceName": "TDSQL",
                        "ResourceCount": 0
                    },
                    {
                        "ResourceType": "SQL Server",
                        "ResourceName": "SQL Server",
                        "ResourceCount": 0
                    },
                    {
                        "ResourceType": "PostgreSQL",
                        "ResourceName": "PostgreSQL",
                        "ResourceCount": 0
                    },
                    {
                        "ResourceType": "NAS",
                        "ResourceName": "NAS",
                        "ResourceCount": 0
                    },
                    {
                        "ResourceType": "Snova",
                        "ResourceName": "Snova",
                        "ResourceCount": 0
                    },
                    {
                        "ResourceType": "Ckafka",
                        "ResourceName": "Ckafka",
                        "ResourceCount": 1
                    },
                    {
                        "ResourceType": "Grocery",
                        "ResourceName": "Grocery",
                        "ResourceCount": 0
                    },
                    {
                        "ResourceType": "Cloudhsm",
                        "ResourceName": "Cloudhsm",
                        "ResourceCount": 0
                    },
                    {
                        "ResourceType": "MongoDB",
                        "ResourceName": "MongoDB",
                        "ResourceCount": 0
                    }
                ]
            }
        ],
        "RequestId": "0fee1673-de33-4f0c-9ce4-037cbcf2d7b2"
    }
}
```

