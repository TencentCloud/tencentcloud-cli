**Example 1: 获取MountPoint实例信息**



Input: 

```
tccli goosefs ListMountPointInstances --cli-unfold-argument  \
    --ClusterId clst-fpINuigO \
    --NodeId ins-0vtvhyru \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "MountPoints": [
            {
                "ClusterId": "clst-fpINuigO",
                "ConfigChanged": false,
                "ConfigId": "cosfs2-cfg-44fcf50c-6fd8",
                "ConfigName": "test-conf1",
                "CosBucketName": "goosefs-******-test-**********",
                "CreateTime": 1782788710,
                "KeepaliveEnabled": false,
                "KeepaliveStatus": "",
                "MountPath": "/mnt/conf_test10",
                "MountPointId": "mpc-HTVHoaAn",
                "MountSource": "cos://goosefs-******-test-**********/",
                "NodeId": "ins-0vtvhyru",
                "NodeIp": "10.0.0.15",
                "Status": "STOPPED",
                "UpdateTime": 1784690423
            }
        ],
        "TotalCount": 22,
        "RequestId": "20e2a6e4-10e1-4da7-9223-0fc129166d61"
    }
}
```

