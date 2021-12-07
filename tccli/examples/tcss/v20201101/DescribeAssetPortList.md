**Example 1: 查询端口占用列表**



Input: 

```
tccli tcss DescribeAssetPortList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Type": "tcp",
                "PublicIP": "-",
                "PublicPort": 0,
                "ContainerPort": 3306,
                "ContainerPID": 1,
                "ContainerName": "/some-mariadb",
                "HostID": "a339b0b9-f60c-4e04-a3dc-672fc5a3e499",
                "HostIP": "172.16.32.2",
                "ProcessName": "mariadbd",
                "ListenContainer": "tcp://:::3306",
                "ListenHost": "",
                "RunAs": "mysql:mysql"
            }
        ],
        "RequestId": "522d7714-ef53-4940-b0ed-46d59a3cf0fd",
        "TotalCount": 58
    }
}
```

