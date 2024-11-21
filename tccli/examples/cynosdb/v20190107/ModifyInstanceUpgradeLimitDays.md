**Example 1: 修改实例小版本升级限制时间**



Input: 

```
tccli cynosdb ModifyInstanceUpgradeLimitDays --cli-unfold-argument  \
    --ClusterId cynosdbmysql-mwg7212w \
    --InstanceId cynosdbmysql-ins-m6f0hjkx \
    --UpgradeLimitDays 30
```

Output: 
```
{
    "Response": {
        "RequestId": "588fbc90-61a4-4125-bc70-65a3f8d1327e"
    }
}
```

