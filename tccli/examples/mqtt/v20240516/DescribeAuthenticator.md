**Example 1: 示例**

示例

Input: 

```
tccli mqtt DescribeAuthenticator --cli-unfold-argument  \
    --InstanceId mqtt-dmzeoj58 \
    --Type HTTP
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Authenticators": [
            {
                "Config": "{\"headers\":[{\"key\":\"user\",\"value\":\"${username}\"}],\"endpoint\":\"127.0.0.1\",\"method\":\"Post\",\"readTimeout\":1,\"connectTimeout\":1,\"body\":[{\"key\":\"user\",\"value\":\"${username}\"}],\"concurrency\":1}",
                "CreateTime": 1731036362,
                "Remark": "this is remark",
                "Status": "open",
                "Type": "HTTP"
            }
        ],
        "RequestId": "756b8ee7-00e8-48ea-94f2-02eead2a5067"
    }
}
```

