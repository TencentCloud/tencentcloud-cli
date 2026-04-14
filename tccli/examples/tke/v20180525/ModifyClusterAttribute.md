**Example 1: 修改安全模式参数**



Input: 

```
tccli tke ModifyClusterAttribute --cli-unfold-argument  \
    --ClusterId cls-p8wo3t7e \
    --SecurityModeConfig.Enabled False
```

Output: 
```
{
    "Response": {
        "AutoUpgradeClusterLevel": {
            "IsAutoUpgrade": false
        },
        "ClusterDesc": "",
        "ClusterLevel": "",
        "ClusterName": "",
        "ClusterProperty": {
            "NodeNameType": ""
        },
        "IsHighAvailability": false,
        "ProjectId": 0,
        "QGPUShareEnable": false,
        "SecurityModeConfig": {
            "Enabled": false
        },
        "RequestId": "ac4991da-f84d-4915-bf2d-2a7c8e6d8abf"
    }
}
```

