**Example 1: 示例**

 

Input: 

```
tccli cwp DescribePublicProxyInstallCommand --cli-unfold-argument  \
    --Ip 0.0.0.0
```

Output: 
```
{
    "Response": {
        "KeepAliveCommand": " wget --no-check-certificate https://up.yd.qcloud.com/ydeyes/download/install_proxy.sh -O install_proxy.sh && sudo bash install_proxy.sh",
        "NginxCommand": "wget --no-check-certificate https://up.yd.qcloud.com/ydeyes/download/install_proxy.sh -O install_proxy.sh && sudo bash install_proxy.sh",
        "RequestId": "5921b751-84f3-4332-a89f-fca2a139bd10"
    }
}
```

