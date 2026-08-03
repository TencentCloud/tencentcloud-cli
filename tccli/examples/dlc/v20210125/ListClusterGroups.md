**Example 1: 列出所有集群组**



Input: 

```
tccli dlc ListClusterGroups --cli-unfold-argument  \
    --Page 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Page": 1,
        "PageSize": 10,
        "TotalPages": 1,
        "Items": [
            {
                "Id": "rayclustergroup-h5l7xk-cw8w",
                "Name": "生产环境集群组",
                "Description": "用于生产环境的集群组",
                "Config": "config-content",
                "AppId": 260090589,
                "Uin": "700002467852",
                "SubAccountUin": "700002467852",
                "CreateTime": 1774256065032,
                "UpdateTime": 1774256065032,
                "Deleted": false
            }
        ],
        "RequestId": "dffa8e31-2df1-4f61-9e88-df82ec7d7ae8"
    }
}
```

