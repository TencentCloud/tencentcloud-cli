**Example 1: 1**



Input: 

```
tccli tdmysql DescribeDatabases --cli-unfold-argument  \
    --InstanceId “tdsql3-01d1c3ed”
```

Output: 
```
{
    "Response": {
        "Databases": [
            {
                "DbName": "mysql"
            }
        ],
        "InstanceId": "tdsql3-01d1c3ed",
        "RequestId": "9b5e5e4a-30f2-46f8-91ee-788495d1e21f"
    }
}
```

**Example 2: 123**



Input: 

```
tccli tdmysql DescribeDatabases --cli-unfold-argument  \
    --InstanceId tdsql3-jko12hds
```

Output: 
```
{
    "Response": {
        "Databases": [],
        "InstanceId": "tdsql3-jko12hds",
        "RequestId": "2efb7186-2e29-46d1-9bc7-05dc2b8240bf"
    }
}
```

**Example 3: 查询云数据库实例上的数据库列表**



Input: 

```
tccli tdmysql DescribeDatabases --cli-unfold-argument  \
    --InstanceId tdsql3-5baee8df
```

Output: 
```
{
    "Response": {
        "Databases": [
            {
                "DbName": "information_schema"
            },
            {
                "DbName": "mysql"
            },
            {
                "DbName": "performance_schema"
            },
            {
                "DbName": "sys"
            }
        ],
        "InstanceId": "tdsql3-42f40429 ",
        "RequestId": "545457454fdasda"
    }
}
```

