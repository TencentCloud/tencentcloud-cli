**Example 1: 查询实例管理终端地址**

本示例用于查询实例管理终端地址。

Input: 

```
tccli cvm DescribeInstanceVncUrl --cli-unfold-argument  \
    --InstanceId ins-r7ov05ke
```

Output: 
```
{
    "Response": {
        "InstanceVncUrl": "wss%3A%2F%2Fgzvnc.qcloud.com%3A26789%2Fvnc%3Fs%3DY1hMdzVUNDh5Wm1aR0VCekdhTmJqdEdMaitCWHoralA5N2Frdk9SQlYvSXFjNlVEVng4RnZFMXUvVW9QWFpwbmFDcWlOdDJIbUJxSTZDL0RXcHZxYnZZMmRkWWZWcEZia2lyb09XMzdKNmM9%26password%3D%26isWindows%3Dfalse%26isUbuntu%3Dfalse",
        "RequestId": "3a685fe7-327a-4815-9bb4-c20587f25939"
    }
}
```

