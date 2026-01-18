**Example 1: 根据McpServerProjectIds查询**



Input: 

```
tccli lighthouse DescribeMcpServerProjects --cli-unfold-argument  \
    --McpServerProjectIds lhmsp-bs542be1h7 \
    --Limit 1 \
    --Offset 0 \
    --WithDownloadUrl False
```

Output: 
```
{
    "Response": {
        "McpServerProjectSet": [
            {
                "CodeFileSet": [
                    {
                        "CodeSha256": "8507cf30271499328bd2fc939e00ce6c2c7a53cb013c372c88dcc32b5466d4ef",
                        "CosKey": "agent_generated/actived/700001768676/lhmsp-bs542be1h7/requirements.txt",
                        "FileName": "requirements.txt"
                    }
                ],
                "EnvSet": [
                    {
                        "Key": "MYSQL_HOST",
                        "Value": ""
                    }
                ],
                "McpServerProjectId": "lhmsp-bs542be1h7",
                "Name": "MySqlDataService"
            }
        ],
        "TotalCount": 1,
        "RequestId": "914e80bb-ae47-49ac-9bc7-b2f42c760487"
    }
}
```

