**Example 1: 查询云边界分析-暴露路径下主机节点的进程列表**

查询云边界分析-暴露路径下主机节点的进程列表

Input: 

```
tccli csip DescribeAssetProcessList --cli-unfold-argument  \
    --Provider tencent
```

Output: 
```
{
    "Response": {
        "AssetProcessList": [
            {
                "AppID": 0,
                "CloudAccountID": "",
                "CloudAccountName": "",
                "CmdLine": "/usr/sbin/NetworkManager",
                "InstanceID": "ins-x",
                "InstanceName": "opcloudos8_1",
                "Port": "",
                "PrivateIp": "",
                "ProcessID": "",
                "ProcessName": "NetworkManager",
                "PublicIp": ""
            }
        ],
        "RequestId": "a6981e0a-681b-4472-83aa-cddbd2c7cccb",
        "TotalCount": 238
    }
}
```

