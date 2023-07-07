**Example 1: 创建印章授权**

给指定用户下发印章授权

Input: 

```
tccli essbasic ChannelCreateSealPolicy --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId yDxAyUyK****cb7u0jQn0Zh7f7 \
    --Agent.ProxyOperator.OpenId 732aaef****541b89c49e0cc \
    --Agent.AppId ed68bc6***********0214e4e \
    --SealId yDRTZxxxxxJNR \
    --UserIds yDdzlxxxxxopk
```

Output: 
```
{
    "Response": {
        "UserIds": [
            "yDdzlxxxxxopk"
        ],
        "RequestId": "fdasfavdavxxxx"
    }
}
```

