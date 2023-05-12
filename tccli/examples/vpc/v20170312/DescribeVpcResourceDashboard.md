**Example 1: 查看VPC资源信息**

查看VPC资源信息

Input: 

```
tccli vpc DescribeVpcResourceDashboard --cli-unfold-argument  \
    --VpcIds vpc-0akbol5v
```

Output: 
```
{
    "Response": {
        "ResourceDashboardSet": [
            {
                "VpcId": "vpc-0akbol5v",
                "SubnetId": "",
                "Classiclink": 0,
                "Nat": 2,
                "Vpngw": 1,
                "Dcg": 1,
                "Pcx": 1,
                "FlowLog": 0,
                "NetworkDetect": 0,
                "NetworkACL": 0,
                "Ip": 157,
                "CVM": 49,
                "LB": 1,
                "CDB": 88,
                "Cmem": 0,
                "CTSDB": 0,
                "MariaDB": 0,
                "SQLServer": 0,
                "Postgres": 0,
                "NAS": 0,
                "Greenplumn": 0,
                "Ckafka": 2,
                "Grocery": 0,
                "HSM": 17,
                "Tcaplus": 0,
                "Cnas": 0,
                "TiDB": 0,
                "Emr": 0,
                "SEAL": 0,
                "CFS": 0,
                "Oracle": 0,
                "ElasticSearch": 0,
                "TBaaS": 0,
                "Itop": 0,
                "DBAudit": 0,
                "CynosDBPostgres": 0,
                "Redis": 0,
                "MongoDB": 0,
                "DCDB": 0,
                "CynosDBMySQL": 0,
                "Subnet": 1,
                "RouteTable": 1
            }
        ],
        "RequestId": "0fee1673-de33-4f0c-9ce4-037cbcf2d7b2"
    }
}
```

