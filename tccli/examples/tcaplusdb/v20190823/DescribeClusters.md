**Example 1: 查询集群列表**

查询用户所属的集群列表

Input: 

```
tccli tcaplusdb DescribeClusters --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "RequestId": "xx",
        "Clusters": [
            {
                "ApiAccessIpv6": "xx",
                "DbaUins": [
                    "xx"
                ],
                "KafkaInfo": {
                    "IsVpc": true,
                    "Topic": "xx",
                    "Password": "xx",
                    "User": "xx",
                    "Address": "xx",
                    "Instance": "ckafka-l4xpzgpz"
                },
                "PasswordStatus": "xx",
                "CreatedTime": "2020-09-22 00:00:00",
                "WriteCapacityUnit": 0,
                "IdlType": "xx",
                "VpcId": "xx",
                "ApiAccessIp": "xx",
                "ClusterId": "xx",
                "ProxyList": [
                    {
                        "ProcessSpeed": 0,
                        "AverageProcessDelay": 0,
                        "MachineType": "xx",
                        "ProxyUid": "xx",
                        "SlowProcessSpeed": 0
                    }
                ],
                "Censorship": 0,
                "SubnetId": "xx",
                "Password": "xx",
                "ApiAccessId": "xx",
                "DiskVolume": 0,
                "DataFlowStatus": 0,
                "Region": "xx",
                "ClusterType": 0,
                "NetworkType": "xx",
                "OldPasswordExpireTime": "xx",
                "ServerList": [
                    {
                        "MachineType": "xx",
                        "ServerUid": "xx",
                        "ReadNum": 0,
                        "WriteNum": 0,
                        "MemoryRate": 0,
                        "DiskRate": 0
                    }
                ],
                "ApiAccessPort": 9999,
                "ClusterName": "xx",
                "ClusterStatus": 0,
                "ReadCapacityUnit": 0
            },
            {
                "ApiAccessIpv6": "xx",
                "DbaUins": [
                    "342",
                    "432432",
                    "342342"
                ],
                "PasswordStatus": "xx",
                "KafkaInfo": {
                    "IsVpc": true,
                    "Topic": "xx",
                    "Password": "xx",
                    "User": "xx",
                    "Address": "xx",
                    "Instance": "ckafka-l4xpzgpz"
                },
                "CreatedTime": "2020-09-22 00:00:00",
                "WriteCapacityUnit": 0,
                "IdlType": "xx",
                "VpcId": "xx",
                "ApiAccessIp": "xx",
                "ClusterId": "xx",
                "ClusterStatus": 0,
                "ProxyList": [
                    {
                        "MachineType": "xx",
                        "AverageProcessDelay": 0,
                        "ProcessSpeed": 0,
                        "ProxyUid": "xx",
                        "SlowProcessSpeed": 0
                    }
                ],
                "Censorship": 1,
                "SubnetId": "xx",
                "Password": "xx",
                "ApiAccessId": "xx",
                "DiskVolume": 0,
                "DataFlowStatus": 0,
                "Region": "xx",
                "ClusterType": 0,
                "OldPasswordExpireTime": "xx",
                "ServerList": [
                    {
                        "ServerUid": "xx",
                        "ReadNum": 0,
                        "DiskRate": 0,
                        "WriteNum": 0,
                        "MemoryRate": 0,
                        "MachineType": "xx"
                    }
                ],
                "ApiAccessPort": 9999,
                "ClusterName": "xx",
                "NetworkType": "xx",
                "ReadCapacityUnit": 0
            }
        ]
    }
}
```

