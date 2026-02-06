**Example 1: 修改数据源**



Input: 

```
tccli wedata UpdateDataSource --cli-unfold-argument  \
    --Id 62266 \
    --ProjectId 1460947878944567296 \
    --ProdConProperties None \
    --DevConProperties None \
    --ProdFileUpload.TrustStore None \
    --ProdFileUpload.KeyStore None \
    --ProdFileUpload.CoreSite None \
    --ProdFileUpload.HdfsSite None \
    --ProdFileUpload.HiveSite None \
    --ProdFileUpload.HBASESite None \
    --ProdFileUpload.KeyTab None \
    --ProdFileUpload.KRB5Conf None \
    --ProdFileUpload.PrivateKey None \
    --ProdFileUpload.PublicKey None \
    --DevFileUpload.TrustStore None \
    --DevFileUpload.KeyStore None \
    --DevFileUpload.CoreSite None \
    --DevFileUpload.HdfsSite None \
    --DevFileUpload.HiveSite None \
    --DevFileUpload.HBASESite None \
    --DevFileUpload.KeyTab None \
    --DevFileUpload.KRB5Conf None \
    --DevFileUpload.PrivateKey None \
    --DevFileUpload.PublicKey None \
    --DisplayName mysql_22_33 \
    --Description None
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "7468019d-ac08-43db-a4d4-9b04be755f78"
    }
}
```

