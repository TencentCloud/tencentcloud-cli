**Example 1: bri_num**



Input: 

```
tccli bri DescribeBRI --cli-unfold-argument  \
    --ResourceId test_resource_id_for_bri_num \
    --RequestData.Service bri_num \
    --RequestData.PhoneNumber 18122223554
```

Output: 
```
{
    "Response": {
        "RequestId": "891f2f2e-4851-4cd8-9555-8d92d6e77902",
        "ResponseData": {
            "Score": 71.0,
            "Tags": [
                "疑似新客户"
            ]
        }
    }
}
```

