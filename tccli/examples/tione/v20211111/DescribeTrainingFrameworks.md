**Example 1: 训练框架列表**

查询训练框架列表

Input: 

```
tccli tione DescribeTrainingFrameworks --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "FrameworkInfos": [
            {
                "Name": "PYTORCH",
                "VersionInfos": [
                    {
                        "Version": "1.9",
                        "TrainingModes": [
                            "DDP",
                            "MPI",
                            "HOROVOD"
                        ],
                        "Environment": "torch1.9-py3.8-cuda11.1-gpu"
                    }
                ]
            }
        ],
        "RequestId": "c559beb8-9863-4929-9ef7-sasdasdwqe"
    }
}
```

