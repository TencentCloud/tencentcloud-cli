**Example 1: 查询 TDSQL-C  分析集群列表**

查询 TDSQL-C  分析集群列表

Input: 

```
tccli cynosdb DescribeLibraDBClusters --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ClusterSet": [
            {
                "AppId": 1251966477,
                "ClusterId": "libradb-e9p7dqqm",
                "ClusterName": "按量计费",
                "CreateTime": "2025-06-20 17:01:53",
                "CynosVersion": "",
                "CynosVersionTag": "",
                "DbVersion": "3.2503.1.0",
                "InstanceNum": 1,
                "IsFreeze": "no",
                "MasterZone": "ap-qingyuan-1",
                "NetAddrs": [
                    {
                        "Description": "",
                        "InstanceGroupId": "",
                        "NetType": "libradbRo",
                        "UniqSubnetId": "subnet-mfsl0rqo",
                        "UniqVpcId": "vpc-95mugkpt",
                        "Vip": "192.168.254.39",
                        "Vport": 3306,
                        "WanDomain": "",
                        "WanIP": "",
                        "WanPort": 0,
                        "WanStatus": "init"
                    }
                ],
                "PayMode": 0,
                "PeriodEndTime": "0001-01-01 00:00:00",
                "PhysicalZone": "",
                "ProjectID": 0,
                "Region": "ap-qingyuan",
                "RenewFlag": 0,
                "Status": "running",
                "StatusDesc": "运行中",
                "Storage": 100,
                "SubnetId": "subnet-mfsl0rqo",
                "Tasks": [],
                "Uin": "3374998458",
                "UpdateTime": "2025-06-23 17:42:21",
                "Vip": "192.168.254.39",
                "VpcId": "vpc-95mugkpt",
                "Vport": 3306,
                "Zone": ""
            }
        ],
        "RequestId": "e22849e3-a047-4ad8-9d4d-c6929eeec965",
        "TotalCount": 1
    }
}
```

