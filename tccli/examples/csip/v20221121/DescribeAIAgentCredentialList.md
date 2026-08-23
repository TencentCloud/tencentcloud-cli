**Example 1: 调用示例**



Input: 

```
tccli csip DescribeAIAgentCredentialList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CredentialList": [
            {
                "CredName": "openclaw_gateway_token_env",
                "CredType": "UNKNOWN",
                "DetectTime": "2026-05-12T16:49:59Z",
                "ID": 835,
                "Locations": [
                    {
                        "ContainerID": "78ba821d5aa4d5c4117935ae8430b014f3af9bbbace58515032460fec2537a87",
                        "Content": "OPENCL***a09e",
                        "DelegateID": 0,
                        "InstanceID": "ins-7xdsd8tg",
                        "Line": 14,
                        "Path": "/proc/7926/environ",
                        "Status": 0
                    }
                ]
            }
        ],
        "TotalCount": 8,
        "RequestId": "9d9a9182-3c03-4e36-9fcf-3021a3af27ba"
    }
}
```

