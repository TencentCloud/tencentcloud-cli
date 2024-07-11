**Example 1: 升级MariaDB按量计费实例**

升级MariaDB按量计费实例

Input: 

```
tccli mariadb UpgradeHourDBInstance --cli-unfold-argument  \
    --InstanceId tdsql-cq3ndzu7 \
    --Memory 2 \
    --Storage 10
```

Output: 
```
{
    "Response": {
        "RequestId": "b3d8965f-5124-451d-be87-499ea75eb3a4"
    }
}
```

