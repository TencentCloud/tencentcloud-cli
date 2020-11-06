**Example 1: Modifying the auto-renewal flag of a TencentDB instance**



Input: 

```
tccli cdb ModifyAutoRenewFlag --cli-unfold-argument  \
    --InstanceIds cdb-f35wr6wj \
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

