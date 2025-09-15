**Example 1: 查询座席状态历史示例**

查询座席状态历史示例

Input: 

```
tccli ccc DescribeStaffStatusHistory --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --StaffUserId foo@tencent.com \
    --StartTimestamp 1756297161 \
    --EndTimestamp 1756815561
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Cursor": "MTc1NjgwMDU0ODI3NSx3ZWlqdW55aUB0ZW5jZW50LmNvbSww",
                "SessionId": "75d7fb65-878c-4db2-8b3a-4484f9e3b931",
                "Status": "busy",
                "Timestamp": 1756800548
            },
            {
                "Cursor": "MTc1NjgwMDU1NzE0OCx3ZWlqdW55aUB0ZW5jZW50LmNvbSwx",
                "SessionId": "",
                "Status": "notReady",
                "Timestamp": 1756800557
            },
            {
                "Cursor": "MTc1NjgwMjk1MzE4OSx3ZWlqdW55aUB0ZW5jZW50LmNvbSw1",
                "SessionId": "",
                "Status": "free",
                "Timestamp": 1756802953
            },
            {
                "Cursor": "MTc1NjgwMjk4MjM5MSx3ZWlqdW55aUB0ZW5jZW50LmNvbSw2",
                "SessionId": "",
                "Status": "afterCallWork",
                "Timestamp": 1756802982
            }
        ],
        "RequestId": "df0c7f16-1886-4b98-ae1d-6fb8ac3464b9"
    }
}
```

