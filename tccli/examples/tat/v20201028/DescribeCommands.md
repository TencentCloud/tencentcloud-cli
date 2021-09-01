**Example 1: 使用 CommandId 查询命令**



Input: 

```
tccli tat DescribeCommands --cli-unfold-argument  \
    --CommandIds cmd-dvstpcyy \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "eb973a12-71e3-4c0c-b1d8-4b863e5f5daf",
        "TotalCount": 1,
        "CommandSet": [
            {
                "CommandId": "cmd-dvstpcyy",
                "CommandName": "run-command",
                "Description": "whoami",
                "FormattedDescription": "",
                "CreatedBy": "USER",
                "Content": "d2hvYW1p",
                "CommandType": "SHELL",
                "WorkingDirectory": "/root/",
                "Timeout": 60,
                "EnableParameter": false,
                "DefaultParameters": "",
                "Username": "root",
                "Tags": [
                    {
                        "Value": "test-key",
                        "Key": "test-value"
                    }
                ],
                "CreatedTime": "2020-11-02T02:48:11+00:00",
                "UpdatedTime": "2020-11-02T02:48:11+00:00"
            }
        ]
    }
}
```

**Example 2: 使用 command-name Filter 查询**



Input: 

```
tccli tat DescribeCommands --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name command-name \
    --Filters.0.Values second-command first-command
```

Output: 
```
{
    "Response": {
        "RequestId": "6b215093-e1f6-4803-b84a-a230849e88d1",
        "TotalCount": 2,
        "CommandSet": [
            {
                "CommandId": "cmd-hb2q34lk",
                "CommandName": "second-command",
                "Description": "ps",
                "FormattedDescription": "",
                "CreatedBy": "USER",
                "Content": "cHM=",
                "CommandType": "SHELL",
                "WorkingDirectory": "/root/",
                "Timeout": 60,
                "EnableParameter": false,
                "DefaultParameters": "",
                "Username": "root",
                "Tags": [
                    {
                        "Value": "test-key",
                        "Key": "test-value"
                    }
                ],
                "CreatedTime": "2020-10-30T07:19:52+00:00",
                "UpdatedTime": "2020-10-30T07:19:52+00:00"
            },
            {
                "CommandId": "cmd-63usjhmq",
                "CommandName": "first-command",
                "Description": "hello world!",
                "FormattedDescription": "",
                "CreatedBy": "USER",
                "Content": "cHM=",
                "CommandType": "SHELL",
                "WorkingDirectory": "/",
                "Timeout": 600,
                "EnableParameter": false,
                "DefaultParameters": "",
                "Username": "root",
                "Tags": [
                    {
                        "Value": "test-key",
                        "Key": "test-value"
                    }
                ],
                "CreatedTime": "2020-10-26T11:26:07+00:00",
                "UpdatedTime": "2020-11-09T08:12:45+00:00"
            }
        ]
    }
}
```

**Example 3: 使用 created-by Filter 查询**



Input: 

```
tccli tat DescribeCommands --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --Filters.0.Name created-by \
    --Filters.0.Values USER
```

Output: 
```
{
    "Response": {
        "RequestId": "6b215093-e1f6-4803-b84a-a230849e88d1",
        "TotalCount": 2,
        "CommandSet": [
            {
                "CommandId": "cmd-hb2q34lk",
                "CommandName": "second-command",
                "Description": "ps",
                "FormattedDescription": "",
                "CreatedBy": "USER",
                "Content": "cHM=",
                "CommandType": "SHELL",
                "WorkingDirectory": "/root/",
                "Timeout": 60,
                "EnableParameter": false,
                "DefaultParameters": "",
                "Username": "root",
                "Tags": [],
                "CreatedTime": "2020-10-30T07:19:52+00:00",
                "UpdatedTime": "2020-10-30T07:19:52+00:00"
            }
        ]
    }
}
```

**Example 4: 使用tag:tag-key Filter 查询命令**



Input: 

```
tccli tat DescribeCommands --cli-unfold-argument  \
    --Filters.0.Values test-value \
    --Filters.0.Name tag:test-key
```

Output: 
```
{
    "Response": {
        "RequestId": "33d3d954-f73a-4a7f-869b-8792bc7a6f13",
        "TotalCount": 1,
        "CommandSet": [
            {
                "CommandId": "cmd-38ps9q4p",
                "CommandName": "tag-test-1",
                "Description": "",
                "FormattedDescription": "",
                "CreatedBy": "USER",
                "Content": "cHMK",
                "CommandType": "SHELL",
                "WorkingDirectory": "/root",
                "Timeout": 60,
                "EnableParameter": false,
                "DefaultParameters": "",
                "Username": "root",
                "Tags": [
                    {
                        "Key": "test-key",
                        "Value": "test-value"
                    }
                ],
                "CreatedTime": "2021-05-12T02:49:04Z",
                "UpdatedTime": "2021-05-12T02:49:04Z"
            }
        ]
    }
}
```

