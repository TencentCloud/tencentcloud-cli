**Example 1: 更新任务**



Input: 

```
tccli tiems UpdateJob --cli-unfold-argument  \
    --JobId aktwbxqmfkr8g44v \
    --Description 123
```

Output: 
```
{
    "Response": {
        "RequestId": "a31293c1-d8ba-4dbb-828e-6f16016fbb88",
        "Job": {
            "Id": "aktwbxqmfkr8g44v",
            "Cluster": "ap-beijing",
            "Region": "ap-beijing",
            "Name": "test",
            "Runtime": "pmml",
            "Description": "123",
            "ConfigId": "0",
            "PredictInput": {
                "InputDataFormat": "json",
                "OutputDataFormat": "json",
                "InputPath": "cos://data-test-125502019.cos.ap-guangzhou.myqcloud.com/test/pmminput",
                "OutputPath": "cos://data-test-125502019.cos.ap-guangzhou.myqcloud.com/test/",
                "BatchSize": 32,
                "SignatureName": ""
            },
            "Status": {
                "DesiredWorkers": 1,
                "CurrentWorkers": 1,
                "Replicas": [
                    "aktwbxqmfkr8g44v-mwjbb"
                ],
                "Status": "Cancelled",
                "Message": ""
            },
            "CreateTime": "2019-11-07T15:41:35+08:00",
            "StartTime": "2019-11-07T15:41:35+08:00",
            "EndTime": "",
            "CancelTime": "",
            "ResourceGroupId": "ap-beijing",
            "ResourceGroupName": "公共资源组",
            "Cpu": 100,
            "Memory": 100,
            "Gpu": 0,
            "GpuMemory": 0,
            "GpuType": "",
            "ConfigName": "test1",
            "ConfigVersion": "1.0"
        }
    }
}
```

