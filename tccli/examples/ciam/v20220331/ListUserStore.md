**Example 1: 查询用户目录列表**



Input: 

```
tccli ciam ListUserStore --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "UserStoreSet": [
            {
                "TenantId": "tenantId",
                "UserStoreLogo": "https://aa.com/bb.png",
                "UserStoreDesc": "管理应用和用户",
                "UserStoreName": "目录1",
                "UserNum": 10,
                "UserStoreId": "2c3aca3b****************a7efe88e",
                "AppNum": 0,
                "LastStatus": true,
                "DefaultStatus": true,
                "CreateDate": 1706682491339,
                "LastStatusTime": 1713168583556,
                "UserStoreProtocolHost": "leecpn"
            }
        ],
        "RequestId": "e2e9e8aa********************9ab34c6e"
    }
}
```

