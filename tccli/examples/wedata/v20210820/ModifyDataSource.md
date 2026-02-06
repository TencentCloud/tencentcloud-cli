**Example 1: ModifyDataSource**

数据源管理-修改数据源

Input: 

```
tccli wedata ModifyDataSource --cli-unfold-argument  \
    --Name batch_hardxia \
    --Category DB \
    --Type MYSQL \
    --ID 62221 \
    --Params {"connectType":"public","authorityType":"true","passwordChanged":false,"advanceParams":[],"deployType":"CONNSTR_PUBLICDB","url":"jdbc:mysql://43.140.253.103:63925/di_mysql_test?useSSL=false&serverTimezone=UTC","username":"wedata","password":"","type":"MYSQL","newType":1} \
    --Description  \
    --Display batch_hardxia \
    --DatabaseName di_mysql_test \
    --Instance  \
    --Status 2 \
    --ClusterId  \
    --OwnerProjectId 1486804694126882816 \
    --OwnerProjectName [数据集成_联调] \
    --OwnerProjectIdent 数据集成_联调 \
    --COSBucket wedata-fusion-dev-1257305158 \
    --COSRegion ap-nanjing \
    --ProjectId 1486804694126882816
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "f05776c5-5746-4327-8e1f-cbc1936bebba"
    }
}
```

