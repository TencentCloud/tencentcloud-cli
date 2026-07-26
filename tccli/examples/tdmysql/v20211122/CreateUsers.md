**Example 1: 批量创建用户**



Input: 

```
tccli tdmysql CreateUsers --cli-unfold-argument  \
    --InstanceId tdsql3-831053d8 \
    --Users.0.UserName test1 \
    --Users.0.Host % \
    --Password t******3 \
    --Description 测试账号 \
    --EncryptedPassword *******x****************pjao7Sj*T******************nJ*****pbM**S8u2J*D**W*******JMa8VJ*I1GQ*chMe3kxu*******g2oRiFkt*HIP+u**vT*1*lSV*M******e***3*LKTj******************BTmW**GJDu********L**M*dF****t*****wk7+******L*************s*GMuG0pWC**F******O*l2******PEDyQo2d0**n************E******j/b2M8*NrWgS***+n/*****T4*0**biInLgzOBsB4/M******Kp*******
```

Output: 
```
{
    "Response": {
        "FlowId": 4295045717,
        "RequestId": "f597ced6-79fd-4a60-980c-acde7b9a316a"
    }
}
```

