**Example 1: 查看分析集群数据源信息**



Input: 

```
tccli cynosdb DescribeLibraDBDataSource --cli-unfold-argument  \
    --ClusterId libradb-r3ochnd5 \
    --InstanceId libradb-ins-c3dp0s9o
```

Output: 
```
{
    "Response": {
        "DataSourceList": [
            {
                "ClusterId": "cynosdbmysql-djhes6w5",
                "DBType": "cynos",
                "IP": "",
                "InstanceId": "cynosdbmysql-ins-348bdpck",
                "Port": 0
            },
            {
                "ClusterId": "cynosdbmysql-jogwvkth",
                "DBType": "cynos",
                "IP": "",
                "InstanceId": "cynosdbmysql-ins-ht2tdr9s",
                "Port": 0
            }
        ],
        "RequestId": "3d9cfef6-b56d-43de-80e8-d9602e9a94b8"
    }
}
```

