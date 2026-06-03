**Example 1: success**



Input: 

```
tccli rum DescribeRumGroupLogV2 --cli-unfold-argument  \
    --OrderBy asc \
    --StartTime 1665993060000 \
    --Limit 10 \
    --Filter [{"Key": "instanceId", "Operator": "eq", "Value": "rum-xyz"}] \
    --EndTime 1665996660000 \
    --ID 100 \
    --Label date
```

Output: 
```
{
    "Response": {
        "RequestId": "81a43a52-d00f-462a-82da-89841117f4ca",
        "Result": "{\"code\":0,\"data\":[{\"1737254300150\":1},{\"1737254310941\":1}],\"msg\":\"\",\"request_id\":\"81a43a52-d00f-462a-82da-89841117f4ca\"}"
    }
}
```

