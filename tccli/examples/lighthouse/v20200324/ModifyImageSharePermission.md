**Example 1: 共享CVM镜像到轻量应用服务器镜像**

共享CVM镜像到轻量应用服务器镜像。

Input: 

```
tccli lighthouse ModifyImageSharePermission --cli-unfold-argument  \
    --ImageId img-xkd784jw \
    --Permission SHARE
```

Output: 
```
{
    "Response": {
        "BlueprintId": "lhbp-su83x02a",
        "RequestId": "4fe640d6-4912-4b43-9b3a-cc3bbab4cef2"
    }
}
```

**Example 2: CVM镜像取消共享到轻量应用服务器镜像**

CVM镜像取消共享到轻量应用服务器镜像

Input: 

```
tccli lighthouse ModifyImageSharePermission --cli-unfold-argument  \
    --ImageId img-xkd784jw \
    --Permission CANEL
```

Output: 
```
{
    "Response": {
        "BlueprintId": null,
        "RequestId": "4fe640d6-4912-4b43-9b3a-cc3bbab4cef2"
    }
}
```

