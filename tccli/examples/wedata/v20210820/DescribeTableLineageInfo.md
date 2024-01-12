**Example 1: 1**

1

Input: 

```
tccli wedata DescribeTableLineageInfo --cli-unfold-argument  \
    --Direction abc \
    --InputDepth 0 \
    --OutputDepth 0 \
    --ExtParams.0.Name abc \
    --ExtParams.0.Value abc \
    --Data.ProjectId abc \
    --Data.DatasourceId abc \
    --Data.TableId abc \
    --Data.Params.0.Name abc \
    --Data.Params.0.Value abc \
    --Data.ParentSet abc \
    --Data.ChildSet abc \
    --Data.ExtParams.0.Name abc \
    --Data.ExtParams.0.Value abc \
    --Data.Id abc \
    --Data.MetastoreType abc \
    --Data.MetastoreTypeName abc \
    --Data.TableName abc \
    --Data.QualifiedName abc \
    --Data.DownStreamCount 0 \
    --Data.UpStreamCount 0 \
    --Data.Description abc \
    --Data.PrefixPath abc \
    --Data.CreateTime abc \
    --Data.ModifyTime abc \
    --Data.Tasks abc \
    --IgnoreTemp True \
    --RecursiveSecond True
```

Output: 
```
{
    "Response": {
        "TableLineageBasicInfo": {
            "ProjectId": "abc",
            "DatasourceId": "abc",
            "TableId": "abc",
            "Params": [
                {
                    "Name": "abc",
                    "Value": "abc"
                }
            ],
            "ParentSet": "abc",
            "ChildSet": "abc",
            "ExtParams": [
                {
                    "Name": "abc",
                    "Value": "abc"
                }
            ],
            "Id": "abc",
            "MetastoreType": "abc",
            "MetastoreTypeName": "abc",
            "TableName": "abc",
            "QualifiedName": "abc",
            "DownStreamCount": 0,
            "UpStreamCount": 0,
            "Description": "abc",
            "PrefixPath": "abc",
            "CreateTime": "abc",
            "ModifyTime": "abc",
            "Tasks": [
                "abc"
            ]
        },
        "RequestId": "abc"
    }
}
```

**Example 2: 错误1**

错误1

Input: 

```
tccli wedata DescribeTableLineageInfo --cli-unfold-argument  \
    --Direction 1 \
    --InputDepth 1 \
    --OutputDepth 1 \
    --Data.ProjectId 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "内部服务错误，请稍后重试。"
        },
        "RequestId": "ca8fa3de-0024-4054-a5db-4919705ee8ee"
    }
}
```

**Example 3: 错误2**

错误2

Input: 

```
tccli wedata DescribeTableLineageInfo --cli-unfold-argument  \
    --Direction 1 \
    --InputDepth 1 \
    --OutputDepth 1 \
    --ExtParams.0.Name 1 \
    --Data.ProjectId 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InternalError",
            "Message": "内部服务错误，请稍后重试。"
        },
        "RequestId": "079c4b23-fd76-4e91-b366-dc0c0a76c032"
    }
}
```

