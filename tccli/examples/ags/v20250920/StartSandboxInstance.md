**Example 1: 启动普通沙箱**

通过 ToolId 启动一个沙箱实例

Input: 

```
tccli ags StartSandboxInstance --cli-unfold-argument  \
    --ToolId sdt-ee4ywozw \
    --Timeout 30m \
    --ClientToken start-sandbox-basic-example \
    --AuthMode TOKEN
```

Output: 
```
{
    "Response": {
        "Instance": {
            "InstanceId": "48dd1132cfb96ccee5fd0aa58da2562d2fe3a929",
            "ToolId": "sdt-ee4ywozw",
            "ToolName": "coding-agent",
            "Status": "STARTING"
        },
        "RequestId": "req-start-sandbox-example"
    }
}
```

