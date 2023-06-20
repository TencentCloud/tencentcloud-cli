**Example 1: 获取临时访问凭证**

授权临时访问凭证具有以下权限：
{"version":"2.0","statement":[{"effect":"allow","action":["name/cos:PutObject"],"resource":["qcs::cos:ap-beijing:uid/123456:prefix//123456/bucketA/*"]}]}

注意，因为GET请求需要给所有参数做urlencode，所以下面示例中的Policy参数是做了两次urlencode的结果。

Input: 

```
tccli sts GetFederationToken --cli-unfold-argument  \
    --Name SUN \
    --Policy %257B%2522version%2522%3A%25222.0%2522%2C%2522statement%2522%3A%255B%257B%2522effect%2522%3A%2522allow%2522%2C%2522action%2522%3A%255B%2522name%2Fcos%3APutObject%2522%255D%2C%2522resource%2522%3A%255B%2522qcs%3A%3Acos%3Aap-beijing%3Auid%2F123456%3Aprefix%2F%2F123456%2FbucketA%2F%2A%2522%255D%257D%255D%257D
```

Output: 
```
{
    "Response": {
        "Credentials": {
            "Token": "kTRt***Jb7m",
            "TmpSecretId": "AKID****CjE6",
            "TmpSecretKey": "Eo28***7ps="
        },
        "Expiration": "2023-06-14T05:06:57Z",
        "ExpiredTime": 1686719217,
        "RequestId": "59a5e07e-4147-4d2e-a808-dca76ac5b3fd"
    }
}
```

