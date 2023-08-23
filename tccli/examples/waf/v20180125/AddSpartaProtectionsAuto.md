**Example 1: 批量添加域名**

用户批量添加域名的场景

Input: 

```
tccli waf AddSpartaProtectionsAuto --cli-unfold-argument  \
    --Domain abc
```

Output: 
```
{
    "Response": {
        "FailedInfos": [
            {
                "Domain": "abc",
                "Message": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

