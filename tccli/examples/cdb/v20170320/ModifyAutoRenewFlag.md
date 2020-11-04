**Example 1: 修改云数据库实例的自动续费标记**



Input: 

```
tccli cdb ModifyAutoRenewFlag --cli-unfold-argument  \
    --InstanceIds cdb-f35wr6wj\
    --AutoRenew 1
```

Output: 
```
{
    "Response": {
        "RequestId": "1a42feb9-82087f71-6a0031ac-699a92a8"
    }
}
```

