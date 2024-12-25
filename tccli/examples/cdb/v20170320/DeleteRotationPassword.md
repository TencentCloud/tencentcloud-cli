**Example 1: 关闭实例账户密码轮转**

POST / HTTP/1.1
Host: cdb.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DeleteRotationPassword
<公共请求参数>

Input: 

```
tccli cdb DeleteRotationPassword --cli-unfold-argument  \
    --InstanceId cdb-0zgqlqmd \
    --User andy \
    --Host 192.1.1.1 \
    --Password Andy454545
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

