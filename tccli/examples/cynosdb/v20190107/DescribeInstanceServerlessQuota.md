**Example 1: 查询集群Serverless弹性信息**



Input: 

```
tccli cynosdb DescribeInstanceServerlessQuota --cli-unfold-argument  \
    --ClusterId cynosdbmysql-mf7uf72f
```

Output: 
```
{
    "Response": {
        "InstanceQuotas": [
            {
                "EnableTime": "2026-09-11 16:31:33",
                "InstanceId": "cynosdbmysql-ins-j6vccbsi",
                "MaxCcu": 8,
                "Status": "opened"
            }
        ],
        "QuotaConfigs": [
            {
                "InstanceType": "ro",
                "MaxCcu": 8,
                "Status": "opened"
            }
        ],
        "RequestId": "24a3aeaf-8cab-4e78-925e-1dbc3ca0c3e4"
    }
}
```

