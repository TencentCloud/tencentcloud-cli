**Example 1: Getting migration check result**

This example shows you how to get the migration check result (check succeeded).

Input: 

```
tccli dts DescribeMigrateCheckJob --cli-unfold-argument  \
    --JobId dts-dau5czmd
```

Output: 
```
{
    "Response": {
        "Status": "finished",
        "ErrorCode": 0,
        "ErrorMessage": "ok",
        "Progress": "100",
        "CheckFlag": 1,
        "RequestId": "336448b0-2a45-4be4-8356-c245eab5784f"
    }
}
```

**Example 2: Getting migration check result - 2**

This example shows you how to get the migration check result (check failed).

Input: 

```
tccli dts DescribeMigrateCheckJob --cli-unfold-argument  \
    --JobId dts-1kl0iy0v
```

Output: 
```
{
    "Response": {
        "Status": "finished",
        "ErrorCode": -1,
        "ErrorMessage": "The selected table does not exist. Please select another one [the input parameter "table" was not found in the source instance]",
        "Progress": "100",
        "CheckFlag": 0,
        "RequestId": "67b4cfcf-6957-48ae-b7ef-ba33209895e3"
    }
}
```

