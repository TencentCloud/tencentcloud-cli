**Example 1: 在指定的云桌面实例上执行脚本任务**



Input: 

```
tccli cvd RunCommand --cli-unfold-argument  \
    --InstanceId cdi-nqj1mqcjmirynr7 \
    --Content cGluZyAtbiA0IDEyNy4wLjAuMQ== \
    --WaitUntilDone True \
    --Type PowerShellScript \
    --ContentEncoding Base64
```

Output: 
```
{
    "Response": {
        "Detail": {
            "Status": "Finished",
            "Output": {
                "Encoding": "PlainText",
                "Lines": [
                    "\n"
                ],
                "AllLinesOffset": 1,
                "LinesOffset": 1,
                "AllLinesNum": 1,
                "LinesNum": 1
            },
            "InvokeId": "cdi-nqj1mqcjmirynr7-ecdfe348-cc7b-4594-98d6-37cf5f84969f",
            "ErrorCode": "",
            "ErrorInfo": ""
        },
        "RequestId": "a4c33d6d-d6a2-47d3-9a19-940ead9f8752",
        "InvokeId": "cdi-nqj1mqcjmirynr7-ecdfe348-cc7b-4594-98d6-37cf5f84969f"
    }
}
```

