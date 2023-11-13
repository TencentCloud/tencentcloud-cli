**Example 1: 删除单个用户的印章授权**

1.指定AppId为yDwfwUUgygormhg1UuS2eARxjMT0mxAw
2.指定子客企业OpenId为org_dianziqian
3.指定要操作的印章Id为yDRSRUUgygj******uO4zjEuBzwyiofZ
4.指定要删除授权的用户userId为yDxbWUyKQDx7OZUuO4zjESvEkRMHc55R

Input: 

```
tccli essbasic ChannelDeleteSealPolicies --cli-unfold-argument  \
    --Agent.ProxyOrganizationOpenId org_dianziqian \
    --Agent.ProxyOperator.OpenId n9527 \
    --Agent.AppId yDwfwUUgygormhg1UuS2eARxjMT0mxAw \
    --SealId yDRSRUUgygj******uO4zjEuBzwyiofZ \
    --UserIds yDxbWUyKQDx7OZUuO4zjESvEkRMHc55R
```

Output: 
```
{
    "Response": {
        "RequestId": "yDasdfasdfxxxxxJNR"
    }
}
```

