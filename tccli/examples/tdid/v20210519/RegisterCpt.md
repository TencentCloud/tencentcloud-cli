**Example 1: RegisterCpt**

凭证模版新建

Input: 

```
tccli tdid RegisterCpt --cli-unfold-argument  \
    --ClusterId xx \
    --GroupId 1 \
    --CptJson xx \
    --CptId 1
```

Output: 
```
{
    "Response": {
        "Id": 42,
        "CptId": 1,
        "RequestId": "xx"
    }
}
```

