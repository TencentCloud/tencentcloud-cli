**Example 1: CreateSmpnEpa**



Input: 

```
tccli smpn CreateSmpnEpa --cli-unfold-argument  \
    --ResourceId test_resource_id_for_smpn_epa \
    --RequestData.PhoneNumber 18122223554 \
    --RequestData.Name 黄页名称
```

Output: 
```
{
    "Response": {
        "RequestId": "891f2f2e-4851-4cd8-9555-8d92d6e77902",
        "ResponseData": {
            "RetCode": 0
        }
    }
}
```

