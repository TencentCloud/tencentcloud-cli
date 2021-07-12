**Example 1: 查询实例组**



Input: 

```
tccli cynosdb DescribeClusterInstanceGrps --cli-unfold-argument  \
    --ClusterId cynosdbpg-oib3wx0i
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "InstanceGrpInfoList": [
            {
                "Status": "xx",
                "UpdatedTime": "2020-09-22 00:00:00",
                "WanDomain": "xx",
                "InstanceSet": [
                    {
                        "ServerlessStatus": "xx",
                        "WanStatus": "xx",
                        "RenewFlag": 0,
                        "Zone": "xx",
                        "DbVersion": "xx",
                        "Storage": 0,
                        "StorageId": "xx",
                        "Memory": 0,
                        "ProcessingTask": "xx",
                        "Status": "xx",
                        "UpdateTime": "2020-09-22 00:00:00",
                        "VpcId": "xx",
                        "MinCpu": 0.0,
                        "MaxCpu": 0.0,
                        "InstanceId": "xx",
                        "ClusterId": "xx",
                        "NetType": 0,
                        "SubnetId": "xx",
                        "InstanceType": "xx",
                        "DestroyTime": "xx",
                        "IsolateTime": "2020-09-22 00:00:00",
                        "DestroyDeadlineText": "xx",
                        "ProjectId": 0,
                        "Region": "xx",
                        "PayMode": 0,
                        "PeriodEndTime": "2020-09-22 00:00:00",
                        "CynosVersion": "xx",
                        "StatusDesc": "xx",
                        "InstanceName": "xx",
                        "Cpu": 0,
                        "StoragePayMode": 0,
                        "WanDomain": "xx",
                        "ClusterName": "xx",
                        "InstanceRole": "xx",
                        "WanPort": 0,
                        "Uin": "xx",
                        "DbType": "xx",
                        "Vip": "xx",
                        "AppId": 0,
                        "WanIP": "xx",
                        "Vport": 0,
                        "CreateTime": "2020-09-22 00:00:00"
                    }
                ],
                "WanPort": 0,
                "ClusterId": "xx",
                "DeletedTime": "2020-09-22 00:00:00",
                "WanStatus": "xx",
                "CreatedTime": "2020-09-22 00:00:00",
                "Vip": "xx",
                "InstanceGrpId": "xx",
                "AppId": 0,
                "WanIP": "xx",
                "Vport": 0,
                "Type": "xx"
            }
        ],
        "RequestId": "ed1bf4b2-4917-4f4f-9f7d-1562e34c9eeb"
    }
}
```

