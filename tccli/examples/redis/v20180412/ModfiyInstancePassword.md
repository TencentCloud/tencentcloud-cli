**Example 1: 变更密码**

重置实例的访问密码

Input: 

```
tccli redis ModfiyInstancePassword --cli-unfold-argument  \
    --InstanceId crs-5a4p**** \
    --OldPassword zy45**** \
    --Password 4569****
```

Output: 
```
{
    "Response": {
        "RequestId": "cca16225-a169-4f11-b1cf-13398200f604",
        "TaskId": 16661
    }
}
```

