**Example 1: 升级版本号**

升级实例内核小版本

Input: 

```
tccli postgres UpgradeDBInstanceKernelVersion --cli-unfold-argument  \
    --DBInstanceId pgro-g7w4itfg \
    --TargetDBKernelVersion v12.7_r1.5 \
    --DryRun true
```

Output: 
```
{
    "Response": {
        "RequestId": "2b376d28-d5fd-40b0-9bdc-d992f8fed15d"
    }
}
```

