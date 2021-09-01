**Example 1: 创建任务**



Input: 

```
tccli tiems CreateJob --cli-unfold-argument  \
    --Name test \
    --Description job \
    --WorkerCount 1 \
    --ConfigId asjcqn7wtdgrd7gt \
    --ResourceGroupId ap-beijing \
    --Cpu 100 \
    --Memory 100 \
    --PredictInput.InputDataFormat json \
    --PredictInput.OutputDataFormat json \
    --PredictInput.InputPath cos://data-test-1255502019.cos.ap-guangzhou.myqcloud.com/test/pmminput \
    --PredictInput.OutputPath cos://data-test-1255502019.cos.ap-guangzhou.myqcloud.com/test/ \
    --PredictInput.BatchSize 32
```

Output: 
```
{
    "Response": {
        "RequestId": "0448ae0a-d593-4a48-a025-bede58e1f841",
        "Job": {
            "Id": "aktwbxqmfkr8g44v",
            "Cluster": "ap-beijing",
            "Region": "ap-beijing",
            "Name": "test",
            "Runtime": "pmml",
            "Description": "job",
            "ConfigId": "asjcqn7wtdgrd7gt",
            "PredictInput": {
                "InputDataFormat": "json",
                "OutputDataFormat": "json",
                "InputPath": "cos://data-test-1255502019.cos.ap-guangzhou.myqcloud.com/test/pmminput",
                "OutputPath": "cos://data-test-1255502019.cos.ap-guangzhou.myqcloud.com/test/",
                "BatchSize": 32,
                "SignatureName": ""
            },
            "Status": {
                "DesiredWorkers": 0,
                "CurrentWorkers": 0,
                "Replicas": [],
                "Status": "Waiting",
                "Message": ""
            },
            "CreateTime": "2019-11-07T15:41:35+08:00",
            "StartTime": "",
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

