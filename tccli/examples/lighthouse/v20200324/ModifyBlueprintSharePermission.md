**Example 1: 共享轻量应用服务器镜像到CVM镜像**

共享轻量应用服务器镜像到CVM镜像。

Input: 

```
tccli lighthouse ModifyBlueprintSharePermission --cli-unfold-argument  \
    --BlueprintId lhbp-fypya4jw \
    --Permission SHARE
```

Output: 
```
{
    "Response": {
        "RequestId": "4fe640d6-4912-4b43-9b3a-cc3bbab4cef2"
    }
}
```

**Example 2: 取消轻量应用服务器镜像共享到CVM镜像**

取消轻量应用服务器镜像共享到CVM镜像

Input: 

```
tccli lighthouse ModifyBlueprintSharePermission --cli-unfold-argument  \
    --BlueprintId lhbp-fypya4jw \
    --Permission CANCEL
```

Output: 
```
{
    "Response": {
        "RequestId": "cbc209f3-9ae3-4138-a3a5-fe4d83a43d24"
    }
}
```

