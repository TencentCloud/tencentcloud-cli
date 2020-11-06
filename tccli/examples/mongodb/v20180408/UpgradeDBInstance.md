**Example 1: 升级包年包月的云数据库实例**

客户需要通过API升级包年包月的云数据库实例

Input: 

```
tccli mongodb UpgradeDBInstance --cli-unfold-argument  \
    --Memory 4 \
    --Volume 250 \
    --InstanceId cmgo-f555zzzz \
    --OplogSize 26
```

Output: 
```
{
    "Response": {
        "RequestId": "be8f4a30-ea2e-4623-8b6b-0ccce04cd9f7",
        "DealId": "19297475"
    }
}
```

