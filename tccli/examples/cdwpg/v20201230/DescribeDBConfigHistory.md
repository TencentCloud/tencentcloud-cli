**Example 1: 配置更改历史查询**



Input: 

```
tccli cdwpg DescribeDBConfigHistory --cli-unfold-argument  \
    --InstanceId cdwpg-xx \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ConfigHistory": [
            {
                "CreatedAt": "2025-03-17T18:07:25+08:00",
                "Id": 4615,
                "InstanceId": "cdwpg-9jcyk7yp",
                "NodeType": "cn",
                "ParamName": "lock_timeout",
                "ParamNewValue": "29999",
                "ParamOldValue": "30000",
                "Status": "success",
                "UpdatedAt": "2025-03-17T18:07:51+08:00"
            },
            {
                "CreatedAt": "2025-02-27T16:44:39+08:00",
                "Id": 4570,
                "InstanceId": "cdwpg-9jcyk7yp",
                "NodeType": "cn",
                "ParamName": "modify_hba_params",
                "ParamNewValue": "[{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"9.0.0.0\",\"mask\":\"24\",\"method\":\"trust\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"0.0.0.0\",\"mask\":\"0\",\"method\":\"trust\"}]",
                "ParamOldValue": "[{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"9.0.0.0\",\"mask\":\"24\",\"method\":\"trust\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"9.0.0.0\",\"mask\":\"24\",\"method\":\"trust\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"0.0.0.0\",\"mask\":\"0\",\"method\":\"trust\"}]",
                "Status": "success",
                "UpdatedAt": "2025-02-27T16:45:06+08:00"
            },
            {
                "CreatedAt": "2025-02-27T16:43:27+08:00",
                "Id": 4569,
                "InstanceId": "cdwpg-9jcyk7yp",
                "NodeType": "cn",
                "ParamName": "modify_hba_params",
                "ParamNewValue": "[{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"9.0.0.0\",\"mask\":\"24\",\"method\":\"trust\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"9.0.0.0\",\"mask\":\"24\",\"method\":\"trust\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"0.0.0.0\",\"mask\":\"0\",\"method\":\"trust\"}]",
                "ParamOldValue": "[{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"9.0.0.0\",\"mask\":\"24\",\"method\":\"trust\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"0.0.0.0\",\"mask\":\"0\",\"method\":\"trust\"}]",
                "Status": "success",
                "UpdatedAt": "2025-02-27T16:43:54+08:00"
            },
            {
                "CreatedAt": "2025-02-27T16:40:42+08:00",
                "Id": 4568,
                "InstanceId": "cdwpg-9jcyk7yp",
                "NodeType": "cn",
                "ParamName": "modify_hba_params",
                "ParamNewValue": "[{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"9.0.0.0\",\"mask\":\"24\",\"method\":\"trust\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"0.0.0.0\",\"mask\":\"0\",\"method\":\"trust\"}]",
                "ParamOldValue": "[{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"0.0.0.0\",\"mask\":\"0\",\"method\":\"trust\"}]",
                "Status": "success",
                "UpdatedAt": "2025-02-27T16:41:09+08:00"
            },
            {
                "CreatedAt": "2025-02-27T16:39:21+08:00",
                "Id": 4567,
                "InstanceId": "cdwpg-9jcyk7yp",
                "NodeType": "cn",
                "ParamName": "modify_hba_params",
                "ParamNewValue": "[{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"0.0.0.0\",\"mask\":\"0\",\"method\":\"trust\"}]",
                "ParamOldValue": "[{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"9.0.0.0\",\"mask\":\"24\",\"method\":\"trust\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"::\",\"mask\":\"0\",\"method\":\"md5\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"0.0.0.0\",\"mask\":\"0\",\"method\":\"md5\"}]",
                "Status": "success",
                "UpdatedAt": "2025-02-27T16:39:47+08:00"
            },
            {
                "CreatedAt": "2025-02-27T16:37:32+08:00",
                "Id": 4566,
                "InstanceId": "cdwpg-9jcyk7yp",
                "NodeType": "cn",
                "ParamName": "max_connections",
                "ParamNewValue": "626",
                "ParamOldValue": "625",
                "Status": "success",
                "UpdatedAt": "2025-02-27T16:37:59+08:00"
            },
            {
                "CreatedAt": "2025-02-26T18:03:03+08:00",
                "Id": 4565,
                "InstanceId": "cdwpg-9jcyk7yp",
                "NodeType": "cn",
                "ParamName": "modify_hba_params",
                "ParamNewValue": "[{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"9.0.0.0\",\"mask\":\"24\",\"method\":\"trust\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"::\",\"mask\":\"0\",\"method\":\"md5\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"0.0.0.0\",\"mask\":\"0\",\"method\":\"md5\"}]",
                "ParamOldValue": "[{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"9.0.0.0\",\"mask\":\"24\",\"method\":\"trust\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"::\",\"mask\":\"0\",\"method\":\"md5\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"0.0.0.0\",\"mask\":\"0\",\"method\":\"trust\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"0.0.0.0\",\"mask\":\"0\",\"method\":\"md5\"}]",
                "Status": "success",
                "UpdatedAt": "2025-02-26T18:03:31+08:00"
            },
            {
                "CreatedAt": "2025-02-26T18:01:33+08:00",
                "Id": 4564,
                "InstanceId": "cdwpg-9jcyk7yp",
                "NodeType": "cn",
                "ParamName": "modify_hba_params",
                "ParamNewValue": "[{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"9.0.0.0\",\"mask\":\"24\",\"method\":\"trust\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"::\",\"mask\":\"0\",\"method\":\"md5\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"0.0.0.0\",\"mask\":\"0\",\"method\":\"trust\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"0.0.0.0\",\"mask\":\"0\",\"method\":\"md5\"}]",
                "ParamOldValue": "[{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"::\",\"mask\":\"0\",\"method\":\"md5\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"0.0.0.0\",\"mask\":\"0\",\"method\":\"trust\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"0.0.0.0\",\"mask\":\"0\",\"method\":\"md5\"}]",
                "Status": "success",
                "UpdatedAt": "2025-02-26T18:02:01+08:00"
            },
            {
                "CreatedAt": "2025-02-26T17:59:57+08:00",
                "Id": 4563,
                "InstanceId": "cdwpg-9jcyk7yp",
                "NodeType": "cn",
                "ParamName": "modify_hba_params",
                "ParamNewValue": "[{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"0.0.0.0\",\"mask\":\"0\",\"method\":\"trust\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"0.0.0.0\",\"mask\":\"0\",\"method\":\"md5\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"::\",\"mask\":\"0\",\"method\":\"md5\"}]",
                "ParamOldValue": "[{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"::\",\"mask\":\"0\",\"method\":\"md5\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"0.0.0.0\",\"mask\":\"0\",\"method\":\"trust\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"0.0.0.0\",\"mask\":\"0\",\"method\":\"md5\"}]",
                "Status": "success",
                "UpdatedAt": "2025-02-26T18:00:25+08:00"
            },
            {
                "CreatedAt": "2025-02-26T17:55:50+08:00",
                "Id": 4562,
                "InstanceId": "cdwpg-9jcyk7yp",
                "NodeType": "cn",
                "ParamName": "modify_hba_params",
                "ParamNewValue": "[{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"0.0.0.0\",\"mask\":\"0\",\"method\":\"trust\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"0.0.0.0\",\"mask\":\"0\",\"method\":\"md5\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"::\",\"mask\":\"0\",\"method\":\"md5\"}]",
                "ParamOldValue": "[{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"0.0.0.0\",\"mask\":\"0\",\"method\":\"md5\"},{\"type\":\"host\",\"database\":\"all\",\"user\":\"all\",\"address\":\"::0\",\"mask\":\"0\",\"method\":\"md5\"}]",
                "Status": "success",
                "UpdatedAt": "2025-02-26T17:56:16+08:00"
            }
        ],
        "RequestId": "3c291e0a-f7b3-4965-86d3-c606bb0c703d",
        "TotalCount": 10
    }
}
```

