**Example 1: 删除单点登录企业员工**

删除单点登录应用号为【yDtrTUUckp94bix0UEbASLp1TuHxTYTS】下面OpenId 为【rUHYMgaz8aNm2IP3Pn8m5q6I3yJDojClFl555uLyeM0】的员工。
当前员工仅做过导入，并没有跟腾讯电子签里面的企业员工进行绑定，
解除绑定成功。

Input: 

```
tccli ess DeleteSingleSignOnEmployees --cli-unfold-argument  \
    --Operator.UserId yDwf3UUckps8dvypUEfH3DjwIpMfa0uw \
    --Operator.ClientIp 8.8.8.8 \
    --SsoApplicationId yDtrTUUckp94bix0UEbASLp1TuHxTYTS \
    --OpenId rUHYMgaz8aNm2IP3Pn8m5q6I3yJDojClFl555uLyeM0
```

Output: 
```
{
    "Response": {
        "RequestId": "s1758723730900664241"
    }
}
```

