**Example 1: CreateDarInstance**



Input: 

```
tccli cynosdb CreateDarInstance --cli-unfold-argument  \
    --ModelConfig.Model hunyuan-t1 \
    --ModelConfig.ApiKey sk-tp-R****zh**HX*n**r***9AU8**********r**S**h*D**1Dxk \
    --ModelConfig.Passport Abc@12345 \
    --Name xiuwenqin \
    --Zone ap-hongkong-3 \
    --Cpu 1 \
    --Mem 1 \
    --Storage 50 \
    --VpcId vpc-e864hbjo \
    --SubnetId subnet-0ao81x2n
```

Output: 
```
{
    "Response": {
        "InstanceId": "dar-l1jaunpu",
        "TaskId": 4,
        "RequestId": "2631ffa6-fe91-4650-b771-ec18bab62e08"
    }
}
```

