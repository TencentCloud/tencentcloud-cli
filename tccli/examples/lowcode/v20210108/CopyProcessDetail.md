**Example 1: 流程详情复制**



Input: 

```
tccli lowcode CopyProcessDetail --cli-unfold-argument  \
    --CopiedProcessKey xx \
    --ProcessName xx \
    --EnvId env-001 \
    --ProcessDesc xx \
    --NewProcessKey xx \
    --CopiedVersion 0
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

