**Example 1: 手动刷新轮转密码**

POST / HTTP/1.1
Host: cdb.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ResetPassword
<公共请求参数>

Input: 

```
tccli cdb ResetPassword --cli-unfold-argument  \
    --InstanceId abc \
    --User abc \
    --Host abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

