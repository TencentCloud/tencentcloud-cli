**Example 1: 内存马白名单-列表**

内存马白名单-列表

Input: 

```
tccli cwp DescribeMemShellRules --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --Filters.0.Name Keywords \
    --Filters.0.Values ef.*- \
    --Filters.1.Name ModifyTime \
    --Filters.1.Values 2024-08-01T11:37:27+08:00 2024-08-01T11:59:07+08:00 \
    --By ModifyTime \
    --Order DESC
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AnnotationsRegexp": ".*fg.*",
                "ClassNameRegexp": "clusterName regexp",
                "CreateTime": "2024-08-01T10:28:05+08:00",
                "GroupID": "1",
                "GroupName": "",
                "HandleHistory": 1,
                "Id": 9,
                "InterfacesRegexp": "ef.*-",
                "IsGlobal": 0,
                "LoaderClassNameRegexp": "kk",
                "LogicalSymbol": 1,
                "MachinesNums": "1",
                "ModifyTime": "2024-08-01T11:59:07+08:00",
                "Operator": "",
                "Status": 0,
                "SuperClassNameRegexp": "cde",
                "UuidHostips": [
                    {
                        "Hostip": "127.0.0.1",
                        "Uuid": "acdd5474-6360-4fd4-bfc7-843162cb8116"
                    }
                ]
            },
            {
                "AnnotationsRegexp": ".*fg.*",
                "ClassNameRegexp": "dds",
                "CreateTime": "2024-08-01T10:28:04+08:00",
                "GroupID": "2",
                "GroupName": "",
                "HandleHistory": 0,
                "Id": 8,
                "InterfacesRegexp": "ef.*-",
                "IsGlobal": 1,
                "LoaderClassNameRegexp": "kk",
                "LogicalSymbol": 1,
                "MachinesNums": "全部服务器",
                "ModifyTime": "2024-08-01T11:37:27+08:00",
                "Operator": "",
                "Status": 0,
                "SuperClassNameRegexp": "cde",
                "UuidHostips": [
                    {
                        "Hostip": "",
                        "Uuid": "69E78F7F-FFC7-47D1-B406-13C9852******"
                    }
                ]
            }
        ],
        "RequestId": "acdd5474-6360-4fd4-bfc7-843162cb8116",
        "TotalCount": 2
    }
}
```

