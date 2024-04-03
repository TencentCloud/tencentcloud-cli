**Example 1: 创建or修改设备分组**

POST / HTTP/1.1
Host: weilingwith.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: saveDeviceGroup

Input: 

```
tccli weilingwith SaveDeviceGroup --cli-unfold-argument  \
    --Id 0 \
    --ParentId 0 \
    --Name abc \
    --Description abc \
    --WorkspaceId 0 \
    --ApplicationToken abc
```

Output: 
```
{
    "Response": {
        "Result": {
            "Id": 0
        },
        "RequestId": "abc"
    }
}
```

