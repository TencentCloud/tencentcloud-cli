**Example 1: success**



Input: 

```
tccli rum DescribeRumLogExportsV2 --cli-unfold-argument  \
    --PageSize 10 \
    --PageNum 1 \
    --ID 100
```

Output: 
```
{
    "Response": {
        "RequestId": "81a43a52-d00f-462a-82da-89841117f4ca",
        "Result": "{\"code\":0,\"data\":{\"code\":0,\"data\":{\"page\":1,\"pageSize\":999,\"totalCount\":1},\"msg\":\"\",\"request_id\":\"81a43a52-d00f-462a-82da-89841117f4ca\"}}"
    }
}
```

