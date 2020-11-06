**Example 1: 绑定黑石物理服务器或半托管服务器到七层转发路径**



Input: 

```
tccli bmlb BindL7Backends --cli-unfold-argument  \
    --LoadBalancerId lb-47gazeml \
    --ListenerId lbl-l6fzjsx5 \
    --DomainId dm-hg8j52ud \
    --LocationId loc-02ywyc8b \
    --BindType 0 \
    --BackendSet.0.Port 555 \
    --BackendSet.0.InstanceId tcpm-px13l9jh \
    --BackendSet.0.Weight 100
```

Output: 
```
{
    "Response": {
        "TaskId": "109776LBTASKID",
        "RequestId": "40e18f3b-2e33-4fa5-9b06-4eb354d1a385"
    }
}
```

