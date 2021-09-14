**Example 1: 根据过滤条件获取 rum 项目列表**



Input: 

```
tccli rum DescribeProjects --cli-unfold-argument  \
    --Offset 1 \
    --Limit 20 \
    --Filters.0.Name 'Name' \
    --Filters.0.Values '测试项目名' '测试项目名2'
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

**Example 2: 获取 rum 项目列表**



Input: 

```
tccli rum DescribeProjects --cli-unfold-argument  \
    --Offset 1 \
    --Limit 20
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

