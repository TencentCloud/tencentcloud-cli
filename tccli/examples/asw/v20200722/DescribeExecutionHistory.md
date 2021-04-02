**Example 1: 查询执行的事件历史**



Input: 

```
tccli asw DescribeExecutionHistory --cli-unfold-argument  \
    --ExecutionResourceName qrn:qcs:asw:ap-guangzhou:1300074211:http:json:flowmachine:bilibili-machine:bfhzs4j8
```

Output: 
```
{
    "Response": {
        "Events": [
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:12345:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-xxxxx",
                "EventId": 1,
                "EventCategory": "ExecutionStart",
                "StepName": "START",
                "ResourceName": "",
                "Timestamp": "1596716960310",
                "Content": "{}",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:12345:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-xxxxx",
                "EventId": 2,
                "EventCategory": "Unknown",
                "StepName": "START",
                "ResourceName": "",
                "Timestamp": "1596716960310",
                "Content": "null",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:12345:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-xxxxx",
                "EventId": 3,
                "EventCategory": "PassNodeEnter",
                "StepName": "ReceivedVideo",
                "ResourceName": "",
                "Timestamp": "1596716960310",
                "Content": "{}",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:12345:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-xxxxx",
                "EventId": 4,
                "EventCategory": "PassNodeExit",
                "StepName": "ReceivedVideo",
                "ResourceName": "",
                "Timestamp": "1596716960310",
                "Content": "{}",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:12345:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-xxxxx",
                "EventId": 5,
                "EventCategory": "TaskNodeEnter",
                "StepName": "MPSAudioSeparate",
                "ResourceName": "qrn:qcs:asw:sh:1300074211:sdk:json:qcloud:mps:audioSeparate",
                "Timestamp": "1596716960311",
                "Content": "{}",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:12345:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-xxxxx",
                "EventId": 6,
                "EventCategory": "TaskNodeExit",
                "StepName": "MPSAudioSeparate",
                "ResourceName": "qrn:qcs:asw:sh:1300074211:sdk:json:qcloud:mps:audioSeparate",
                "Timestamp": "1596716960514",
                "Content": "{}",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:12345:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-xxxxx",
                "EventId": 7,
                "EventCategory": "TaskNodeEnter",
                "StepName": "CheckMPS",
                "ResourceName": "qrn:qcs:asw:sh:1300074211:sdk:json:qcloud:mps:checkMpsJob",
                "Timestamp": "1596716960514",
                "Content": "",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:12345:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-xxxxx",
                "EventId": 8,
                "EventCategory": "TaskNodeExit",
                "StepName": "CheckMPS",
                "ResourceName": "qrn:qcs:asw:sh:1300074211:sdk:json:qcloud:mps:checkMpsJob",
                "Timestamp": "1596716993478",
                "Content": "",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:12345:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-xxxxx",
                "EventId": 9,
                "EventCategory": "TaskNodeEnter",
                "StepName": "GetMPSAudioURL",
                "ResourceName": "qrn:qcs:asw:sh:1300074211:sdk:json:qcloud:scf:Invoke/GetMPSAudioURL",
                "Timestamp": "1596716993481",
                "Content": "",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:12345:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-xxxxx",
                "EventId": 10,
                "EventCategory": "TaskNodeExit",
                "StepName": "GetMPSAudioURL",
                "ResourceName": "qrn:qcs:asw:sh:1300074211:sdk:json:qcloud:scf:Invoke/GetMPSAudioURL",
                "Timestamp": "1596716993747",
                "Content": "{}",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:12345:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-xxxxx",
                "EventId": 11,
                "EventCategory": "TaskNodeEnter",
                "StepName": "ASR",
                "ResourceName": "qrn:qcs:asw:sh:1300074211:sdk:json:qcloud:asr:generalASR",
                "Timestamp": "1596716993748",
                "Content": "{}",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:12345:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-xxxxx",
                "EventId": 12,
                "EventCategory": "TaskNodeExit",
                "StepName": "ASR",
                "ResourceName": "qrn:qcs:asw:sh:1300074211:sdk:json:qcloud:asr:generalASR",
                "Timestamp": "1596716994159",
                "Content": "{}",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:12345:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-xxxxx",
                "EventId": 13,
                "EventCategory": "TaskNodeEnter",
                "StepName": "CheckASR",
                "ResourceName": "qrn:qcs:asw:sh:1300074211:sdk:json:qcloud:asr:checkASR",
                "Timestamp": "1596716994160",
                "Content": "{\"input\":\"{\"TaskId\":12345}\"}",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:12345:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-xxxxx",
                "EventId": 14,
                "EventCategory": "TaskNodeExit",
                "StepName": "CheckASR",
                "ResourceName": "qrn:qcs:asw:sh:1300074211:sdk:json:qcloud:asr:checkASR",
                "Timestamp": "1596717016158",
                "Content": "",
                "Exception": ""
            },
            {
                "ExecutionResourceName": "qrn:qcs:asw:ap-guangzhou:12345:execution:bfhzs4j8:bgi61l31bgi61l32-bgi61l33-bgi61kw0-xxxxx",
                "EventId": 15,
                "EventCategory": "Unknown",
                "StepName": "END",
                "ResourceName": "",
                "Timestamp": "1596717016159",
                "Content": "null",
                "Exception": ""
            }
        ],
        "RequestId": ""
    }
}
```

