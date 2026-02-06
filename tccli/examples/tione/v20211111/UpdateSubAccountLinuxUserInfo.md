**Example 1: UpdateSubAccountLinuxUserInfo**

更新LinuxUser信息

Input: 

```
tccli tione UpdateSubAccountLinuxUserInfo --cli-unfold-argument  \
    --SubAccountList.0.Uin 100055132983 \
    --SubAccountList.0.SubUin 100033176827 \
    --SubAccountList.0.SubUinName ExampleUser \
    --SubAccountList.0.LinuxUid 50000 \
    --SubAccountList.0.LinuxGid 50000
```

Output: 
```
{
    "Response": {
        "RequestId": "30841715-2516-4a28-a4fa-4b5a62ea9ded"
    }
}
```

