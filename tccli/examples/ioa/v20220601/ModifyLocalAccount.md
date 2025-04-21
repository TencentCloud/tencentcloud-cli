**Example 1: 修改用户名**

-

Input: 

```
tccli ioa ModifyLocalAccount --cli-unfold-argument  \
    --Id 862 \
    --UserName pftest \
    --Status 0 \
    --GroupId 8204
```

Output: 
```
{
    "Response": {
        "RequestId": "a33893fd-a0a7-4518-bafa-b293ea898e96"
    }
}
```

