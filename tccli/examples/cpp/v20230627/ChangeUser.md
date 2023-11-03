**Example 1: 抖音作者增删**

抖音作者增删

Input: 

```
tccli cpp ChangeUser --cli-unfold-argument  \
    --UserId MS4wLjABAAAAKRsxsTnDn9WCxYtOUpOf1-CCflveqs0kHpzVDBbRglD4QhCNbmWfqO4ciQOgdzod \
    --UserName 福贵剪影 \
    --Homepage https://www.douyin.com/user/MS4wLjABAAAAKRsxsTnDn9WCxYtOUpOf1-CCflveqs0kHpzVDBbRglD4QhCNbmWfqO4ciQOgdzod \
    --Status 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "UserId": "abc",
            "UserName": "abc",
            "Homepage": "abc",
            "Status": 0
        },
        "RequestId": "abc"
    }
}
```

