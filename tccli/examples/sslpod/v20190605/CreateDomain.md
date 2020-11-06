**Example 1: 通过域名端口添加监控**



Input: 

```
tccli sslpod CreateDomain --cli-unfold-argument  \
    --Domain cloud.tencent.com \
    --Tags 123 \
    --IP 1.1.1.1 \
    --ServerType 0 \
    --Notice True \
    --Port 443
```

Output: 
```
{
    "Response": {
        "RequestId": "9f50312e-cfd7-47ac-b0a5-383991a24cd6"
    }
}
```

