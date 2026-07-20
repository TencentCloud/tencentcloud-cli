**Example 1: 设置当前课堂信令回放的主版本**



Input: 

```
tccli lcic SetMainEditVersion --cli-unfold-argument  \
    --SdkAppId 3520371 \
    --RoomId 326744409 \
    --VersionNo 2 \
    --Operator admin
```

Output: 
```
{
    "Response": {
        "ClassId": 326744409,
        "MainVersion": 2,
        "PreviousMainVersion": 0,
        "RequestId": "659fdede-d390-44ea-956d-06cde47ab178"
    }
}
```

