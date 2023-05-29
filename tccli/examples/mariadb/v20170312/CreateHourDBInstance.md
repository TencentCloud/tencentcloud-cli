**Example 1: 创建MariaDB按量计费实例**

创建MariaDB按量计费实例

Input: 

```
tccli mariadb CreateHourDBInstance --cli-unfold-argument  \
    --DbVersionId 5.7.17 \
    --VpcId vpc-n2vdqxdx \
    --Storage 10 \
    --Zones ap-guangzhou-1 ap-guangzhou-1 \
    --SubnetId subnet-j2ezrypg \
    --Memory 2 \
    --NodeCount 2
```

Output: 
```
{
    "Response": {
        "DealName": "20200409111543",
        "InstanceIds": [
            "tdsql-dup8gl6t"
        ],
        "FlowId": 22051110000,
        "RequestId": "05ad9b30-ac0a-4945-afd5-3d405d537a93"
    }
}
```

