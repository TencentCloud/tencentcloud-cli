**Example 1: 修改黑石负载均衡七层监听器**



Input: 

```
tccli bmlb ModifyL7Listener --cli-unfold-argument  \
    --LoadBalancerId lb-47gazeml \
    --ListenerId lbl-l6fzjsx5 \
    --ListenerName renameListener \
    --Bandwidth 100
```

Output: 
```
{
    "Response": {
        "TaskId": "2385738",
        "RequestId": "40349a3f-752c-4a2b-8309-f13ee81bc891"
    }
}
```

