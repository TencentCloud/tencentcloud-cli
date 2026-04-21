**Example 1: 查询**



Input: 

```
tccli bi DescribeUserGroupTreeList --cli-unfold-argument  \
    --ProjectId 674 \
    --Keyword 
```

Output: 
```
{
    "Response": {
        "Msg": "默认业务成功",
        "RequestId": "N_Jevw74-Kc4T-4JX1-88hD-IC_qLCaVmdVgX1GU",
        "Extra": "",
        "Data": [
            {
                "Id": 12,
                "GroupName": "总办",
                "ParentId": -1,
                "ParentName": null,
                "IsDefault": 0,
                "AdminUserId": "hoo",
                "UserList": null,
                "Description": null,
                "Location": 1,
                "Children": null,
                "HasChildren": false
            }
        ]
    }
}
```

