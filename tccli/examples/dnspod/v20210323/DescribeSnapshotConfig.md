**Example 1: 查询解析快照配置**

 查询解析快照配置

Input: 

```
tccli dnspod DescribeSnapshotConfig --cli-unfold-argument  \
    --Domain xx.com
```

Output: 
```
{
    "Response": {
        "RequestId": "567ca259-aff2-449b-a3af-c8cf7ee32f91",
        "SnapshotConfig": {
            "Id": "1112",
            "DomainId": "121212",
            "Status": "enable",
            "Config": "monthly",
            "CreatedOn": "2022-08-16 11:33:56",
            "UpdatedOn": "2022-10-16 11:34:21",
            "SnapshotCount": 3
        }
    }
}
```

