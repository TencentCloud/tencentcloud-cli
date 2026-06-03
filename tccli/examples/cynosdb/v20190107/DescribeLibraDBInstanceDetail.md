**Example 1: 查询分析实例信息**



Input: 

```
tccli cynosdb DescribeLibraDBInstanceDetail --cli-unfold-argument  \
    --ClusterId cynosdbmysql-pehkn7u7 \
    --InstanceId libradb-ins-6hmc6et4
```

Output: 
```
{
    "Response": {
        "AppId": 251232065,
        "ClusterId": "cynosdbmysql-pehkn7u7",
        "ClusterName": "cynos_libra回归v5.7_包年包月_202604161238",
        "Cpu": 4,
        "CreateTime": "2026-04-16 12:42:23",
        "InstanceId": "libradb-ins-6hmc6et4",
        "InstanceName": "LIBRADB_AUTO_TEST_包年包月",
        "InstanceNetInfo": {
            "InstanceGroupId": "cynosdbmysql-grp-foszl979",
            "InstanceGroupType": "libradbRo",
            "NetType": 1,
            "SubnetId": "subnet-c8tytrdg",
            "Vip": "10.0.5.177",
            "VpcId": "vpc-d3pif7pp",
            "Vport": 3306,
            "WanDomain": "",
            "WanIP": "",
            "WanPort": 0,
            "WanStatus": "init"
        },
        "InstanceRole": "libradbRo",
        "InstanceType": "common",
        "LibraDBVersion": "5.2512.1.0",
        "Memory": 16,
        "NetType": 0,
        "NodeCount": 1,
        "NodeInfo": [
            {
                "Cpu": 4,
                "DataStatus": "Running",
                "Memory": 16,
                "Message": "",
                "NodeId": "libradbn-0",
                "Status": "normal",
                "Storage": 50
            }
        ],
        "PayMode": 1,
        "PeriodEndTime": "2026-05-16 12:42:22",
        "PeriodStartTime": "2026-04-16 12:42:22",
        "ProjectId": 0,
        "Region": "ap-guangzhou",
        "RenewFlag": 0,
        "ResourceTags": [],
        "Status": "running",
        "StatusDesc": "运行中",
        "Storage": 50,
        "StorageType": "CLOUD_HSSD",
        "SubnetId": "",
        "Uin": "700000432793",
        "UpdateTime": "2026-04-16 12:45:47",
        "Vip": "",
        "VpcId": "",
        "Vport": 0,
        "Zone": "ap-guangzhou-4",
        "RequestId": "f18a0453-6340-4420-a0a0-a0857e84f4cf"
    }
}
```

