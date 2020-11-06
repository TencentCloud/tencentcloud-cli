**Example 1: 解绑黑石物理服务器或者托管服务器到七层转发路径**



Input: 

```
tccli bmlb UnbindL7Backends --cli-unfold-argument  \
    --LoadBalancerId lb-47gazeml \
    --ListenerId lbl-l6fzjsx5 \
    --DomainId dm-hg8j52ud \
    --LocationId loc-02ywyc8b \
    --BindType 0 \
    --BackendSet.0.Port 99 \
    --BackendSet.0.InstanceId tcpm-px13l9jh
```

Output: 
```
{
    "Response": {
        "TaskId": "109778LBTASKID",
        "RequestId": "12226230-0b32-40b8-8595-c93e809b7aaa"
    }
}
```

