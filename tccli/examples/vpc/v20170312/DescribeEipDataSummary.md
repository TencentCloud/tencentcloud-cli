**Example 1: 全量运营数据拉取接口**

支持指定数据协议、地域

Input: 

```
tccli vpc DescribeEipDataSummary --cli-unfold-argument  \
    --RequestSourceInternal cloud_info_sec \
    --Limit 20 \
    --WatchScheme cEipTag_common \
    --DataRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "RawContent": "{\"uin\":2202081286,\"resourcePrefix\":\"eip\",\"resourceId\":\"eip-4hovjd7y\",\"tagKey\":\"kkkk\",\"tagValue\":\"56\",\"dateCreated\":1560544060,\"id\":2}",
                "RecordId": 2,
                "Region": "ap-guangzhou",
                "TableName": "cEipTag",
                "WatchScheme": "cEipTag_common"
            },
            {
                "RawContent": "{\"uin\":2202081286,\"resourcePrefix\":\"eip\",\"resourceId\":\"eip-4hovjd7y\",\"tagKey\":\"testkey\",\"tagValue\":\"34\",\"dateCreated\":1560544060,\"id\":3}",
                "RecordId": 3,
                "Region": "ap-guangzhou",
                "TableName": "cEipTag",
                "WatchScheme": "cEipTag_common"
            },
            {
                "RawContent": "{\"uin\":2202081286,\"resourcePrefix\":\"eip\",\"resourceId\":\"eip-qu1lizou\",\"tagKey\":\"123\",\"tagValue\":\"456\",\"dateCreated\":1560544060,\"id\":4}",
                "RecordId": 4,
                "Region": "ap-guangzhou",
                "TableName": "cEipTag",
                "WatchScheme": "cEipTag_common"
            },
            {
                "RawContent": "{\"uin\":2202081286,\"resourcePrefix\":\"eip\",\"resourceId\":\"eip-qu1lizou\",\"tagKey\":\"asd\",\"tagValue\":\"fgh\",\"dateCreated\":1560544060,\"id\":5}",
                "RecordId": 5,
                "Region": "ap-guangzhou",
                "TableName": "cEipTag",
                "WatchScheme": "cEipTag_common"
            },
            {
                "RawContent": "{\"uin\":2202081286,\"resourcePrefix\":\"eip\",\"resourceId\":\"eip-0q3rkmx0\",\"tagKey\":\"441\",\"tagValue\":\"114\",\"dateCreated\":1560544060,\"id\":6}",
                "RecordId": 6,
                "Region": "ap-guangzhou",
                "TableName": "cEipTag",
                "WatchScheme": "cEipTag_common"
            },
            {
                "RawContent": "{\"uin\":2202081286,\"resourcePrefix\":\"eip\",\"resourceId\":\"eip-0q3rkmx0\",\"tagKey\":\"414\",\"tagValue\":\"141\",\"dateCreated\":1560544060,\"id\":7}",
                "RecordId": 7,
                "Region": "ap-guangzhou",
                "TableName": "cEipTag",
                "WatchScheme": "cEipTag_common"
            },
            {
                "RawContent": "{\"uin\":2202081286,\"resourcePrefix\":\"eip\",\"resourceId\":\"eip-gq6vtj1c\",\"tagKey\":\"441\",\"tagValue\":\"111\",\"dateCreated\":1560544060,\"id\":8}",
                "RecordId": 8,
                "Region": "ap-guangzhou",
                "TableName": "cEipTag",
                "WatchScheme": "cEipTag_common"
            },
            {
                "RawContent": "{\"uin\":2202081286,\"resourcePrefix\":\"eip\",\"resourceId\":\"eip-7853rqxa\",\"tagKey\":\"441\",\"tagValue\":\"111\",\"dateCreated\":1560544060,\"id\":9}",
                "RecordId": 9,
                "Region": "ap-guangzhou",
                "TableName": "cEipTag",
                "WatchScheme": "cEipTag_common"
            },
            {
                "RawContent": "{\"uin\":2202081286,\"resourcePrefix\":\"eip\",\"resourceId\":\"eip-8zal36va\",\"tagKey\":\"441\",\"tagValue\":\"111\",\"dateCreated\":1560544060,\"id\":10}",
                "RecordId": 10,
                "Region": "ap-guangzhou",
                "TableName": "cEipTag",
                "WatchScheme": "cEipTag_common"
            },
            {
                "RawContent": "{\"uin\":2202081286,\"resourcePrefix\":\"eip\",\"resourceId\":\"eip-c20oe7ba\",\"tagKey\":\"441\",\"tagValue\":\"111\",\"dateCreated\":1560544060,\"id\":11}",
                "RecordId": 11,
                "Region": "ap-guangzhou",
                "TableName": "cEipTag",
                "WatchScheme": "cEipTag_common"
            },
            {
                "RawContent": "{\"uin\":2202081286,\"resourcePrefix\":\"eip\",\"resourceId\":\"eip-7jytgazw\",\"tagKey\":\"441\",\"tagValue\":\"111\",\"dateCreated\":1560544060,\"id\":12}",
                "RecordId": 12,
                "Region": "ap-guangzhou",
                "TableName": "cEipTag",
                "WatchScheme": "cEipTag_common"
            },
            {
                "RawContent": "{\"uin\":2202081286,\"resourcePrefix\":\"eip\",\"resourceId\":\"eip-hud9u570\",\"tagKey\":\"441\",\"tagValue\":\"111\",\"dateCreated\":1560544060,\"id\":13}",
                "RecordId": 13,
                "Region": "ap-guangzhou",
                "TableName": "cEipTag",
                "WatchScheme": "cEipTag_common"
            },
            {
                "RawContent": "{\"uin\":2202081286,\"resourcePrefix\":\"eip\",\"resourceId\":\"eip-qhy08zam\",\"tagKey\":\"1\",\"tagValue\":\"2\",\"dateCreated\":1560544060,\"id\":14}",
                "RecordId": 14,
                "Region": "ap-guangzhou",
                "TableName": "cEipTag",
                "WatchScheme": "cEipTag_common"
            },
            {
                "RawContent": "{\"uin\":2202081286,\"resourcePrefix\":\"eip\",\"resourceId\":\"eip-7ruym25e\",\"tagKey\":\"123\",\"tagValue\":\"321\",\"dateCreated\":1560544061,\"id\":15}",
                "RecordId": 15,
                "Region": "ap-guangzhou",
                "TableName": "cEipTag",
                "WatchScheme": "cEipTag_common"
            },
            {
                "RawContent": "{\"uin\":2202081286,\"resourcePrefix\":\"eip\",\"resourceId\":\"eip-bq62qjac\",\"tagKey\":\"adsf\",\"tagValue\":\"adsf\",\"dateCreated\":1560544061,\"id\":16}",
                "RecordId": 16,
                "Region": "ap-guangzhou",
                "TableName": "cEipTag",
                "WatchScheme": "cEipTag_common"
            },
            {
                "RawContent": "{\"uin\":2202081286,\"resourcePrefix\":\"eip\",\"resourceId\":\"eip-8usprnik\",\"tagKey\":\"124\",\"tagValue\":\"421\",\"dateCreated\":1560544061,\"id\":24}",
                "RecordId": 24,
                "Region": "ap-guangzhou",
                "TableName": "cEipTag",
                "WatchScheme": "cEipTag_common"
            },
            {
                "RawContent": "{\"uin\":2202081286,\"resourcePrefix\":\"eip\",\"resourceId\":\"eip-8usprnik\",\"tagKey\":\"1231\",\"tagValue\":\"12313\",\"dateCreated\":1560544061,\"id\":26}",
                "RecordId": 26,
                "Region": "ap-guangzhou",
                "TableName": "cEipTag",
                "WatchScheme": "cEipTag_common"
            },
            {
                "RawContent": "{\"uin\":230614980,\"resourcePrefix\":\"eip\",\"resourceId\":\"eip-ra28i4so\",\"tagKey\":\"test_tag\",\"tagValue\":\"test_value\",\"dateCreated\":1560544061,\"id\":27}",
                "RecordId": 27,
                "Region": "ap-guangzhou",
                "TableName": "cEipTag",
                "WatchScheme": "cEipTag_common"
            },
            {
                "RawContent": "{\"uin\":230614980,\"resourcePrefix\":\"eip\",\"resourceId\":\"eip-0e02pf40\",\"tagKey\":\"berton\",\"tagValue\":\"hello\",\"dateCreated\":1560544062,\"id\":31}",
                "RecordId": 31,
                "Region": "ap-guangzhou",
                "TableName": "cEipTag",
                "WatchScheme": "cEipTag_common"
            },
            {
                "RawContent": "{\"uin\":2202081286,\"resourcePrefix\":\"bwp\",\"resourceId\":\"bwp-coed87c2\",\"tagKey\":\"name\",\"tagValue\":\"sveinchen\",\"dateCreated\":1561133650,\"id\":57}",
                "RecordId": 57,
                "Region": "ap-guangzhou",
                "TableName": "cEipTag",
                "WatchScheme": "cEipTag_common"
            }
        ],
        "RequestId": "f8eda5db-7102-4763-a1ac-1e3acc92a247",
        "Total": 11132
    }
}
```

