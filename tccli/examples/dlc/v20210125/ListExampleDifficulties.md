**Example 1: ListExampleDifficulties**

获取所有案例难度（去重）

Input: 

```
tccli dlc ListExampleDifficulties --cli-unfold-argument  \
    --Page 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Difficulty": "advanced"
            }
        ],
        "Page": 1,
        "PageSize": 10,
        "Total": 3,
        "TotalPages": 1,
        "RequestId": "163a459a-adbd-4cbf-8f1c-ebeb5ae0fe55"
    }
}
```

