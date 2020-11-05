**Example 1: Changing cluster password**

This example shows you how to change a cluster password.

Input: 

```
tccli tcaplusdb ModifyClusterPassword --cli-unfold-argument  \
    --ClusterId 23311894780\
    --OldPassword canmkdmk1215LM\
    --NewPassword 99c59cb345c61063db\
    --OldPasswordExpireTime 2019-08-26%2017%3A25%3A00
```

Output: 
```
{
    "Response": {
        "RequestId": "8cEcE3E8-2fE2-6d4b-5E34-Fdc01E35f2C6"
    }
}
```

