**Example 1: 获取成员标签检测不合规资源列表**

获取成员标签检测不合规资源列表

Input: 

```
tccli organization ListNonCompliantResource --cli-unfold-argument  \
    --MaxResults 10 \
    --PaginationToken  \
    --MemberUin 1111111111
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Resource": "qcs::vpc::uin/1111111111:subnet/subnet-test1",
                "ComplianceDetails": {
                    "ComplianceStatus": true,
                    "KeysWithNonCompliantValues": [
                        "abc"
                    ],
                    "NonCompliantKeys": [
                        "abc"
                    ]
                },
                "Tags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ]
            }
        ],
        "PaginationToken": "fgh363",
        "RequestId": "242effbd-5220-4776-9cc2-87afbdcb68db"
    }
}
```

