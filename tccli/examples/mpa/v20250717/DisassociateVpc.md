**Example 1: 解关联VPC**



Input: 

```
tccli mpa DisassociateVpc --cli-unfold-argument  \
    --AgentAcceleratorId aat-ei8fzf27 \
    --VpcInfo.0.VpcId vpc-gmjjk6sn \
    --VpcInfo.0.VpcRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "TaskId": "0a459a12-74b0-418a-80fb-a76e2c837d71",
        "RequestId": "a361d374-0273-40b9-bcf0-a840636b52d0"
    }
}
```

