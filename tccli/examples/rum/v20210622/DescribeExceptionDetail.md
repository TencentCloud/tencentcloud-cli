**Example 1: 拉取个例详情**



Input: 

```
tccli rum DescribeExceptionDetail --cli-unfold-argument  \
    --ProductId 5d4fa0e8d8 \
    --ClientIdentify 2b94f1df-4f5c-4ac6-9698-5863e0e8add1 \
    --Feature 6D0914E53B7B0E4CA61005BE48F26D16 \
    --IssueType 1 \
    --StartEventTime 1745164800 \
    --EndEventTime 1745251200 \
    --RequestHeader BEGIN{"X-ProductId": "5d4fa0e8d8","X-Tc-Username": "cdx_test"}END
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Data": "{\"baseRsp\":{\"code\":0,\"msg\":\"success\"},\"detail\":{\"base_detail\":{\"event_time\":\"1745207648\",\"report_time\":\"1745207689\",\"account_id\":\"100004\",\"qimei\":\"183ea3d1ed17004f9191cbf9eed40e97\",\"device_id\":\"183ea3d1ed17004f9191cbf9eed40e97\",\"os_version\":\"Android 11,level 30\",\"brand\":\"OnePlus\",\"model\":\"MT2110\",\"bundle_id\":\"com.example.sdkapp\",\"app_version\":\"4.4.3-SNAPSHOT\",\"hot_patch_version\":\"1234\",\"client_identify\":\"2b94f1df-4f5c-4ac6-9698-5863e0e8add1\",\"sdk_version\":\"4.4.3-SNAPSHOT\"}",
        "Message": "",
        "RequestId": "8e5a197b-3be3-4ee7-a08f-bb03b3153d8e"
    }
}
```

