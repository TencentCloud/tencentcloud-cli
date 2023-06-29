**Example 1: 隔离容器网络状态**



Input: 

```
tccli tcss ModifyContainerNetStatus --cli-unfold-argument  \
    --ContainerID xxxx \
    --Status EVENT_ISOLATE_CONTAINER
```

Output: 
```
{
    "Response": {
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198"
    }
}
```

