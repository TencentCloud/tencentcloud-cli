**Example 1: CopyAndroidInstance 示例**



Input: 

```
tccli gs CopyAndroidInstance --cli-unfold-argument  \
    --SourceAndroidInstanceId cai-1300055477-ea99GVmmMxh \
    --TargetAndroidInstanceId cai-1300055477-ea999ohpfry \
    --Excludes /data/media/0/Android/data/com.zlongame.cn.ro /data/app/com.zlongame.cn.ro*
```

Output: 
```
{
    "Response": {
        "RequestId": "69054011-bd78-4ac3-b091-e32d025de527",
        "TaskId": "b2979beb-2ac1-4e9a-bd77-68039dfeeb80"
    }
}
```

