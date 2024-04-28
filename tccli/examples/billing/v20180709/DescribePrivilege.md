**Example 1: uin不是最高优先级特权用户**

响应中IsTopPriorityPrivilegeUin为false，说明该uin不是最高优先级特权用户；因入参StopIfNotTopPriorityPrivilegeUin设置为true，则不会返回特权信息。

Input: 

```
tccli billing DescribePrivilege --cli-unfold-argument  \
    --PrivilegeKeyList fallback_guarantee
```

Output: 
```
{
    "Response": {
        "IsTopPriorityPrivilegeUin": false,
        "PrivilegeKeyItemList": [],
        "RequestId": "7c140555-a07b-454c-83d1-066dbea3a51d"
    }
}
```

**Example 2: uin是最高优先级特权用户**

响应中IsTopPriorityPrivilegeUin为true，说明该uin是最高优先级特权用户；入参StopIfNotTopPriorityPrivilegeUin无效，返回特权的兜底特权状态为打开。

Input: 

```
tccli billing DescribePrivilege --cli-unfold-argument  \
    --PrivilegeKeyList fallback_guarantee
```

Output: 
```
{
    "Response": {
        "IsTopPriorityPrivilegeUin": true,
        "PrivilegeKeyItemList": [
            {
                "PrivilegeKey": "fallback_guarantee",
                "Status": 3
            }
        ],
        "RequestId": "fe4c010a-8f84-40c9-92a7-e7a0465e044b"
    }
}
```

