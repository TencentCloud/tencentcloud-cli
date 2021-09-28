**Example 1: 修改集群密码**

修改集群密码

Input: 

```
tccli tcaplusdb ModifyClusterPassword --cli-unfold-argument  \
    --ClusterId 23311894780 \
    --OldPassword canmkdmk1215LM \
    --NewPassword 99c59cb345c61063db \
    --OldPasswordExpireTime '2020-09-22 00:00:00'
```

Output: 
```
{
    "Response": {
        "RequestId": "8cEcE3E8-2fE2-6d4b-5E34-Fdc01E35f2C6"
    }
}
```

