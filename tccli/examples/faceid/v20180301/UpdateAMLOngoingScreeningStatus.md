**Example 1: 调用示例**



Input: 

```
tccli faceid UpdateAMLOngoingScreeningStatus --cli-unfold-argument  \
    --UniqueCustomerID USER_20260904_001 \
    --EnableOngoingScreening False
```

Output: 
```
{
    "Response": {
        "Description": "成功",
        "EnableOngoingScreening": false,
        "Result": "Success",
        "UniqueCustomerID": "USER_20260904_001",
        "RequestId": "84f22af4-9167-4e49-9d5f-db2987116bed"
    }
}
```

