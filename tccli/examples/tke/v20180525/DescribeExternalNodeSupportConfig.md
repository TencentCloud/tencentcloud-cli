**Example 1: 查看开启第三方节点池配置信息**



Input: 

```
tccli tke DescribeExternalNodeSupportConfig --cli-unfold-argument  \
    --ClusterId cls-lm91rql0
```

Output: 
```
{
    "Response": {
        "RequestId": "4c6c63c7-b23e-4896-bf3b-6bc44dxxxxxx",
        "ClusterCIDR": "172.22.0.0/16",
        "NetworkType": "CiliumVXLan",
        "SubnetId": "subnet-drsvvxxx",
        "Enabled": true,
        "AS": "1001",
        "SwitchIP": "1.1.1.1",
        "Status": "Initializing",
        "Proxy": "1.1.1.1",
        "Master": "1.1.1.1",
        "Progress": [
            {
                "EndAt": "2021-11-05T12:40:51Z",
                "Message": "",
                "Name": "EnsureNodeMasterCommunicate",
                "StartAt": "2021-11-05T12:40:45Z",
                "Status": "success"
            },
            {
                "EndAt": "2021-11-05T12:40:52Z",
                "Message": "",
                "Name": "EnsureInClusterAccess",
                "StartAt": "2021-11-05T12:40:51Z",
                "Status": "success"
            },
            {
                "EndAt": "2021-11-05T12:40:57Z",
                "Message": "",
                "Name": "EnsureExternalNodeProxy",
                "StartAt": "2021-11-05T12:40:52Z",
                "Status": "success"
            },
            {
                "EndAt": "2021-11-05T12:40:57Z",
                "Message": "",
                "Name": "EnsureBootStrap",
                "StartAt": "2021-11-05T12:40:57Z",
                "Status": "success"
            },
            {
                "EndAt": "2021-11-05T12:40:57Z",
                "Message": "",
                "Name": "EnsureAdmissionController",
                "StartAt": "2021-11-05T12:40:57Z",
                "Status": "success"
            },
            {
                "EndAt": "2021-11-05T12:41:00Z",
                "Message": "",
                "Name": "InstallUnderlayCilium",
                "StartAt": "2021-11-05T12:40:57Z",
                "Status": "success"
            },
            {
                "EndAt": "2021-11-05T12:41:00Z",
                "Message": "",
                "Name": "CompleteEnable",
                "StartAt": "2021-11-05T12:41:00Z",
                "Status": "success"
            }
        ],
        "FailedReason": "fail"
    }
}
```

