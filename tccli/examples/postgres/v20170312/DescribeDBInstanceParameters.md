**Example 1: 查询实例指定参数信息**

查询实例postgres-lzrwgg6d的max_connecions参数信息

Input: 

```
tccli postgres DescribeDBInstanceParameters --cli-unfold-argument  \
    --ParamName max_connections \
    --DBInstanceId postgres-lzrwgg6d
```

Output: 
```
{
    "Response": {
        "Detail": [
            {
                "Advanced": false,
                "ClassificationCN": "连接和认证",
                "ClassificationEN": "Connections and Authentication",
                "CurrentValue": "2048",
                "DefaultValue": "2048",
                "EnumValue": null,
                "ID": 15124,
                "LastModifyTime": "",
                "Max": 2048,
                "Min": 100,
                "Name": "max_connections",
                "NeedReboot": true,
                "ParamDescriptionCH": "实例最大连接数",
                "ParamDescriptionEN": "Sets the maximum number of concurrent connections.",
                "ParamValueType": "integer",
                "SpecRelated": true,
                "SpecRelationSet": null,
                "StandbyRelated": 0,
                "Unit": "",
                "VersionRelationSet": null
            }
        ],
        "RequestId": "ce4ecf74-b26f-44e7-9340-539032e92b9f",
        "TotalCount": 1
    }
}
```

