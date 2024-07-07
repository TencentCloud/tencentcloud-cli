**Example 1: 关闭实例账户密码轮转**

POST / HTTP/1.1
Host: cdb.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DeleteRotationPassword
<公共请求参数>

Input: 

```
tccli cdb DeleteRotationPassword --cli-unfold-argument  \
    --InstanceId abc \
    --User abc \
    --Host abc \
    --Password abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

