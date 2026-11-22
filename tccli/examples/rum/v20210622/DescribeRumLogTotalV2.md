**Example 1: 接口示例**

获取接口总数

Input: 

```
tccli rum DescribeRumLogTotalV2 --cli-unfold-argument  \
    --OrderBy asc \
    --StartTime 1767860481000000000 \
    --Limit 100 \
    --Filter [{"Key": "id","Operator": "eq","Value": "120000"}] \
    --EndTime 1767946881000000000 \
    --ID 120000
```

Output: 
```
{
    "Response": {
        "RequestId": "2eb407f1-108c-4fc2-9aa4-b94e72eb7e0b",
        "Result": "{\"Total\":1523}"
    }
}
```

