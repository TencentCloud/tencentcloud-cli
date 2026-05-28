**Example 1: ListPGUserMigrations**

查询指定环境已应用migration列表

Input: 

```
tccli tcb ListPGUserMigrations --cli-unfold-argument  \
    --EnvId pg-ethan06-d9gzgavrt1f14772b
```

Output: 
```
{
    "Response": {
        "LatestVersion": "20260526000000",
        "Migrations": [
            {
                "AppliedAt": "2026-05-26T11:26:14+08:00",
                "Checksum": "eeaf0dd9391ba7829bd12b47482fab4a0e031a040f00cfb6eafc5c23b9fcf791",
                "CreatedBy": "100019231666",
                "Name": "test_init",
                "Source": "cloudapi",
                "Version": "20260526000000"
            }
        ],
        "Total": 1,
        "RequestId": "926c3526-a4e1-4c6a-a5e6-f8ca0c3e175e"
    }
}
```

