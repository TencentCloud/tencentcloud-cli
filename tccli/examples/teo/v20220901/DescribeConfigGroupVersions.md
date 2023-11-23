**Example 1: 查询版本列表**

查询站点 ID 为 zone-2kpsqmtisdcb 的站点下配置组 ID 为 cg-27fil26zq2s1 的配置组下版本 ID 为 ver-2kuq2mhis9c0 的版本信息。

Input: 

```
tccli teo DescribeConfigGroupVersions --cli-unfold-argument  \
    --ZoneId zone-2kpsqmtisdcb \
    --GroupId cg-27fil26zq2s1 \
    --Filters.0.Name version-id \
    --Filters.0.Values ver-2kuq2mhis9c0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ConfigGroupVersionInfos": [
            {
                "VersionId": "ver-2kuq2mhis9c0",
                "Description": "test",
                "VersionNumber": "1.0",
                "GroupId": "cg-27fil26zq2s1",
                "GroupType": "l7_acceleration",
                "Status": "RELEASED",
                "CreateTime": "2020-09-22T00:00:00+00:00"
            }
        ],
        "RequestId": "9bd9c732-8f9a-4cd3-a3e8-1c9db5e53631"
    }
}
```

