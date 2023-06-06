**Example 1: 查询独享实例列表**

查询独享实例列表

Input: 

```
tccli apigateway DescribeExclusiveInstances --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {},
        "RequestId": "abc"
    }
}
```

