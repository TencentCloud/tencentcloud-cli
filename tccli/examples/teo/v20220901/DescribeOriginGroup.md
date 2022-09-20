**Example 1: 查询指定站点的源站组列表**



Input: 

```
tccli teo DescribeOriginGroup --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name zone-id \
    --Filters.0.Values zone-20hzkd4rdmy0 \
    --Filters.0.Fuzzy False
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "TotalCount": 1,
        "OriginGroups": [
            {
                "OriginGroupId": "origin-136db381-8d3d-11ec-89a4-00ff977fb3c8",
                "OriginGroupName": "origin-name",
                "ZoneId": "zone-20hzkd4rdmy0",
                "ZoneName": "tencent.com",
                "OriginRecords": [
                    {
                        "Area": [],
                        "Port": 80,
                        "Record": "1.2.3.4",
                        "RecordId": "record-4b2dbd84-8d9a-11ec-9527-00ff977fb3c8",
                        "Weight": 100
                    }
                ],
                "ConfigurationType": "weight",
                "OriginType": "self",
                "UpdateTime": "2020-09-22T00:00:00+00:00"
            }
        ]
    }
}
```

**Example 2: 查询指定源站组ID的源站组信息**



Input: 

```
tccli teo DescribeOriginGroup --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name zone-id \
    --Filters.0.Values zone-20hzkd4rdmy0 \
    --Filters.0.Fuzzy False \
    --Filters.1.Name origin-group-id \
    --Filters.1.Values origin-136db381-8d3d-11ec-89a4-00ff977fb3c8 \
    --Filters.1.Fuzzy False
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "TotalCount": 1,
        "OriginGroups": [
            {
                "OriginGroupId": "origin-136db381-8d3d-11ec-89a4-00ff977fb3c8",
                "OriginGroupName": "origin-name",
                "ZoneId": "zone-20hzkd4rdmy0",
                "ZoneName": "tencent.com",
                "OriginRecords": [
                    {
                        "Area": [],
                        "Port": 80,
                        "Record": "1.2.3.4",
                        "RecordId": "record-4b2dbd84-8d9a-11ec-9527-00ff977fb3c8",
                        "Weight": 100
                    }
                ],
                "ConfigurationType": "weight",
                "OriginType": "self",
                "UpdateTime": "2020-09-22T00:00:00+00:00"
            }
        ]
    }
}
```

**Example 3: 查询指定源站组名称的源站组信息（模糊查询）**



Input: 

```
tccli teo DescribeOriginGroup --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name zone-id \
    --Filters.0.Values zone-20hzkd4rdmy0 \
    --Filters.0.Fuzzy False \
    --Filters.1.Name origin-group-name \
    --Filters.1.Values name \
    --Filters.1.Fuzzy True
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "TotalCount": 1,
        "OriginGroups": [
            {
                "OriginGroupId": "origin-136db381-8d3d-11ec-89a4-00ff977fb3c8",
                "OriginGroupName": "origin-name",
                "ZoneId": "zone-20hzkd4rdmy0",
                "ZoneName": "tencent.com",
                "OriginRecords": [
                    {
                        "Area": [],
                        "Port": 80,
                        "Record": "1.2.3.4",
                        "RecordId": "record-4b2dbd84-8d9a-11ec-9527-00ff977fb3c8",
                        "Weight": 100
                    }
                ],
                "ConfigurationType": "weight",
                "OriginType": "self",
                "UpdateTime": "2020-09-22T00:00:00+00:00"
            }
        ]
    }
}
```

