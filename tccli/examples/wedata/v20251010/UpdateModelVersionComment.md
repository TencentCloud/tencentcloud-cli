**Example 1: 修改模型版本描述**

修改模型版本描述

Input: 

```
tccli wedata UpdateModelVersionComment --cli-unfold-argument  \
    --CatalogName yb_test05 \
    --SchemaName sc_test05 \
    --ModelName randyrren1 \
    --NewComment NewComment \
    --ModelVersion 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "ModelVersion": {
                "Aliases": [],
                "Audit": {
                    "CreatedAt": "1761907624030",
                    "Creator": "1290245077@qq.com",
                    "LastModifiedAt": "1761908807510",
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
        "RequestId": "92c1b047-3299-409e-8b94-14a6b34d811a"
    }
}
```

