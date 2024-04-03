**Example 1: 111**



Input: 

```
tccli rum DescribeDataFetchProject --cli-unfold-argument  \
    --EndTime 1625454840 \
    --Type condition \
    --ID 1 \
    --StartTime 1625444040
```

Output: 
```
{
    "Response": {
        "RequestId": "9906759b-ea71-409e-b4e0-b877512713cf",
        "Result": "{\"request_id\":\"9906759b-ea71-409e-b4e0-b877512713cf\",\"results\":[{\"statement_id\":0,\"series\":[{\"name\":\"fetch_project_statistics\",\"columns\":[\"key\",\"value\"]}],\"total\":0},{\"statement_id\":1,\"series\":[{\"name\":\"fetch_project_statistics\",\"columns\":[\"key\",\"value\"]}],\"total\":0},{\"statement_id\":2,\"series\":[{\"name\":\"fetch_project_statistics\",\"columns\":[\"key\",\"value\"]}],\"total\":0},{\"statement_id\":3,\"series\":[{\"name\":\"fetch_project_statistics\",\"columns\":[\"key\",\"value\"]}],\"total\":0},{\"statement_id\":4,\"series\":[{\"name\":\"fetch_project_statistics\",\"columns\":[\"key\",\"value\"]}],\"total\":0},{\"statement_id\":5,\"series\":[{\"name\":\"fetch_project_statistics\",\"columns\":[\"key\",\"value\"]}],\"total\":0},{\"statement_id\":6,\"series\":[{\"name\":\"fetch_project_statistics\",\"columns\":[\"key\",\"value\"]}],\"total\":0},{\"statement_id\":7,\"series\":[{\"name\":\"fetch_project_statistics\",\"columns\":[\"key\",\"value\"]}],\"total\":0},{\"statement_id\":8,\"series\":[{\"name\":\"fetch_project_statistics\",\"columns\":[\"key\",\"value\"]}],\"total\":0},{\"statement_id\":9,\"series\":[{\"name\":\"fetch_project_statistics\",\"columns\":[\"key\",\"value\"]}],\"total\":0}]}"
    }
}
```

**Example 2: 获取DescribeDataFetchProject信息**



Input: 

```
tccli rum DescribeDataFetchProject --cli-unfold-argument  \
    --ExtSecond 自定义2 \
    --Engine ie2 \
    --IsAbroad 1 \
    --Area 中国 \
    --NetType 2 \
    --CostType avg \
    --Level 1 \
    --Os apple \
    --Brand apple \
    --Isp 中国移动 \
    --VersionNum 版本 \
    --Platform 2 \
    --ExtThird 自定义3 \
    --ExtFirst 自定义1 \
    --StartTime 1625444040 \
    --Device 三星 \
    --From index.html \
    --EndTime 1625454840 \
    --Type pagepv \
    --ID 1 \
    --Browser ie
```

Output: 
```
{
    "Response": {
        "Result": "xxxx",
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

