**Example 1: 查询集群存储选项**

查询集群ID为hpc-5lyv94lq的集群存储选项信息。

Input: 

```
tccli thpc DescribeClusterStorageOption --cli-unfold-argument  \
    --ClusterId hpc-5lyv94lq
```

Output: 
```
{
    "Response": {
        "StorageOption": {
            "CFSOptions": [
                {
                    "LocalPath": "/opt/",
                    "RemotePath": "172.30.3.90:/j25ey5tz/hpc-kjddsnfa/opt/",
                    "Protocol": "NFS 3.0",
                    "StorageType": "SD"
                }
            ],
            "GooseFSOptions": [
                {
                    "LocalPath": "/data/",
                    "RemotePath": "/",
                    "Masters": [
                        "172.30.4.63:9202",
                        "172.30.0.128:9202"
                    ]
                }
            ]
        },
        "RequestId": "2aeaea7e-9fc4-4c17-8a9b-50343b712993"
    }
}
```

