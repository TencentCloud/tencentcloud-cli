**Example 1: 删除设备分组**

	
POST / HTTP/1.1
Host: weilingwith.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: deleteDeviceGroup
<公共请求参数>

Input: 

```
tccli weilingwith DeleteDeviceGroup --cli-unfold-argument  \
    --Id 0 \
    --WorkspaceId 1000 \
    --ApplicationToken abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

