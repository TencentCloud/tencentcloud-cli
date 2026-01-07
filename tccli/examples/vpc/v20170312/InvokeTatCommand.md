**Example 1: 执行EIP直通命令**

执行EIP直通命令。

Input: 

```
tccli vpc InvokeTatCommand --cli-unfold-argument  \
    --InvokeScene EIP_DIRECT \
    --InstanceIds ins-1ksiem34 \
    --Parameters {"dst_eip":"43.137.44.127"}
```

Output: 
```
{
    "Response": {
        "InvocationStatus": "SUCCESS",
        "InstanceInvokeResult": [
            {
                "InstanceId": "ins-1ksiem34",
                "TaskStatus": "SUCCESS",
                "TaskResult": {
                    "ExitCode": 0,
                    "Output": "cm9vdAo=",
                    "Dropped": 0,
                    "OutputUploadCOSErrorInfo": "",
                    "OutputUrl": "",
                    "ExecStartTime": "2020-11-05T07:49:58+00:00",
                    "ExecEndTime": "2020-11-05T07:50:04+00:00"
                }
            }
        ],
        "RequestId": "410c9edd-6dde-40e9-8693-cc55bfc98ad8"
    }
}
```

