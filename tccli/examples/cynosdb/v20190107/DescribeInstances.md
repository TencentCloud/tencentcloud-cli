**Example 1: 查询实例列表**



Input: 

```
tccli cynosdb DescribeInstances --cli-unfold-argument  \
    --OrderBy xx \
    --Status xx \
    --DbType xx \
    --OrderByType xx \
    --Filters.0.Values cynosdbpg-ins-bzkxxrmt \
    --Filters.0.Names xx \
    --Filters.0.ExactMatch True \
    --Filters.0.Name xx \
    --Offset 0 \
    --Limit 0 \
    --InstanceIds xx
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "ServerlessStatus": "",
                "WanStatus": "",
                "RenewFlag": 2,
                "Zone": "ap-guangzhou-3",
                "DbVersion": "5.7",
                "Storage": 100,
                "Memory": 4,
                "ProcessingTask": "",
                "Status": "deleted",
                "UpdateTime": "2020-11-13 11:43:04",
                "VpcId": "",
                "InstanceId": "cynosdbmysql-ins-pd59rjuk",
                "ClusterId": "cynosdbmysql-6bsl6k03",
                "NetType": 0,
                "PeriodEndTime": "2020-11-13 11:40:16",
                "InstanceType": "ro",
                "DestroyTime": "",
                "IsolateTime": "2020-11-13 11:40:28",
                "DestroyDeadlineText": "",
                "ProjectId": 0,
                "Region": "ap-guangzhou",
                "PayMode": 1,
                "SubnetId": "",
                "CynosVersion": "2.0.11",
                "StatusDesc": "已删除",
                "InstanceName": "cynosdbmysql-ins-pd59rjuk",
                "Cpu": 2,
                "WanDomain": "",
                "ClusterName": "预付费集群",
                "InstanceRole": "ro",
                "WanPort": 0,
                "Uin": "100000007539",
                "DbType": "MYSQL",
                "Vip": "",
                "AppId": 251007582,
                "WanIP": "",
                "Vport": 0,
                "CreateTime": "2020-11-13 11:37:30"
            },
            {
                "ServerlessStatus": "",
                "WanStatus": "",
                "RenewFlag": 2,
                "Zone": "ap-guangzhou-3",
                "DbVersion": "5.7",
                "Storage": 100,
                "Memory": 8,
                "ProcessingTask": "",
                "Status": "deleted",
                "UpdateTime": "2020-11-13 11:43:04",
                "VpcId": "",
                "InstanceId": "cynosdbmysql-ins-dxxbxr1a",
                "ClusterId": "cynosdbmysql-6bsl6k03",
                "NetType": 0,
                "PeriodEndTime": "2020-11-13 11:40:15",
                "InstanceType": "rw",
                "DestroyTime": "",
                "IsolateTime": "2020-11-13 11:40:25",
                "DestroyDeadlineText": "",
                "ProjectId": 0,
                "Region": "ap-guangzhou",
                "PayMode": 1,
                "SubnetId": "",
                "CynosVersion": "2.0.11",
                "StatusDesc": "已删除",
                "InstanceName": "cynosdbmysql-ins-dxxbxr1a",
                "Cpu": 4,
                "WanDomain": "",
                "ClusterName": "预付费集群",
                "InstanceRole": "master",
                "WanPort": 0,
                "Uin": "100000007539",
                "DbType": "MYSQL",
                "Vip": "",
                "AppId": 251007582,
                "WanIP": "",
                "Vport": 0,
                "CreateTime": "2020-11-13 11:35:24"
            }
        ],
        "TotalCount": 26,
        "RequestId": "03ea3f94-297d-11eb-8f30-525400b7dd5a"
    }
}
```

