**Example 1: 示例**

示例

Input: 

```
tccli trocket DescribeMQTTUserList --cli-unfold-argument  \
    --InstanceId mqtt-47ka4rdr \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "CreatedTime": 1705392159000,
                "ModifiedTime": 1705392159000,
                "Password": "sunjianxiong",
                "PermRead": true,
                "PermWrite": true,
                "Remark": "",
                "Username": "user1"
            }
        ],
        "RequestId": "8e86117c-a56c-4598-9e1f-4a039eed6e3a",
        "TotalCount": 1
    }
}
```

