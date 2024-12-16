**Example 1: 查询集群详情**



Input: 

```
tccli lighthousedb DescribeClusterDetail --cli-unfold-argument  \
    --ClusterId lhdbmysql-dzu7vipz
```

Output: 
```
{
    "Response": {
        "Detail": {
            "Charset": "utf8",
            "ClusterId": "lhdbmysql-dzu7vipz",
            "ClusterName": "MySQL-3o9T",
            "Cpu": 1,
            "CreateTime": "2021-04-23 11:25:54",
            "DbType": "MYSQL",
            "DbVersion": "5.7",
            "Memory": 1,
            "Region": "ap-guangzhou",
            "Status": "running",
            "StatusDesc": "运行中",
            "UsedStorage": 0
        },
        "RequestId": ""
    }
}
```

