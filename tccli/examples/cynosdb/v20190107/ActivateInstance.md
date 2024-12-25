**Example 1: 恢复实例访问**

恢复实例访问

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
        "RequestId": "fd5759b5-89e9-483c-b79c-d99b27c33192",
        "FlowId": 147842
    }
}
```

