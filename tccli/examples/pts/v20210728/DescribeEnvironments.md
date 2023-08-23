**Example 1: 环境列表查询**

环境列表查询

Input: 

```
tccli pts DescribeEnvironments --cli-unfold-argument  \
    --ProjectIds project-xx \
    --EnvIds env-xx \
    --Name abc \
    --Offset 0 \
    --Limit 0 \
    --OrderBy abc \
    --Ascend True
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

