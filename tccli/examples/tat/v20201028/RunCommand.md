**Example 1: 在 CVM 批量执行命令**



Input: 

```
tccli tat RunCommand --cli-unfold-argument  \
    --CommandName run-command \
    --SaveCommand False \
    --Description whoami \
    --Content d2hvYW1p \
    --CommandType SHELL \
    --WorkingDirectory /root/ \
    --Timeout 60 \
    --InstanceIds ins-zj0f57ew ins-zj0f57ex ins-zj0f57ev
```

Output: 
```
{
    "Response": {
        "RequestId": "f3e3a951-56b1-4042-af23-ba50223a8f60",
        "CommandId": "cmd-5oa8jajm",
        "InvocationId": "inv-mp6m9vmu"
    }
}
```

