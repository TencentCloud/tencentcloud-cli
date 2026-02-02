**Example 1: 查询只读分析引擎实例详情**

本接口（DescribeLibraDBInstanceDetail）用于查询只读分析引擎实例详情

Input: 

```
tccli cynosdb DescribeLibraDBInstanceDetail --cli-unfold-argument  \
    --ClusterId cynosdbmysql-9xl6z5m1 \
    --InstanceId libradb-ins-3v7ejwba
```

Output: 
```
{
    "Response": {
        "AppId": 1300274166,
        "ClusterId": "cynosdbmysql-xxx",
        "ClusterName": "test_cluster",
        "Cpu": 8,
        "CreateTime": "2025-04-07 16:26:29",
        "InstanceId": "libradb-ins-3v7ejwba",
        "InstanceName": "test_1",
        "InstanceNetInfo": {
            "InstanceGroupId": "cynosdbmysql-grp-xxx",
            "InstanceGroupType": "libradbRo",
            "NetType": 1,
            "SubnetId": "subnet-xxxx",
            "Vip": "10.0.0.34",
            "VpcId": "vpc-dfa31dd1",
            "Vport": 2000,
            "WanDomain": "",
            "WanIP": "",
            "WanPort": 0,
            "WanStatus": "init"
        },
        "InstanceRole": "libradbRo",
        "InstanceType": "Common",
        "LibraDBVersion": "1.2404.21.0",
        "Memory": 32,
        "NetType": 0,
        "NodeCount": 1,
        "NodeInfo": [
            {
                "Cpu": 8,
                "DataStatus": "Running",
                "Memory": 32,
                "Message": "",
                "NodeId": "libradbn-0",
                "Status": "normal",
                "Storage": 20
            }
        ],
        "PayMode": 0,
        "PeriodEndTime": "0001-01-01 00:00:00",
        "PeriodStartTime": "2025-04-07 16:26:28",
        "ProjectId": 0,
        "Region": "ap-guangzhou",
        "RenewFlag": 1,
        "RequestId": "e760a135-4e85-42a0-99e8-8496f1a5ed0c",
        "ResourceTags": [],
        "Status": "running",
        "StatusDesc": "运行中",
        "Storage": 20,
        "StorageType": "CLOUD_TCS",
        "SubnetId": "",
        "Uin": "700001143625",
        "UpdateTime": "2025-04-07 16:29:05",
        "Vip": "",
        "VpcId": "",
        "Vport": 0,
        "Zone": "ap-guangzhou-7"
    }
}
```

