**Example 1: 示例**



Input: 

```
tccli cwp ModifyWebPageProtectDir --cli-unfold-argument  \
    --ProtectDirAddr /data/www/ \
    --ProtectDirName 网站根目录 \
    --ProtectFileType .php;.html;.js \
    --HostConfig.0.Quuid 机器Quuid \
    --HostConfig.0.ProtectSwitch 1 \
    --HostConfig.0.AutoRecovery 1
```

Output: 
```
{
    "Response": {
        "RequestId": "g54f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

