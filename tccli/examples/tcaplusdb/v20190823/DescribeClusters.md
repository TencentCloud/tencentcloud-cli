**Example 1: 查询集群列表**

查询用户所属的集群列表

Input: 

```
tccli tcaplusdb DescribeClusters --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Clusters": [
            {
                "ClusterName": "clustername",
                "ClusterId": "145462",
                "Region": "ap-shanghai",
                "IdlType": "proto",
                "NetworkType": "proto",
                "VpcId": "testvpc",
                "SubnetId": "testsubnetid",
                "CreatedTime": "2020-09-22 00:00:00",
                "Password": "passd1",
                "PasswordStatus": "1",
                "ApiAccessId": "accessid",
                "ApiAccessIp": "accessip",
                "ApiAccessPort": 0,
                "OldPasswordExpireTime": "17832322",
                "ApiAccessIpv6": "",
                "ClusterType": 0,
                "ClusterStatus": 0,
                "ReadCapacityUnit": 1000,
                "WriteCapacityUnit": 1000,
                "DiskVolume": 10,
                "ServerList": [
                    {
                        "ServerUid": "1",
                        "MachineType": "svr",
                        "MemoryRate": 0,
                        "DiskRate": 0,
                        "ReadNum": 0,
                        "WriteNum": 0,
                        "Version": "1"
                    }
                ],
                "ProxyList": [
                    {
                        "ProxyUid": "2",
                        "MachineType": "proxy",
                        "ProcessSpeed": 0,
                        "AverageProcessDelay": 0,
                        "SlowProcessSpeed": 0,
                        "Version": "2"
                    }
                ],
                "Censorship": 0,
                "DbaUins": [
                    "1888232"
                ],
                "DataFlowStatus": 0,
                "KafkaInfo": {
                    "Address": "address",
                    "Topic": "topic",
                    "User": "usr0",
                    "Password": "usrpasswd",
                    "Instance": "instid",
                    "IsVpc": 0
                },
                "TxhBackupExpireDay": 1,
                "UlogBackupExpireDay": 1,
                "IsReadOnlyUlogBackupExpireDay": 1,
                "RestProxyStatus": 0
            }
        ],
        "RequestId": "1947843-12321"
    }
}
```

