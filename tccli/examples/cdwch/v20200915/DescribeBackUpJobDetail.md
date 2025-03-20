**Example 1: 示例**



Input: 

```
tccli cdwch DescribeBackUpJobDetail --cli-unfold-argument  \
    --InstanceId cdwch-xxxxxxxx \
    --BackUpJobId 0
```

Output: 
```
{
    "Response": {
        "RequestId": "20a71202-27c4-4120-80c4-fb1a8e15dxxx",
        "TableContents": [
            {
                "Table": "tb_test",
                "Ips": "10.x.x.x",
                "VCluster": "default",
                "TotalBytes": 1024,
                "Database": "db_test",
                "ZooPath": "/data",
                "Rip": "192.x.x.x"
            }
        ]
    }
}
```

