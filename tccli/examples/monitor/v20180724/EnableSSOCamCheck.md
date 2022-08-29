**Example 1: EnableSSOCamCheck**

SSO单点登录时，开启cam鉴权

Input: 

```
tccli monitor EnableSSOCamCheck --cli-unfold-argument  \
    --InstanceId grafana-abcdefgh \
    --EnableSSOCamCheck True
```

Output: 
```
{
    "Response": {
        "RequestId": "qmunlpf51noe13qp5vyvg7mq5t4t4w6u"
    }
}
```

