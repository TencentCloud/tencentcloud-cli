**Example 1: 重启集群节点**



Input: 

```
tccli omics RebootHPCNodes --cli-unfold-argument  \
    --ClusterId hpc-9jragud9 \
    --NodeIds ins-85ckz3bg \
    --StopType SOFT
```

Output: 
```
{
    "Response": {
        "RequestId": "e73ad829-d0b8-418c-a07f-17561c294e71"
    }
}
```

