**Example 1: 手动刷新轮转密码**

POST / HTTP/1.1
Host: cdb.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: ResetPassword
<公共请求参数>

Input: 

```
tccli cdb ResetPassword --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv \
    --User andy \
    --Host 172.1.1.1
```

Output: 
```
{
    "Response": {
        "RequestId": "d5b053f3-d58e-4048-aef9-b8cc9f044951"
    }
}
```

