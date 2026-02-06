**Example 1: DescribeSubAccountLinuxUserInfos**

批量查询子账号Linux用户信息

Input: 

```
tccli tione DescribeSubAccountLinuxUserInfos --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "5dee4285-b87f-4005-ad48-45729a5942d8",
        "SubAccountList": [
            {
                "LinuxGid": 20000,
                "LinuxUid": 20001,
                "SubUin": "0",
                "SubUinName": "ExampleUser",
                "Uin": "100033122983"
            }
        ]
    }
}
```

