**Example 1: 查询应用下的策略信息**

查询当前应用下的增量迁移策略，输出按照更新时间升序排序。

Input: 

```
tccli vod DescribeIncrementalMigrationStrategyInfos --cli-unfold-argument  \
    --SubAppId 123456789 \
    --SortBy.Field UpdateTime \
    --SortBy.Order Asc \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "b6376a73-reqid-demo-b097-de6bb60b3976",
        "StrategyInfoSet": [
            {
                "BucketId": "bucketid1",
                "HttpOriginConfig": {
                    "Mode": "ASYNC",
                    "OriginCondition": {
                        "HttpStatusCode": 404,
                        "Prefix": "test/"
                    },
                    "OriginInfo": {
                        "EndpointInfo": {
                            "Endpoint": "example.com",
                            "StandbyEndpointSet": [
                                "standby.com",
                                "standby2.com"
                            ]
                        },
                        "FileInfo": {
                            "PrefixConfig": {
                                "Prefix": "prefix"
                            },
                            "SuffixConfig": {
                                "Suffix": "suffix"
                            }
                        }
                    },
                    "OriginParameter": {
                        "HttpHeaderInfo": {
                            "FollowHttpHeaderKeySet": [
                                "Host"
                            ],
                            "HeaderFollowMode": "FOLLOW_ALL",
                            "NewHttpHeaderSet": [
                                {
                                    "Key": "Host",
                                    "Value": "demo.com"
                                }
                            ]
                        },
                        "HttpRedirectCode": 302,
                        "OriginRedirectionFollowMode": "FOLLOW",
                        "Protocol": "HTTP",
                        "QueryStringFollowMode": "FOLLOW"
                    }
                },
                "OriginType": "HTTP",
                "StrategyId": "im-123-demoid",
                "StrategyName": "demo1",
                "SubAppId": 123456789
            },
            {
                "BucketId": "bucketid2",
                "HttpOriginConfig": {
                    "Mode": "SYNC",
                    "OriginCondition": {
                        "HttpStatusCode": 404
                    },
                    "OriginInfo": {
                        "EndpointInfo": {
                            "Endpoint": "example.com"
                        }
                    },
                    "OriginParameter": {
                        "HttpHeaderInfo": {
                            "HeaderFollowMode": "IGNORE_ALL",
                            "NewHttpHeaderSet": [
                                {
                                    "Key": "host",
                                    "Value": "demo.com"
                                }
                            ]
                        },
                        "HttpRedirectCode": 301,
                        "OriginRedirectionFollowMode": "FOLLOW",
                        "Protocol": "HTTPS",
                        "QueryStringFollowMode": "FOLLOW"
                    }
                },
                "OriginType": "HTTP",
                "StrategyId": "im-123-demoid2",
                "StrategyName": "demo2",
                "SubAppId": 123456789
            }
        ],
        "TotalCount": 2
    }
}
```

**Example 2: 查询应用指定存储桶的增量迁移策略**

查询应用指定存储桶的增量迁移策略

Input: 

```
tccli vod DescribeIncrementalMigrationStrategyInfos --cli-unfold-argument  \
    --SubAppId 123456789 \
    --Filters.0.Name BucketId \
    --Filters.0.Values bucketid2 \
    --SortBy.Field UpdateTime \
    --SortBy.Order Asc \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "a70a4fb9-reqid-demo-aa39-3282aa745a26",
        "StrategyInfoSet": [
            {
                "BucketId": "bucketid2",
                "HttpOriginConfig": {
                    "Mode": "SYNC",
                    "OriginCondition": {
                        "HttpStatusCode": 404
                    },
                    "OriginInfo": {
                        "EndpointInfo": {
                            "Endpoint": "example2.com"
                        }
                    },
                    "OriginParameter": {
                        "HttpHeaderInfo": {
                            "HeaderFollowMode": "IGNORE_ALL",
                            "NewHttpHeaderSet": [
                                {
                                    "Key": "host",
                                    "Value": "demo.com"
                                }
                            ]
                        },
                        "HttpRedirectCode": 301,
                        "OriginRedirectionFollowMode": "FOLLOW",
                        "Protocol": "HTTPS",
                        "QueryStringFollowMode": "FOLLOW"
                    }
                },
                "OriginType": "HTTP",
                "StrategyId": "im-123-demoid2",
                "StrategyName": "demo2",
                "SubAppId": 123456789
            }
        ],
        "TotalCount": 1
    }
}
```

