**Example 1: 查询密钥对列表**

本示例用于用户查询密钥对列表

Input: 

```
tccli cvm DescribeKeyPairs --cli-unfold-argument  \
    --Filters.0.Name key-name \
    --Filters.0.Values MyKeyPair \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "KeyPairSet": [
            {
                "AssociatedInstanceIds": [],
                "CreatedTime": "2025-10-16T08:12:48Z",
                "Description": "",
                "KeyId": "skey-1q8j7b93",
                "KeyName": "MyKeyPair",
                "ProjectId": 0,
                "PublicKey": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC8gSdflU6iZDlLp3uRgfIQ7d9gl4SzF2yO9BJ1VyzhgWkbYsUS8u7qbwxC6UeAc8364FhT4MjVjXi/+6hYpDnnMiK6lqKBxotLupUtkVmYt+osdPP+y3OcCzTqHWCsY3s7AvyvD41+nuH6LrpXZ4LlHJynPc66eqd5gpnCyg2O1sxW+pd2Zigk0QGWiCuVtm4ICEp3DNHG/9wlVzd++xODf398JU3ebxBsXfe46mFSkyBVbsJLuNueZd4eGDS3q0WhimnvpgZoYOGsNPl4GBLCGOHWZrl/9hE+az6P8W7QwpVe5gvy5MG3usk6zpc0f/diZrdXX7 skey-1q8j7b93",
                "Tags": [
                    {
                        "Key": "MyKeyPairTagKey",
                        "Value": "MyKeyPairTagValue"
                    }
                ]
            }
        ],
        "RequestId": "eebd54d0-a305-4716-9a84-6017ac14e8c8",
        "TotalCount": 120
    }
}
```

