**Example 1: 为集群指定队列生成注册码**



Input: 

```
tccli thpc GenerateRegisterCode --cli-unfold-argument  \
    --ClusterId hpc-kywo***a \
    --QueueName compute \
    --ExpireSeconds 3600
```

Output: 
```
{
    "Response": {
        "ExpireAt": 1778041412,
        "RegisterCode": "***********************0*******3*m*w*SIs******l*********M****D*0**************9uI************md***9*****c3*********1*********j****A***A*N****DM**n******3**P*Jz*********m*****9*****vudEt-**7j*",
        "RequestId": "c7be8eb1-046a-4b48-9b29-535543cb9a3f"
    }
}
```

