**Example 1: 查询网络应用列表**

用于查询网络应用列表

Input: 

```
tccli cls DescribeNetworkApplications --cli-unfold-argument  \
    --Filters.0.Key name \
    --Filters.0.Values api
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "CreateTime": 1766490528,
                "LogsetId": "f1a7c428-e500-4e0b-8ed6-bfbe991560e6",
                "Name": "api_name",
                "NetworkAppId": "64f5ef50-f46a-4903-9091-a4640e566083",
                "Region": "ap-guangzhou",
                "SubUin": 100039234035,
                "TopicId": "4673b334-aee5-481e-b643-029a10f4a254",
                "Uin": 100026423095,
                "UpdateTime": 1766490528
            }
        ],
        "Total": 2,
        "RequestId": "dfcf166d-be6b-44cb-bbce-4528c1295b71"
    }
}
```

