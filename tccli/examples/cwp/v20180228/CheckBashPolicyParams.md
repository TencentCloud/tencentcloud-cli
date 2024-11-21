**Example 1: 示例**



Input: 

```
tccli cwp CheckBashPolicyParams --cli-unfold-argument  \
    --CheckField Name,Process \
    --EventId 1098230 \
    --Name mapleaa \
    --Rule rm -f /tmp/* \
    --Id 1320 \
    --Rules.Process.Exe /tmp/test \
    --Rules.Process.Cmdline /tmp/test \
    --Rules.PProcess.Exe /tmp/test \
    --Rules.PProcess.Cmdline /tmp/test \
    --Rules.AProcess.Exe /tmp/test \
    --Rules.AProcess.Cmdline /tmp/test
```

Output: 
```
{
    "Response": {
        "RequestId": "d92d723e-4aac-4f4a-bbf9-e5430e29d289",
        "ErrCode": 2,
        "ErrMsg": "正则表达式与命令内容不匹配"
    }
}
```

