**Example 1: 实例开机**

实例关机不收费场景下，重新开机。

Input: 

```
tccli hai StartInstance --cli-unfold-argument  \
    --InstanceId hai-dunyfdff \
    --DryRun False
```

Output: 
```
{
    "Response": {
        "TaskId": 123456,
        "RequestId": "83697e89-90d2-4fff-bbb1-1bc3d53c4dfadfdad"
    }
}
```

