**Example 1: 获取数据目录详情列表**

获取数据目录详情列表

Input: 

```
tccli wedata ListCatalogs --cli-unfold-argument  \
    --WorkspaceId default \
    --MaxResults 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Audit": {
                        "CreatedAt": "1761297897122",
                        "Creator": "1290245077@qq.com",
                        "LastModifiedAt": "0",
                        "LastModifier": ""
                    },
                    "Comment": "asads",
                    "Id": "047dd000-89cc-4835-b0c5-b09e528c3890",
                    "MetaOwner": {
                        "FullName": "myq_test1234",
                        "Owner": "1290245077@qq.com",
                        "OwnerType": "user"
                    },
                    "Name": "myq_test1234",
                    "Operator": "1290245077@qq.com",
                    "Properties": [
                        {
                            "Key": "tccatalog.identifier",
                            "Value": "tccatalog.v1.uid4104946694037711100"
                        }
                    ],
                    "Status": "2",
                    "Type": "MODEL"
                }
            ],
            "NextPageToken": "eyJvZmZzZXQiOjF9"
        },
        "RequestId": "6ac069ac-2d09-4e6a-b802-d5befa4fc6cc"
    }
}
```

**Example 2: 根据类型筛选示例**

根据类型筛选示例

Input: 

```
tccli wedata ListCatalogs --cli-unfold-argument  \
    --WorkspaceId defa \
    --MaxResults 10 \
    --Types VOLUME
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Audit": {
                        "CreatedAt": "1763390502132",
                        "Creator": "wedata30-dev@tencent.com",
                        "CreatorName": "wedata30-dev@tencent.com",
                        "LastModifiedAt": "1763390502132",
                        "LastModifier": "wedata30-dev@tencent.com",
                        "LastModifierName": "wedata30-dev@tencent.com"
                    },
                    "Comment": "micofywang_volume",
                    "Id": "d9ac34b2-2277-4c1f-b5fe-6591b1dc919a",
                    "MetaOwner": {
                        "FullName": "micofywang_volume",
                        "Owner": "700002164618",
                        "OwnerName": "wedata30-dev@tencent.com",
                        "OwnerType": "user"
                    },
                    "Name": "micofywang_volume",
                    "Operator": "wedata30-dev@tencent.com",
                    "Properties": [
                        {
                            "Key": "tccatalog.identifier",
                            "Value": "tccatalog.v1.uid3742685767363361395@1300055887_ap-guangzhou"
                        },
                        {
                            "Key": "cos-access-key-id",
                            "Value": "AKIDa7Xm7FCvSmuraDPlvvkOusrkU6HMGyS"
                        },
                        {
                            "Key": "cos-secret-access-key",
                            "Value": "teDZjfS8cv76sSpcHYdEE6nHdR6yjRbX"
                        },
                        {
                            "Key": "credential-providers",
                            "Value": "cos-secret-key"
                        },
                        {
                            "Key": "disable-filesystem-ops",
                            "Value": "true"
                        },
                        {
                            "Key": "filesystem-providers",
                            "Value": "cos"
                        }
                    ],
                    "Status": "2",
                    "Type": "VOLUME"
                }
            ],
            "NextPageToken": ""
        },
        "RequestId": "77fa4bd5-aebb-4f95-b1cc-efc597c69ae8"
    }
}
```

