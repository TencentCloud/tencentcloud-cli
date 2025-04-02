**Example 1: 查询角色信息**



Input: 

```
tccli trocket DescribeRolesInternal --cli-unfold-argument  \
    --InstanceId rocketmq-47x924vjavzz \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "AccessKey": "eyJrZXlJZCI6I",
                "Name": "zdl30ddfdadadd"
            },
            {
                "AccessKey": "eyJrZXlJZCI6InJvY2tldG1xL",
                "Name": "a3324r23fsefsdsfdf"
            },
            {
                "AccessKey": "eyJrZXlJZC",
                "Name": "abcdefasda"
            }
        ],
        "RequestId": "849d5961-41d3-457b-876c-1c709f16e374",
        "TotalCount": 3
    }
}
```

