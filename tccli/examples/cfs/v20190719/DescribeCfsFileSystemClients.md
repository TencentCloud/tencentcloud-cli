**Example 1: 查询文件系统客户端**



Input: 

```
tccli cfs DescribeCfsFileSystemClients --cli-unfold-argument  \
    --FileSystemId cfs-12345
```

Output: 
```
{
    "Response": {
        "RequestId": "aaaa-bbbb-cccc-dddd",
        "ClientList": [
            {
                "MountDirectory": "/mnt",
                "ZoneName": "广州一区",
                "Zone": "ap-guangzhou-1",
                "VpcId": "vpc-gvem39gr",
                "ClientIp": "10.1.1.10",
                "CfsVip": "10.1.1.11"
            }
        ]
    }
}
```

