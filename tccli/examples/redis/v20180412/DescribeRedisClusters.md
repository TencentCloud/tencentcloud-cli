**Example 1: 示例1**



Input: 

```
tccli redis DescribeRedisClusters --cli-unfold-argument  \
    --Limit 100 \
    --DedicatedClusterId cluster-0astoh6a \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Total": 4,
        "Resources": [
            {
                "AppId": 251200288,
                "RegionId": 1,
                "ZoneId": 100002,
                "PayMode": 1,
                "ProjectId": 0,
                "AutoRenewFlag": 0,
                "ClusterName": "crs-cdc-9nyfki8h",
                "StartTime": "2022-06-10 14:40:33",
                "EndTime": "2022-07-10 14:40:33",
                "Status": 1,
                "RedisClusterId": "crs-cdc-9nyfki8h",
                "BaseBundles": [
                    {
                        "ResourceBundleName": "cc-standard",
                        "AvailableMemory": 0,
                        "Count": 1
                    }
                ],
                "ResourceBundles": [
                    {
                        "ResourceBundleName": "resource-bundle-mini",
                        "AvailableMemory": 16,
                        "Count": 1
                    }
                ],
                "DedicatedClusterId": "cluster-0astoh6a"
            },
            {
                "AppId": 251200288,
                "RegionId": 1,
                "ZoneId": 100002,
                "PayMode": 1,
                "ProjectId": 0,
                "AutoRenewFlag": 0,
                "ClusterName": "crs-cdc-3blwadqr",
                "StartTime": "2022-06-10 11:43:57",
                "EndTime": "2022-07-10 11:43:57",
                "Status": 1,
                "RedisClusterId": "crs-cdc-3blwadqr",
                "BaseBundles": [
                    {
                        "ResourceBundleName": "cc-standard",
                        "AvailableMemory": 0,
                        "Count": 1
                    }
                ],
                "ResourceBundles": [
                    {
                        "ResourceBundleName": "resource-bundle-mini",
                        "AvailableMemory": 16,
                        "Count": 1
                    }
                ],
                "DedicatedClusterId": "cluster-0astoh6a"
            },
            {
                "AppId": 251200288,
                "RegionId": 1,
                "ZoneId": 100002,
                "PayMode": 1,
                "ProjectId": 0,
                "AutoRenewFlag": 0,
                "ClusterName": "crs-cdc-etfesut3",
                "StartTime": "2022-06-10 11:00:25",
                "EndTime": "2022-07-10 11:00:25",
                "Status": 1,
                "RedisClusterId": "crs-cdc-etfesut3",
                "BaseBundles": [
                    {
                        "ResourceBundleName": "cc-standard",
                        "AvailableMemory": 0,
                        "Count": 1
                    }
                ],
                "ResourceBundles": [
                    {
                        "ResourceBundleName": "resource-bundle-mini",
                        "AvailableMemory": 16,
                        "Count": 1
                    },
                    {
                        "ResourceBundleName": "resource-bundle-large",
                        "AvailableMemory": 538,
                        "Count": 1
                    }
                ],
                "DedicatedClusterId": "cluster-0astoh6a"
            },
            {
                "AppId": 251200288,
                "RegionId": 1,
                "ZoneId": 100002,
                "PayMode": 1,
                "ProjectId": 0,
                "AutoRenewFlag": 0,
                "ClusterName": "crs-cdc-4myknrdf",
                "StartTime": "2022-06-10 10:33:12",
                "EndTime": "2022-08-10 10:33:12",
                "Status": 2,
                "RedisClusterId": "crs-cdc-4myknrdf",
                "BaseBundles": [
                    {
                        "ResourceBundleName": "cc-standard",
                        "AvailableMemory": 0,
                        "Count": 1
                    }
                ],
                "ResourceBundles": [
                    {
                        "ResourceBundleName": "resource-bundle-mini",
                        "AvailableMemory": 16,
                        "Count": 1
                    },
                    {
                        "ResourceBundleName": "resource-bundle-small-1",
                        "AvailableMemory": 48,
                        "Count": 2
                    }
                ],
                "DedicatedClusterId": "cluster-0astoh6a"
            }
        ],
        "RequestId": "1504cdf3-0095-4694-86d2-5f2a6f8c99a4"
    }
}
```

