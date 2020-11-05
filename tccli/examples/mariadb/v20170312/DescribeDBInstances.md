**Example 1: Querying the list of instances by instance ID**



Input: 

```
tccli mariadb DescribeDBInstances --cli-unfold-argument  \
    --InstanceIds tdsql-722d255z
```

Output: 
```
{
    "Response": {
        "RequestId": "6838d283-fdd9-419c-aabe-df6ee5cf42a7",
        "TotalCount": 1,
        "Instances": [
            {
                "InstanceId": "tdsql-722d255z",
                "InstanceName": "tdsql-722d255z",
                "AppId": 1251006373,
                "OriginSerialId": "set_1524577391_54095887",
                "ProjectId": 0,
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-1",
                "VpcId": 75203,
                "SubnetId": 45109,
                "UniqueVpcId": "vpc-5rkcp0wb",
                "UniqueSubnetId": "subnet-6ffate6q",
                "Status": 2,
                "Vip": "172.17.0.8",
                "Vport": 3306,
                "WanDomain": "",
                "WanVip": "",
                "WanPort": 0,
                "CreateTime": "2018-04-24 21:40:59",
                "UpdateTime": "2018-04-24 22:25:59",
                "AutoRenewFlag": 0,
                "NodeCount": 2,
                "Id": 40964,
                "IsTmp": 0,
                "ExclusterId": "",
                "Memory": 2,
                "Storage": 30,
                "Qps": 2100,
                "Pid": 10890,
                "PeriodEndTime": "2018-05-02 21:40:59",
                "Uin": "20548499",
                "TdsqlVersion": "Designed based on MariaDB 10.1.9 (compatible with MySQL 5.6)"
            }
        ]
    }
}
```

