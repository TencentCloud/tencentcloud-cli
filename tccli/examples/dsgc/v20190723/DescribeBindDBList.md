**Example 1: 查询DB绑定的列表**

查询DB绑定的列表

Input: 

```
tccli dsgc DescribeBindDBList --cli-unfold-argument  \
    --DataSourceType cdb \
    --DataSourceId cdb-2345ffsdf2 \
    --DspaId dspa-abcd1234
```

Output: 
```
{
    "Response": {
        "BindDBList": [
            "szffsd0212"
        ],
        "BindList": [
            {
                "ResourceId": "cdb-2g345",
                "DbInfos": [
                    {
                        "DbName": "db2212",
                        "ValidStatus": "1"
                    }
                ]
            }
        ],
        "RequestId": "afsdfs-fg234sc"
    }
}
```

