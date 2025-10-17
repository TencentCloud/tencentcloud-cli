**Example 1: CreateDataSource**

数据源管理-创建数据源

Input: 

```
tccli wedata CreateDataSource --cli-unfold-argument  \
    --Name mysql_test \
    --Category DB \
    --Type MYSQL \
    --OwnerProjectId 1486804694126882816 \
    --OwnerProjectName DI \
    --OwnerProjectIdent 数据集成_联调 \
    --Params {"connectType":"public","authorityType":"true","advanceParams":[],"deployType":"CONNSTR_PUBLICDB","url":"jdbc:mysql://43.140.253.103:63925/di_mysql_test?useSSL=false&serverTimezone=UTC","username":"wedata","password":"1234","type":"MYSQL","newType":1} \
    --Description  \
    --Display  \
    --Status 1 \
    --ClusterId  \
    --COSBucket wedata-fusion-dev-1257305158 \
    --COSRegion ap-nanjing \
    --ConnectResult 
```

Output: 
```
{
    "Response": {
        "Data": 62235,
        "RequestId": "3fee373e-8cd9-48a0-8003-12dbe3658ba7"
    }
}
```

