**Example 1: DescribeSmpnMhm**



Input: 

```
tccli smpn DescribeSmpnMhm --cli-unfold-argument  \
    --ResourceId test_resource_id_for_smpn_mhm \
    --RequestData.PhoneNumber 18122225555
```

Output: 
```
{
    "Response": {
        "RequestId": "891f2f2e-4851-4cd8-9555-8d92d6e77902",
        "ResponseData": {
            "TagType": 0,
            "TagCount": 0
        }
    }
}
```

