**Example 1: 销毁DB Custom 集群**

将无需使用的 DB Custom 集群销毁

Input: 

```
tccli dbdc DestroyDBCustomCluster --cli-unfold-argument  \
    --ClusterId dbcc-c4pwpw3d
```

Output: 
```
{
    "Response": {
        "TaskId": 46,
        "RequestId": "f8093fdd-9d15-4c04-929c-4dea6b9e8e7e"
    }
}
```

