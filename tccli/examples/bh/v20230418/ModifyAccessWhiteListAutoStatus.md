**Example 1: 取消自动添加IP**

取消自动添加IP

Input: 

```
tccli bh ModifyAccessWhiteListAutoStatus --cli-unfold-argument  \
    --AllowAuto False
```

Output: 
```
{
    "Response": {
        "RequestId": "c7c79e35-65b9-4c2a-beea-a038fdf8c082"
    }
}
```

**Example 2: 放开自动添加IP**

放开自动添加P

Input: 

```
tccli bh ModifyAccessWhiteListAutoStatus --cli-unfold-argument  \
    --AllowAuto True
```

Output: 
```
{
    "Response": {
        "RequestId": "c7c79e35-65b9-4c2a-beea-a038fdf8c082"
    }
}
```

