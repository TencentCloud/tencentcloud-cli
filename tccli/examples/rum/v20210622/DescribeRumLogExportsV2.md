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
        "Result": "[{\"id\":158000,\"task_id\":33,\"filters\":[{\"Key\":\"id\",\"Operator\":\"eq\",\"Value\":\"158000\"}],\"fields\":[\"aid\",\"level\"],\"last_row_id\":0,\"processed_total\":0,\"total\":0,\"status\":\"done\"}]"
    }
}
```

