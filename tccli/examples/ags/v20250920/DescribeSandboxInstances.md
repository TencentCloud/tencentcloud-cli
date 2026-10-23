**Example 1: 按照实例id查询**



Input: 

```
tccli ags DescribeSandboxInstances --cli-unfold-argument  \
    --InstanceIds wvhtuasdgdg2fh5accrhr5g62v26yt6epmd54kx6
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "AuthMode": "DEFAULT",
                "CreateTime": "2026-08-25T17:00:27+08:00",
                "CustomConfiguration": {
                    "Resources": {
                        "CPU": "2000m",
                        "Memory": "1000Mi",
                        "Storage": ""
                    }
                },
                "ExpiresAt": "2026-08-25T17:05:19+08:00",
                "InstanceId": "wvhtuasdgdg2fh5accrhr5g62v26yt6epmd54kx6",
                "NetworkMode": "PUBLIC",
                "Persistent": false,
                "Status": "STOPPED",
                "TimeoutSeconds": 300,
                "ToolId": "sdt-an98k9md",
                "ToolName": "e2e-test-2f86f215",
                "UpdateTime": "2026-08-25T17:00:28+08:00"
            }
        ],
        "RequestId": "23950fb8-761b-4dc1-b843-4c5d6d04977b"
    }
}
```

