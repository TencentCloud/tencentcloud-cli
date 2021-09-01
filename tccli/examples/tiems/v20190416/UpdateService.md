**Example 1: 更新服务**



Input: 

```
tccli tiems UpdateService --cli-unfold-argument  \
    --ServiceId ank95gbm4dwfhmds \
    --Scaler.StartReplicas 2 \
    --Scaler.MaxReplicas 2
```

Output: 
```
{
    "Response": {
        "RequestId": "9c7e1137-91a3-4c3b-8ff8-d695276a9b13",
        "Service": {
            "Id": "ank95gbm4dwfhmds",
            "Cluster": "ap-beijing",
            "Region": "ap-beijing",
            "Name": "test",
            "Runtime": "pmml",
            "ModelUri": "cos://ti-ems-125502019.cos.ap-beijing.myqcloud.com/models/pmml/",
            "Cpu": 100,
            "Memory": 100,
            "Gpu": 0,
            "GpuMemory": 0,
            "CreateTime": "2019-11-07T15:14:19+08:00",
            "UpdateTime": "2019-11-07T15:14:19+08:00",
            "ScaleMode": "MANUAL",
            "Scaler": {
                "MaxReplicas": 2,
                "MinReplicas": 0,
                "StartReplicas": 2,
                "HpaMetrics": []
            },
            "Status": {
                "DesiredReplicas": 1,
                "CurrentReplicas": 1,
                "Replicas": [
                    "ank95gbm4dwfhmds-fccc99cdd-ftff5"
                ],
                "Status": "Normal",
                "Message": "",
                "Conditions": []
            },
            "AccessToken": "",
            "ConfigName": "test1",
            "ConfigVersion": "1.0",
            "ServeSeconds": 307,
            "ConfigId": "asjcqn7wtdgrd7gt",
            "ResourceGroupId": "ap-beijing",
            "ResourceGroupName": "公共资源组",
            "Exposes": [],
            "Description": "test",
            "GpuType": ""
        }
    }
}
```

