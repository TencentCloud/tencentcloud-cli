**Example 1: 修改实例小版本升级限制时间**



Input: 

```
tccli cynosdb ModifyInstanceUpgradeLimitDays --cli-unfold-argument  \
    --ClusterId abc \
    --InstanceId abc \
    --UpgradeLimitDays 30
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

