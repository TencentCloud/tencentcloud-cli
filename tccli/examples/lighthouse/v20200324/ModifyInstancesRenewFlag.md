**Example 1: 修改实例的续费标识**

修改实例的续费标识

Input: 

```
tccli lighthouse ModifyInstancesRenewFlag --cli-unfold-argument  \
    --InstanceIds lhins-ruy9d2tw \
    --RenewFlag NOTIFY_AND_AUTO_RENEW
```

Output: 
```
{
    "Response": {
        "RequestId": "4804b3a2-0c0f-4900-a39a-76885a17d4bb"
    }
}
```

