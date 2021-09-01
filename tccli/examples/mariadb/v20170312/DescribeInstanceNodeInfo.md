**Example 1: 获取数据库实例主备节点信息**



Input: 

```
tccli mariadb DescribeInstanceNodeInfo --cli-unfold-argument  \
    --InstanceId tdsql-b43f8yjl
```

Output: 
```
{
    "Response": {
        "RequestId": "186315",
        "NodesInfo": [
            {
                "Role": "master",
                "NodeId": "5c2af09aeeb701fef6d5fef4329bb62d61f211ac"
            },
            {
                "Role": "slave",
                "NodeId": "dbedea66f4ba2b71e6816e3f9d0c2936e5448786"
            },
            {
                "Role": "slave",
                "NodeId": "1b40c8a28bec5c4af666d31b24119e319d68773e"
            }
        ],
        "TotalCount": 3
    }
}
```

