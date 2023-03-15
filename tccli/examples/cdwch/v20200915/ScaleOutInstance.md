**Example 1: test**

ck水平扩容实例

Input: 

```
tccli cdwch ScaleOutInstance --cli-unfold-argument  \
    --InstanceId abc \
    --Type abc \
    --NodeCount 0 \
    --ScaleOutCluster abc \
    --UserSubnetIPNum 0 \
    --ScaleOutNodeIp abc \
    --ReduceShardInfo abc
```

Output: 
```
{
    "Response": {
        "FlowId": "abc",
        "InstanceId": "abc",
        "ErrorMsg": "abc",
        "RequestId": "abc"
    }
}
```

