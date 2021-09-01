**Example 1: 修改黑石负载均衡七层转发路径后端实例权重**



Input: 

```
tccli bmlb ModifyL7BackendWeight --cli-unfold-argument  \
    --LoadBalancerId lb-47gazeml \
    --ListenerId lbl-l6fzjsx5 \
    --DomainId dm-hg8j52ud \
    --LocationId loc-02ywyc8b \
    --BindType 0 \
    --Port 99 \
    --InstanceId tcpm-px13l9jh \
    --Weight 80
```

Output: 
```
{
    "Response": {
        "TaskId": "123456LBTASKID",
        "RequestId": "7cfc5d54-ea38-4656-a78b-30f27ab188a7"
    }
}
```

