**Example 1: 查询实例升级检查任务**

无

Input: 

```
tccli cdb DescribeInstanceUpgradeCheckJob --cli-unfold-argument  \
    --InstanceId 037c0b3b-1320-11ee-b0c3-6c92bf629868 \
    --DstMysqlVersion 8.0
```

Output: 
```
{
    "Response": {
        "ExistUpgradeCheckJob": true,
        "JobId": 145,
        "RequestId": "60b5d6cd-aecc-4740-a681-353e645293b4"
    }
}
```

