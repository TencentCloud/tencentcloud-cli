**Example 1: 印章授权申请下发**

给指定人员下发印章授权

Input: 

```
tccli ess CreateSealPolicy --cli-unfold-argument  \
    --SealId yDxbNUyKQDx3oAUuO4zjEBQGidlGe4hP \
    --Policy  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj \
    --Expired 1736906734 \
    --Users.0.UserId yDRSRUUgygj6rqouUuO4zjESlnSFPcIE
```

Output: 
```
{
    "Response": {
        "RequestId": "49500cb4-ca5e-4da0-93fb-e15f3a710ed7 ",
        "UserIds": []
    }
}
```

