**Example 1: 扩容云数据库实例**



Input: 

```
tccli mariadb UpgradeDBInstance --cli-unfold-argument  \
    --InstanceId tdsql-avw0207d \
    --Memory 2000 \
    --Storage 20000 \
    --AutoVoucher true
```

Output: 
```
{
    "Response": {
        "RequestId": "9b59ee51-0e13-1c2f-dedb-59fabe9d7f4a",
        "DealName": "20171103110035"
    }
}
```

