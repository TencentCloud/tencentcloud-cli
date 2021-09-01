**Example 1: DescribeSmpnMrl**



Input: 

```
tccli smpn DescribeSmpnMrl --cli-unfold-argument  \
    --ResourceId test_resource_id_for_smpn_mrl \
    --RequestData.PhoneNumber 18122225555
```

Output: 
```
{
    "Response": {
        "RequestId": "891f2f2e-4851-4cd8-9555-8d92d6e77902",
        "ResponseData": {
            "DisturbLevel": 1,
            "HouseAgentLevel": 1,
            "InsuranceLevel": 1,
            "SalesLevel": 1,
            "CheatLevel": 1
        }
    }
}
```

