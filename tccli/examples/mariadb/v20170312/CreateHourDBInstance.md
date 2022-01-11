**Example 1: 创建后付费实例**



Input: 

```
tccli mariadb CreateHourDBInstance --cli-unfold-argument  \
    --Zones ap-guangzhou-1 ap-guangzhou-1 \
    --NodeCount 2 \
    --VpcId vpc-n2vdqxdx \
    --SubnetId subnet-j2ezrypg \
    --Memory 2 \
    --Storage 10 \
    --DbVersionId 5.7.17
```

Output: 
```
{
    "Response": {
        "DealName": "20200409111543",
        "InstanceIds": [
            "tdsql-dup8gl6t"
        ],
        "RequestId": "05ad9b30-ac0a-4945-afd5-3d405d537a93"
    }
}
```

