**Example 1: 修改模型版本别名**

修改模型版本别名

Input: 

```
tccli wedata UpdateModelVersionAliases --cli-unfold-argument  \
    --CatalogName yb_test05 \
    --SchemaName sc_test05 \
    --ModelName randyrren1 \
    --ModelVersion 1 \
    --AddedAliases UpdateModelVersionAliases1
```

Output: 
```
{
    "Response": {
        "Data": {
            "ModelVersion": {
                "Aliases": [
                    "UpdateModelVersionAliases1"
                ],
                "Audit": {
                    "CreatedAt": "1761907624030",
                    "Creator": "1290245077@qq.com",
                    "LastModifiedAt": "1761908974391",
                    "LastModifier": "1290245077@qq.com"
                },
                "CatalogName": "",
                "Comment": "NewComment",
                "ModelName": "",
                "Properties": [
                    {
                        "Key": "tccatalog.identifier",
                        "Value": "tccatalog.v1.uid4002408858624546662"
                    }
                ],
                "SchemaName": "",
                "Uri": "cosn://easechen-zd-251409079/randyrren/1",
                "Version": "1"
            }
        },
        "RequestId": "52d6e072-1a72-4f72-89cb-d87cbf30ccc5"
    }
}
```

