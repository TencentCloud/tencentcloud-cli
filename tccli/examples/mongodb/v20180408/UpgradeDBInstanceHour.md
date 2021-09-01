**Example 1: 升级包年包月的云数据库实例**

用户需要通过API升级包年包月的云数据库实例

Input: 

```
tccli mongodb UpgradeDBInstanceHour --cli-unfold-argument  \
    --Memory 4 \
    --Volume 250 \
    --InstanceId cmgo-f555zzz \
    --OplogSize 25
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "DealId": "20171201160000002670226599824833"
    }
}
```

