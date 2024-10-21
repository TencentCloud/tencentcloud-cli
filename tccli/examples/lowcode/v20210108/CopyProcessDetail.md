**Example 1: 流程详情复制**



Input: 

```
tccli lowcode CopyProcessDetail --cli-unfold-argument  \
    --CopiedProcessKey abc \
    --CopiedVersion 0 \
    --NewProcessKey abc \
    --ProcessDesc abc \
    --ProcessName abc \
    --EnvType abc \
    --EnvId abc \
    --AppCode abc \
    --CopiedReleaseVersion abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

