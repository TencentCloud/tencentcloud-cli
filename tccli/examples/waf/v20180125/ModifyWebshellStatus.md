**Example 1: 设置域名webshell检测状态**



Input: 

```
tccli waf ModifyWebshellStatus --cli-unfold-argument  \
    --Webshell ''{"Domain":"lsd.qcloudwaf.com", "Status":1}''
```

Output: 
```
{
    "Response": {
        "Success": {
            "Code": "Success",
            "Message": "Success"
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

