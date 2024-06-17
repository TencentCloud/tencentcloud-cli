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
                "ClusterName": "abc",
                "ClusterId": "abc",
                "Region": "abc",
                "IdlType": "abc",
                "NetworkType": "abc",
                "VpcId": "abc",
                "SubnetId": "abc",
                "CreatedTime": "2020-09-22 00:00:00",
                "Password": "abc",
                "PasswordStatus": "abc",
                "ApiAccessId": "abc",
                "ApiAccessIp": "abc",
                "ApiAccessPort": 0,
                "OldPasswordExpireTime": "abc",
                "ApiAccessIpv6": "abc",
                "ClusterType": 0,
                "ClusterStatus": 0,
                "ReadCapacityUnit": 0,
                "WriteCapacityUnit": 0,
                "DiskVolume": 0,
                "ServerList": [
                    {
                        "ServerUid": "abc",
                        "MachineType": "abc",
                        "MemoryRate": 0,
                        "DiskRate": 0,
                        "ReadNum": 0,
                        "WriteNum": 0,
                        "Version": "abc"
                    }
                ],
                "ProxyList": [
                    {
                        "ProxyUid": "abc",
                        "MachineType": "abc",
                        "ProcessSpeed": 0,
                        "AverageProcessDelay": 0,
                        "SlowProcessSpeed": 0,
                        "Version": "abc"
                    }
                ],
                "Censorship": 0,
                "DbaUins": [
                    "abc"
                ],
                "DataFlowStatus": 0,
                "KafkaInfo": {
                    "Address": "abc",
                    "Topic": "abc",
                    "User": "abc",
                    "Password": "abc",
                    "Instance": "abc",
                    "IsVpc": 0
                },
                "TxhBackupExpireDay": 1,
                "UlogBackupExpireDay": 1,
                "IsReadOnlyUlogBackupExpireDay": 1,
                "RestProxyStatus": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

