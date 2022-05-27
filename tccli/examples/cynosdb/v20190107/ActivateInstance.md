**Example 1: 恢复实例访问**



Input: 

```
tccli cynosdb ActivateInstance --cli-unfold-argument  \
    --ClusterId cynosdbmysql-bzxxrmtq \
    --InstanceIdList cynosdbmysql-ins-7upukfpw
```

Output: 
```
{
    "Response": {
        "RequestId": "128046",
        "FlowId": "123"
    }
}
```

