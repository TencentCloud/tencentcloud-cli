**Example 1: 取消放开全部来源IP**

取消放开全部来源IP

Input: 

```
tccli bh ModifyAccessWhiteListStatus --cli-unfold-argument  \
    --AllowAny False
```

Output: 
```
{
    "Response": {
        "RequestId": "c7c79e35-65b9-4c2a-beea-a038fdf8c082"
    }
}
```

**Example 2: 放开全部来源IP**

放开全部来源IP

Input: 

```
tccli bh ModifyAccessWhiteListStatus --cli-unfold-argument  \
    --AllowAny True
```

Output: 
```
{
    "Response": {
        "RequestId": "c7c79e35-65b9-4c2a-beea-a038fdf8c082"
    }
}
```

