**Example 1: 示例**



Input: 

```
tccli dlc ListInferenceModels --cli-unfold-argument  \
    --Page 1 \
    --PageSize 2 \
    --StartTime 0 \
    --EndTime 1111 \
    --ParameterSizeMin 5 \
    --ParameterSizeMax 6
```

Output: 
```
{
    "Response": {
        "Items": [],
        "Page": 1,
        "PageSize": 2,
        "Total": 0,
        "TotalPages": 0,
        "RequestId": "3b46d143-1f21-456f-9a3f-3e8d568f413c"
    }
}
```

