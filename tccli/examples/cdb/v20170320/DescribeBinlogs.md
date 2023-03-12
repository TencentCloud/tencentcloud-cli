**Example 1: 查询二进制日志**

查询二进制日志

Input: 

```
tccli cdb DescribeBinlogs --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "BinlogFinishTime": "2020-11-12 21:13:12",
                "BinlogStartTime": "2020-11-12 21:13:04",
                "Date": "2020-11-12 21:13:35",
                "InternetUrl": "https://*****",
                "IntranetUrl": "https://*****",
                "Name": "cdb73977_binlog_mysqlbin.000004",
                "Size": 505,
                "Status": "FINISHED",
                "Region": "ap-guangzhou",
                "CosStorageType": 0,
                "RemoteInfo": [],
                "Type": "binlog",
                "InstanceId": "cdb-xxx"
            },
            {
                "BinlogFinishTime": "2020-11-12 21:13:04",
                "BinlogStartTime": "2020-11-02 11:38:49",
                "Date": "2020-11-12 21:13:25",
                "InternetUrl": "https://*****",
                "IntranetUrl": "https://*****",
                "Name": "cdb73977_binlog_mysqlbin.000003",
                "Size": 4537,
                "Status": "FINISHED",
                "Region": "ap-guangzhou",
                "CosStorageType": 0,
                "RemoteInfo": [],
                "Type": "binlog",
                "InstanceId": "cdb-xxx"
            }
        ],
        "RequestId": "2d8504a5-157d-4753-a060-6464b0e875e5",
        "TotalCount": 2
    }
}
```

