**Example 1: 重装 DB Custom 节点的操作系统**



Input: 

```
tccli dbdc ResetDBCustomNode --cli-unfold-argument  \
    --NodeId dbcn-lqzvz9er \
    --LoginSettings.Password paWD@123 \
    --ImageId img-7rqxtnh9 \
    --HostName host-name-reset-node
```

Output: 
```
{
    "Response": {
        "TaskId": 4062,
        "RequestId": "afe969e0-42ac-493b-a4e0-b1bfb0140059"
    }
}
```

