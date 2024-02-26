**Example 1: 删除指定定时任务**

删除定时任务`865d042d-0219-46c3-9821-6028c96cfb7c`。

Input: 

```
tccli cvm DeleteInstancesActionTimer --cli-unfold-argument  \
    --ActionTimerIds 865d042d-0219-46c3-9821-6028c96cfb7c
```

Output: 
```
{
    "Response": {
        "RequestId": "6e185c04-116f-47b7-b21c-e13580c5d0f2"
    }
}
```

