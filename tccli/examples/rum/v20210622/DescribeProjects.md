**Example 1: 根据过滤条件获取 RUM 应用列表**

根据过滤条件获取 RUM 应用列表

Input: 

```
tccli rum DescribeProjects --cli-unfold-argument  \
    --Limit 20 \
    --Filters.0.Values '测试项目名2' '测试项目名' \
    --Filters.0.Name 'Name' \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ProjectSet": [],
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

**Example 2: 获取 RUM 应用列表**

获取 RUM 应用列表

Input: 

```
tccli rum DescribeProjects --cli-unfold-argument  \
    --Limit 20 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ProjectSet": [],
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

