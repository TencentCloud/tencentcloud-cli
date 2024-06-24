**Example 1: 删除应用实例**

删除应用实例

Input: 

```
tccli camp DeleteInstance --cli-unfold-argument  \
    --ProjectID abc \
    --EnvironmentName abc \
    --ApplicationID abc \
    --InstanceID abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

**Example 2: 删除实例**



Input: 

```
tccli camp DeleteInstance --cli-unfold-argument  \
    --ProjectID prj-hjqj5jmt \
    --ApplicationID app-4vxd88l6 \
    --EnvironmentName development \
    --InstanceID tad-jrh2rl2w
```

Output: 
```
{
    "Response": {
        "RequestId": "5976eb0f-ab70-4636-a2ba-522b3189e908"
    }
}
```

