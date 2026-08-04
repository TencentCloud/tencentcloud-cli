**Example 1: 更新集群组**



Input: 

```
tccli dlc UpdateClusterGroup --cli-unfold-argument  \
    --Id rayclustergroup-h5l7xk-cw8w \
    --Description 更新后的描述 \
    --Config config-content
```

Output: 
```
{
    "Response": {
        "Id": "rayclustergroup-h5l7xk-cw8w",
        "Name": "生产环境集群组",
        "Description": "更新后的描述",
        "Config": "config-content",
        "AppId": 260090589,
        "Uin": "700002467852",
        "SubAccountUin": "700002467852",
        "CreateTime": 1774256065032,
        "UpdateTime": 1774256065032,
        "Deleted": false,
        "RequestId": "dffa8e31-2df1-4f61-9e88-df82ec7d7ae8"
    }
}
```

