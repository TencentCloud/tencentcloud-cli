**Example 1: 账号组详情**

账号组详情

Input: 

```
tccli config DescribeAggregator --cli-unfold-argument  \
    --OwnerUin 234234324 \
    --AccountGroupId ca-sdfs7734h24h3
```

Output: 
```
{
    "Response": {
        "AggregatorAccounts": [
            {
                "MemberUin": 23423424,
                "MemberName": "test_user"
            }
        ],
        "Type": "RD",
        "Description": "全局账号组",
        "RequestId": "73d105d8-5820-434f-9fac-76f926e61c",
        "Name": "名称",
        "AggregatorStatus": 1
    }
}
```

