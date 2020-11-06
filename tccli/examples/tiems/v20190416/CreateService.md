**Example 1: 创建服务**



Input: 

```
tccli tiems CreateService --cli-unfold-argument  \
    --ServiceConfigId asjcqn7wtdgrd7gt \
    --Name test \
    --ScaleMode MANUAL \
    --ResourceGroupId ap-beijing \
    --Cpu 100 \
    --Memory 100 \
    --Description test \
    --Scaler.StartReplicas 1
```

Output: 
```
{
    "Response": {
        "RequestId": "48d37fb1-15fa-4320-9c59-d673c653e0d4",
        "Service": {
            "Id": "ank95gbm4dwfhmds",
            "Cluster": "ap-beijing",
            "Region": "ap-beijing",
            "Name": "test",
            "Runtime": "pmml",
            "ModelUri": "cos://ti-ems-12502019.cos.ap-beijing.myqcloud.com/models/pmml/",
            "Cpu": 100,
            "Memory": 100,
            "Gpu": 0,
            "GpuMemory": 0,
            "CreateTime": "2019-11-07T15:14:19+08:00",
            "UpdateTime": "2019-11-07T15:14:19+08:00",
            "ScaleMode": "MANUAL",
            "Scaler": {
                "MaxReplicas": 1,
                "MinReplicas": 1,
                "StartReplicas": 1,
                "HpaMetrics": []
            },
            "Status": {
                "DesiredReplicas": 0,
                "CurrentReplicas": 1,
                "Replicas": [],
                "Status": "Waiting",
                "Message": "",
                "Conditions": []
            },
            "AccessToken": "",
            "ConfigName": "test1",
            "ConfigVersion": "1.0",
            "ServeSeconds": 1,
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

