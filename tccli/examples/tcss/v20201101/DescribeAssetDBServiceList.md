**Example 1: 查询db服务列表**



Input: 

```
tccli tcss DescribeAssetDBServiceList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ServiceID": "316237346564376164346334376231386136636436306630306366326266393131323536323939383433",
                "HostID": "a339b0b9-f60c-4e04-a3dc-672fc5a3e499",
                "HostIP": "172.16.32.2",
                "ContainerName": "/some-mariadb",
                "MainType": "db",
                "Type": "mysql",
                "Version": "",
                "RunAs": "mysql:mysql",
                "Exe": "/usr/sbin/mariadbd",
                "Config": "",
                "ProcessCnt": 0,
                "AccessLog": "",
                "ErrorLog": "",
                "DataPath": "",
                "WebRoot": "",
                "Pids": [
                    6776
                ],
                "Listen": [
                    "tcp://:::3306"
                ],
                "Parameter": "mysqld",
                "ContainerId": "57c36b768d6a7164992a5070bff58a76dcaba251c02fdd1d79e7abedf5654aa2"
            },
            {
                "ServiceID": "373538346334313961333265643635333839393535323964623530613962623131323536323939383433",
                "HostID": "5f029cbb-3690-4e63-b49f-00699e274c09",
                "HostIP": "10.0.0.11",
                "ContainerName": "/redis",
                "MainType": "db",
                "Type": "redis",
                "Version": "",
                "RunAs": "redis:redis",
                "Exe": "/usr/local/bin/redis-server",
                "Config": "",
                "ProcessCnt": 0,
                "AccessLog": "",
                "ErrorLog": "",
                "DataPath": "",
                "WebRoot": "",
                "Pids": [
                    1324531
                ],
                "Listen": [
                    "tcp://:::6379",
                    "tcp://0.0.0.0:6379"
                ],
                "Parameter": "redis-server *:6379         ",
                "ContainerId": "690049831fc902c88a1f930c9cf2a67d235099bf7a61c1f62777c69629ded230"
            }
        ],
        "RequestId": "339214f6-ea32-4c1a-89fb-7973665cdc3c",
        "TotalCount": 2
    }
}
```

