**Example 1: 查询全网根账号组信息**



Input: 

```
tccli ioa DescribeRootAccountGroup --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "Description": "这里是该分组的描述",
            "ExtraInfo": "{\"salt\": \"xf681fafy\"}",
            "Id": 14632,
            "IdPath": "14632",
            "IdPathArr": [
                14632
            ],
            "Import": "0",
            "ImportEnable": false,
            "ImportType": "zijian",
            "Itime": "2023-04-18 23:01:11",
            "MiniIamId": "1256733004o8vX5K5hVcGCeQKddLZNmf",
            "Name": "全网账户",
            "NamePath": "全网账户",
            "OrgId": "0",
            "ParentId": 0,
            "ParentOrgId": "0",
            "Source": 0,
            "Utime": "2023-04-18 23:01:11"
        },
        "RequestId": "91b9b2f8-25cb-461c-9f48-2c5495c57f00"
    }
}
```

