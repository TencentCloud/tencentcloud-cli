**Example 1: 新增抽样**



Input: 

```
tccli rum ModifyProjectLimit --cli-unfold-argument  \
    --ProjectInterface web \
    --ProjectID 8 \
    --ReportRate 10 \
    --ReportType 1
```

Output: 
```
{
    "Response": {
        "Msg": "success",
        "RequestId": "a62c0f90-5ed0-4f3e-b285-8e4885a5ca45"
    }
}
```

**Example 2: 新增修改限流**

新增修改限流

Input: 

```
tccli rum ModifyProjectLimit --cli-unfold-argument  \
    --ProjectID 1 \
    --ProjectInterface web \
    --ReportRate 10 \
    --ReportType 1 \
    --ID 1
```

Output: 
```
{
    "Response": {
        "Msg": "xx",
        "RequestId": "xx"
    }
}
```

