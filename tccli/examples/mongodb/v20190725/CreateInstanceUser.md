**Example 1: 创建用户**



Input: 

```
tccli mongodb CreateInstanceUser --cli-unfold-argument  \
    --InstanceId cmgo-******** \
    --UserName testuser1 \
    --Password ********* \
    --EncryptedPassword ***o*****DJ67kN52GK8oC49foA**+rXHRLrL6t2N7***CiKTN/mGSkMfDIh7vSrArnyk3ccBpG***Q***SUP/6uGotJaRLmN**O*B*1b1f**Cd7cEg*G3d****W*****v*a*V*l1w**68*btB*U*jH*******+cRO**PEhB**fEUgJ*mW************SrsUf***xPpL8E*q2x4Lljb*m*****+VLJL*7**UfFz**YSX48+Co*dAO*******1/*hGeCf**09yV0gJHa+zyas4Arbrr*Y5tEG3Ox**fh***gIrBBeEx1ZY**VnFBRs+699JijqQRlnZcZTl5WH**w== \
    --Database admin \
    --Description 测试用 \
    --EnablePasswordRotation 0
```

Output: 
```
{
    "Response": {
        "FlowId": 1750660112001309,
        "RequestId": "81b1c606-daa6-4778-aedf-84dc896469d2"
    }
}
```

