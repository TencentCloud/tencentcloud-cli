**Example 1: 查询网络应用详情**

用于查询网络应用详情

Input: 

```
tccli cls DescribeNetworkApplicationDetail --cli-unfold-argument  \
    --NetworkAppId 64f5ef50-f46a-4903-9091-a4640e566083
```

Output: 
```
{
    "Response": {
        "Info": {
            "CreateTime": 1766490528,
            "LogsetId": "f1a7c428-e500-4e0b-8ed6-bfbe991560e6",
            "Name": "api_name",
            "NetworkAppId": "64f5ef50-f46a-4903-9091-a4640e566083",
            "Region": "ap-guangzhou",
            "SubUin": 100039234035,
            "Token": "eyJuX2FfaWQiOiI2NG***C1mNDZhLTQ5MDMtOTA5MS1hNDY0MGU1NjYwODMiLCJ1aW4iOjEwMDAyNjQyMzA5NSwia2V5IjoiZDUxMWZmMGYtN2E4Zi00MzIxLWJhNGQtO***cmVnaW9uIjoiYXAtZ3Vhbmd6aG91LW9wZW4i***BpY19pZCI6IjQ2NzNiMzM0LWFlZTUtNDgxZS1iNjQzLTAyOWExMGY0YTI1NCJ9",
            "TopicId": "4673b334-aee5-481e-b643-029a10f4a254",
            "Uin": 100026423095,
            "UpdateTime": 1766490528
        },
        "RequestId": "4941ebb4-8937-4ac1-a3a7-05b3b07540ec"
    }
}
```

