**Example 1: 查询用户自定义引擎参数**

查询用户自定义引擎参数

Input: 

```
tccli dlc DescribeUserDataEngineConfig --cli-unfold-argument  \
    --Sorting xx \
    --Limit 0 \
    --Offset 0 \
    --SortBy xx \
    --Filters.0.Name xx \
    --Filters.0.Values xx
```

Output: 
```
{
    "Response": {
        "DataEngineConfigInstanceInfos": [
            {}
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

