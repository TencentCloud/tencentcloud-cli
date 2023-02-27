**Example 1: 撤销个人资源权限**

撤销素材 Id `5fd8ad3d628dc30001bd0895` 对团队 `cmetid_afd3ad3d6289k390d9dk09ad0` 授予的读权限。

Input: 

```
tccli cme RevokeResourceAuthorization --cli-unfold-argument  \
    --Authorizees.0.Type TEAM \
    --Authorizees.0.Id cmetid_afd3ad3d6289k390d9dk09ad0 \
    --Operator user_id_1c5ebebd4392343b6489560 \
    --Platform test \
    --Owner.Type PERSON \
    --Owner.Id user_id_1c5ebebd4392343b6489560 \
    --Resources.0.Type MATERIAL \
    --Resources.0.Id 5fd8ad3d628dc30001bd0895 \
    --Permissions R
```

Output: 
```
{
    "Response": {
        "RequestId": "d1c5eb0e-e499-4419-b465-60c097fbb65b"
    }
}
```

