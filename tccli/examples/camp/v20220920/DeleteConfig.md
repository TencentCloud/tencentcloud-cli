**Example 1: DeleteConfig**

删除配置

Input: 

```
tccli camp DeleteConfig --cli-unfold-argument  \
    --Platform abc \
    --ProjectID abc \
    --ConfigName abc \
    --ConfigVersion abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

**Example 2: 删除配置**



Input: 

```
tccli camp DeleteConfig --cli-unfold-argument  \
    --ProjectID prj-hjqj5jmt \
    --ConfigName dasdasdas \
    --ConfigVersion 0.0.1
```

Output: 
```
{
    "Response": {
        "RequestId": "caf9f780-2c2f-45b9-a165-d155ec7fab6d"
    }
}
```

