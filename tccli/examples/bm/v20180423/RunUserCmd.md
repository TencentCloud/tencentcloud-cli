**Example 1: 运行自定义脚本**



Input: 

```
tccli bm RunUserCmd --cli-unfold-argument  \
    --CmdId cmd-aaaaa \
    --UserName root \
    --Password 123456 \
    --CmdParam xx \
    --InstanceIds cpm-xxx0 cpm-xxx1 cpm-xxx2
```

Output: 
```
{
    "Response": {
        "SuccessTaskInfoSet": [
            {
                "InstanceId": "cpm-xxx0",
                "TaskId": 902537
            },
            {
                "InstanceId": "cpm-xxx1",
                "TaskId": 902538
            }
        ],
        "FailedTaskInfoSet": [
            {
                "InstanceId": "cpm-xxx2",
                "ErrorMsg": "Some message"
            }
        ],
        "RequestId": "b035baf0-b935-4321-b6b4-cbd54c06437a"
    }
}
```

