**Example 1: 删除产出登记项**



Input: 

```
tccli wedata DeleteTaskOutputRegistry --cli-unfold-argument  \
    --Id 0 \
    --ProjectId abc \
    --TaskId abc
```

Output: 
```
{
    "Response": {
        "Data": 123,
        "RequestId": "abc"
    }
}
```

**Example 2: 示例1**

示例1

Input: 

```
tccli wedata DeleteTaskOutputRegistry --cli-unfold-argument  \
    --Id 3 \
    --ProjectId 1460947878944567296 \
    --TaskId 123456789
```

Output: 
```
{
    "Response": {
        "Data": 3,
        "RequestId": "334f1255-3610-4f14-bf0f-8cec9c46e0a5"
    }
}
```

