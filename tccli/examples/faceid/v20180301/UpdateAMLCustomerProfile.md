**Example 1: 调用示例**



Input: 

```
tccli faceid UpdateAMLCustomerProfile --cli-unfold-argument  \
    --UniqueCustomerID USER_20260904_004 \
    --EntityType PERSON \
    --Person.FullName John Smith \
    --Person.DateOfBirth 1990-05-17 \
    --Person.Gender MALE \
    --Person.Nationality US
```

Output: 
```
{
    "Response": {
        "Description": "Customer profile updated successfully.",
        "EnableOngoingScreening": false,
        "Result": "Success",
        "RiskLevel": "SKIPPED",
        "RequestId": "b2027748-18a5-46bc-8247-28c04bf730ce"
    }
}
```

