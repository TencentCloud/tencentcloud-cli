**Example 1: 获取实例信息列表**

获取实例信息列表，支持按实例ID，实例名称，地域来查询实例相关信息。

Input: 

```
tccli dbbrain DescribeDiagDBInstances --cli-unfold-argument  \
    --IsSupported true \
    --Offset 0 \
    --Limit 50 \
    --Product mysql
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "DbScanStatus": 1,
        "Items": [
            {
                "GroupName": "4个地域一个组",
                "EventCount": 0,
                "Memory": 4000,
                "Product": "MySQL",
                "Cpu": 2,
                "Source": "TENCENT_CLOUD",
                "UniqSubnetId": "subnet-test",
                "DeployMode": "CUSTOM",
                "InstanceType": 1,
                "AuditRunningStatus": "normal",
                "Status": 1,
                "EngineVersion": "5.6",
                "InstanceId": "cdb-test",
                "Vport": 63492,
                "InitFlag": 1,
                "TaskStatus": 0,
                "UniqVpcId": "vpc-fstest",
                "GroupId": "dg-0ttest",
                "InstanceName": "长期监控",
                "HealthScore": 100,
                "InstanceConf": {
                    "OverviewDisplay": "Yes",
                    "DailyInspection": "Yes",
                    "KeyDelimiters": []
                },
                "AuditPolicyStatus": "UNBOUND",
                "Volume": 100,
                "DeadlineTime": "2021-02-25 16:33:26",
                "SecAuditStatus": "ON",
                "Region": "ap-guangzhou",
                "Vip": "10.5.0.9",
                "IsSupported": true,
                "CreateTime": "2021-02-25 16:33:26",
                "InternalVip": "10.5.0.9",
                "ClusterId": "cdb-test",
                "InternalVport": 9090,
                "ClusterName": "cdb-test"
            }
        ],
        "RequestId": "b2d08895-1cfe-48bc-b7f7-87fd7cb5d6f1"
    }
}
```

