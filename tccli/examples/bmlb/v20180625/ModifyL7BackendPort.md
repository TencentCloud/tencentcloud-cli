**Example 1: 修改黑石负载均衡七层转发路径后端实例端口**



Input: 

```
tccli bmlb ModifyL7BackendPort --cli-unfold-argument  \
    --LoadBalancerId lb-47gazeml \
    --ListenerId lbl-l6fzjsx5 \
    --DomainId dm-hg8j52ud \
    --LocationId loc-02ywyc8b \
    --BindType 0 \
    --Port 555 \
    --InstanceId tcpm-px13l9jh \
    --NewPort 99
```

Output: 
```
{
    "Response": {
        "TaskId": "12344LBTASKID",
        "RequestId": "aa32786f-18c1-4251-a25c-351a0bab7985"
    }
}
```

