**Example 1: 示例**



Input: 

```
tccli rum DescribeTDEMFunnelList --cli-unfold-argument  \
    --AppId 1****2 \
    --Keyword 下单 \
    --Status active1 \
    --Page 1 \
    --PageSize 4
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "{\"Code\":\"InvalidParameter\",\"Message\":\"Status 仅支持 active 或 inactive\"}",
        "RequestId": "fc8ec2b7-0ccf-4b98-8d88-b167b5a5f4ac"
    }
}
```

