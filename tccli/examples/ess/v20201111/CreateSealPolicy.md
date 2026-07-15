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

**Example 2: 针对用印的合同授权**



Input: 

```
tccli ess CreateSealPolicy --cli-unfold-argument  \
    --Operator.UserId yDtT9UUckp9fjxkfUu1yXuRSuJNQ0bO6 \
    --Users.0.UserId yDtT9UUckp9fjxkfUu1yXuRSuJNQ0bO6 \
    --SealId yDClqUUckpaj38v1UmGrVdB8iMEXjdyR \
    --Expired 1789442071 \
    --UserIds yDtT9UUckp9fjxkfUu1yXuRSuJNQ0bO6 \
    --Policy 测试******* \
    --AuthorizationFlows.FlowIds yD3a2UUckpmwknasU1Uy3T8nlBwEDRxj
```

Output: 
```
{
    "Response": {
        "SealOperatorVerifyPath": "",
        "SealOperatorVerifyQrcodeUrl": "",
        "UserIds": [
            "yDtT9UUckp9fjxkfUu1yXuRSuJNQ0bO6"
        ],
        "RequestId": "3add2dda-bd7b-471a-9bbf-85e814de2dab"
    }
}
```

