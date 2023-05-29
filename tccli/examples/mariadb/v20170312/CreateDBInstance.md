**Example 1: 创建MariaDB包年包月实例**

创建MariaDB包年包月实例

Input: 

```
tccli mariadb CreateDBInstance --cli-unfold-argument  \
    --Zones ap-guangzhou-2 ap-guangzhou-2 \
    --Memory 2000 \
    --Storage 10000 \
    --NodeCount 1 \
    --Count 1 \
    --Period 1 \
    --AutoVoucher true
```

Output: 
```
{
    "Response": {
        "RequestId": "8c4fba95-01e4-61d9-4146-59fc5afdf962",
        "DealName": "20171103110163",
        "InstanceIds": null
    }
}
```

