**Example 1: 修改实例规格**



Input: 

```
tccli tdcpg ModifyClusterInstancesSpec --cli-unfold-argument  \
    --ClusterId tdsqlcpg-xxx \
    --InstanceIdSet tdcpg-ins-xxx \
    --CPU 2 \
    --Memory 4 \
    --OperationTiming IMMIDIATE
```

Output: 
```
{
    "Response": {
        "RequestId": "03ea3f94-297d-11eb-8f30-525400b7dd5a"
    }
}
```

