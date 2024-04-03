**Example 1: 示例**

示例

Input: 

```
tccli bi DescribeDatasourceList --cli-unfold-argument  \
    --ProjectId 2
```

Output: 
```
{
    "Response": {
        "Data": {
            "List": null,
            "Total": 0,
            "TotalPages": 0
        },
        "Extra": "",
        "Msg": "success",
        "RequestId": "3a66482b-7460-4d22-95bc-eae8c28568e4"
    }
}
```

**Example 2: success**

查询数据源列表

Input: 

```
tccli bi DescribeDatasourceList --cli-unfold-argument  \
    --ProjectId 11
```

Output: 
```
{
    "Response": {
        "RequestId": "b8116ab8-92e8-4370-b3d5-6cb464b83609",
        "Extra": "",
        "Data": {
            "List": null,
            "Total": 0,
            "TotalPages": 0
        },
        "Msg": "success"
    }
}
```

