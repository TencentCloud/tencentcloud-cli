**Example 1: 获取域名分组列表**

 

Input: 

```
tccli dnspod DescribeDomainGroupList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "GroupList": [
            {
                "GroupId": 1,
                "GroupName": "默认分组",
                "GroupType": "system",
                "Size": 3
            }
        ]
    }
}
```

