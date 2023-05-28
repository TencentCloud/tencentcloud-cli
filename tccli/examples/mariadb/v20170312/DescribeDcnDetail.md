**Example 1: 获取实例灾备详情**

获取实例灾备详情

Input: 

```
tccli mariadb DescribeDcnDetail --cli-unfold-argument  \
    --InstanceId tdsql-ohjuvzgt
```

Output: 
```
{
    "Response": {
        "DcnDetails": [
            {
                "Cpu": 1,
                "CreateTime": "2022-11-08 11:39:44",
                "DcnFlag": 1,
                "DcnStatus": 0,
                "EncryptStatus": 0,
                "InstanceId": "tdsql-ohjuvzgt",
                "InstanceName": "tdsql-ohjuvzgt",
                "InstanceType": 2,
                "Memory": 2,
                "PayMode": 0,
                "PeriodEndTime": "0001-01-01 00:00:00",
                "Region": "ap-guangzhou",
                "ReplicaConfig": null,
                "ReplicaStatus": null,
                "Status": 2,
                "StatusDesc": "运行中",
                "Storage": 10,
                "Vip": "172.16.16.140",
                "Vipv6": "",
                "Vport": 3306,
                "Zone": "ap-guangzhou-2"
            },
            {
                "Cpu": 1,
                "CreateTime": "2022-11-08 11:43:06",
                "DcnFlag": 2,
                "DcnStatus": 2,
                "EncryptStatus": 0,
                "InstanceId": "tdsql-61vf76u9",
                "InstanceName": "tdsql-61vf76u9",
                "InstanceType": 3,
                "Memory": 2,
                "PayMode": 0,
                "PeriodEndTime": "0001-01-01 00:00:00",
                "Region": "ap-guangzhou",
                "ReplicaConfig": {
                    "DelayReplicationType": "DEFAULT",
                    "DueTime": "",
                    "ReplicationDelay": 0,
                    "RoReplicationMode": "START"
                },
                "ReplicaStatus": {
                    "Delay": 0,
                    "Status": "RUNNING"
                },
                "Status": 2,
                "StatusDesc": "运行中",
                "Storage": 10,
                "Vip": "172.16.16.70",
                "Vipv6": "",
                "Vport": 3306,
                "Zone": "ap-guangzhou-3"
            }
        ],
        "RequestId": "6bd7aceb-4f68-4048-9551-037d16a0870b"
    }
}
```

