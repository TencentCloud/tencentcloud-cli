**Example 1: 查询主机列表**



Input: 

```
tccli tcss DescribeAssetHostList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "HostID": "43d2d5df-93af-4229-b62e-60130801db2b",
                "HostName": "",
                "Group": "",
                "HostIP": "10.0.0.33",
                "DockerVersion": "",
                "DockerFileSystemDriver": "",
                "ImageCnt": 0,
                "ContainerCnt": 0,
                "Status": "online"
            },
            {
                "HostID": "1f17abee-b687-11ea-ab12-48fd8e5f45fe",
                "HostName": "VM-16-36-ubuntu",
                "Group": "",
                "HostIP": "172.16.16.36",
                "DockerVersion": "",
                "DockerFileSystemDriver": "",
                "ImageCnt": 0,
                "ContainerCnt": 0,
                "Status": "online"
            }
        ],
        "RequestId": "1a55edb3-33de-4538-81a8-8eb26a0db655",
        "TotalCount": 122
    }
}
```

