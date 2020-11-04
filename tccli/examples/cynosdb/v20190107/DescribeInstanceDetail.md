**Example 1: 查询实例详情**



Input: 

```
tccli cynosdb DescribeInstanceDetail --cli-unfold-argument  \
    --InstanceId cynosdbpg-ins-bzkxxrmt
```

Output: 
```
{
    "Response": {
        "RequestId": "175707",
        "Detail": {
            "Zone": "ap-guangzhou-3",
            "DbVersion": "10.0",
            "Storage": 100,
            "Memory": 4,
            "Status": "running",
            "UpdateTime": "2018-06-20 19:12:54",
            "VpcId": "vpc-1ptuei0b",
            "InstanceId": "cynosdbpg-ins-bzkxxrmt",
            "ClusterId": "cynosdbpg-cluster-5ne6bjyx",
            "NetType": 1,
            "PeriodEndTime": "2018-07-20 19:17:16",
            "InstanceType": "rw",
            "ProjectId": 0,
            "Region": "ap-guangzhou",
            "PayMode": 0,
            "SubnetId": "subnet-1tmw9t4o",
            "StatusDesc": "运行中",
            "InstanceName": "ahhah哈哈呵呵",
            "Cpu": 2,
            "WanDomain": "",
            "ClusterName": "cynosdbpg-cluster-5ne6bjyx",
            "InstanceRole": "master",
            "WanPort": 0,
            "Uin": "3374998458",
            "DbType": "POSTGRESQL",
            "Vip": "10.0.1.2",
            "AppId": 1251006243,
            "Vport": 5432,
            "CreateTime": "2018-06-20 19:12:54"
        }
    }
}
```

