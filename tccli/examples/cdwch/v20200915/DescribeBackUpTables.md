**Example 1: 示例**

获取可备份表信息



Input: 

```
tccli cdwch DescribeBackUpTables --cli-unfold-argument  \
    --InstanceId cdwch-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "AvailableTables": [
            {
                "VCluster": "default",
                "Database": "db_test",
                "Table": "tb_test",
                "TotalBytes": 0,
                "Ips": "10.x.x.x",
                "ZooPath": "/data",
                "Rip": "192.x.x.x"
            }
        ],
        "ErrorMsg": "",
        "RequestId": "asdfaes-xad12x-123axafg"
    }
}
```

